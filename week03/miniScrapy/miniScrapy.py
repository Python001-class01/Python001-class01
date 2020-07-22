import threading
import requests
from queue import Queue
import json
from lxml import etree
from fake_useragent import UserAgent
import math
import pymysql
from db_config import configs
import traceback

dataQueue = Queue()
averageQueue = Queue()
flag = False


class CrawlerThread(threading.Thread):
    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        print(f"Start thread:{self.thread_id}")
        self.scheduler()
        print(f"Finish thread:{self.thread_id}")

    def scheduler(self):
        while True:
            if self.queue.empty():
                break
            else:
                city = self.queue.get()
                print(f"Thread id is {self.thread_id}, city is {city}")

                result = self.get_next_page(1, city)
                totalPage = result['totalCount']
                resultSize = result['resultSize']
                pageCount = math.ceil(totalPage / resultSize)
                # print(f"pageCount:{pageCount}")
                # salary_list = self.get_salary_avg(result['result'])

                dataQueue.put({city: result['result']})

                for p in range(2, pageCount+1):
                    page_result = self.get_next_page(p, city)['result']
                    dataQueue.put({city: page_result})

    def get_next_page(self, page, city):
        ua = UserAgent()
        s = requests.Session()
        url = f'https://www.lagou.com/jobs/positionAjax.json?px=default&city={city}&needAddtionalResult=false'
        headers = {
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'User-Agent': ua.random,
            'Referer': 'https://www.lagou.com/jobs/list_Python'
        }
        s.headers['User-Agent'] = ua.random
        from_data = {
            'first': 'true',
            'pn': page,
            'kd': 'Python'
        }
        get_url = 'https://www.lagou.com/jobs/list_Python'
        s.get(get_url, headers=headers)
        cookies = s.cookies

        response = s.post(url, data=from_data,
                          cookies=cookies, headers=headers)
        json_data = json.loads(response.text)

        return json_data['content']['positionResult']


class ParseThread(threading.Thread):
    def __init__(self, thread_id, queue, db_config):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.db_config = db_config

    def run(self):
        print(f"Start thread:{self.thread_id}")
        while not flag:
            try:
                item = self.queue.get(False)
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done()
            except Exception as e:
                # print(e)
                pass

        print(f"Finish thread:{self.thread_id}")

    def parse_data(self, item):
        try:
            self.get_salary_avg(item)
        except Exception as e:
            # print(e)
            pass

    # 一页的平均工资列表
    def get_salary_avg(self, page_content):
        # salary_list = []
        for city in page_content:
            #     print(page_result[r]["companyFullName"], page_result[r]["positionName"], page_result[r["salary"])

            for r in range(0, len(page_content[city])):
                salary_range = page_content[city][r]["salary"]
                salary_range = salary_range.split("-")
                slow = salary_range[0].replace('k', '')
                shigh = salary_range[1].replace('k', '')
                average = (int(slow) + int(shigh)) / 2
                # print(page_content[city][r]["salary"], average)
                # print(f"put {city}:{average} to averageQueue")
                averageQueue.put({city: average})


def save_to_database(result):
    if not isinstance(result, dict):
        print("Type error")
        return

    db = pymysql.connect(
        configs["host"], configs["user"], configs["password"], configs["database"])

    cursor = db.cursor()

    sql = """CREATE TABLE IF NOT EXISTS %s (
            CITY CHAR(20),
            SALARY FLOAT
        )""" % (configs["table"])
    cursor.execute(sql)

    for c in result:
        sql = """INSERT INTO %s (CITY, SALARY) VALUES ("%s", "%s")""" % (
            configs["table"], c, result[c])

        try:
            cursor.execute(sql)
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()


if __name__ == "__main__":
    cityQueue = Queue(4)
    city_list = ["北京", "上海", "广州", "深圳"]
    # city_list = ["深圳"]
    for city in city_list:
        cityQueue.put(city)

    crawler_thread = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for thread_id in crawl_name_list:
        thread = CrawlerThread(thread_id, cityQueue)
        thread.start()
        crawler_thread.append(thread)

    parser_thread = []
    parser_name_list = ['parse_1', 'parse_2', 'parse_3', 'parse_4']
    for thread_id in parser_name_list:
        thread = ParseThread(thread_id, dataQueue, None)
        thread.start()
        parser_thread.append(thread)

    for t in crawler_thread:
        t.join()

    flag = True
    average_dict = []

    for t in parser_thread:
        t.join()

    while not averageQueue.empty():
        # if averageQueue.not_empty:
        item = averageQueue.get()
        # print(item)
        average_dict.append(item)
    # print(average_dict)
    result_avg = {}

    count = 0
    total = {}
    for city in city_list:
        total[city] = [0, 0]

    for dic in average_dict:
        for key in dic:
            count += 1
            # print(dic[key])
            total[key][0] += dic[key]
            total[key][1] += 1

    salary_data = {}
    for city in total:
        avg = total[city][0] / total[city][1]
        # result_avg[key] = avg
        # print(f"{city}的Python平均工资是:{avg}")
        salary_data[city] = avg

    # salary_data = {"北京": 21.659744408945688, "上海": 19.271634615384617,
    #                "广州": 14.738805970149254, "深圳": 17.529891304347824}

    save_to_database(salary_data)
    print("exit main thread")
