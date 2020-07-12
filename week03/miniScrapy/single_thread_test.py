import requests
from lxml import etree
from fake_useragent import UserAgent
import json
import math

ua = UserAgent()

def crawl_film(city):
    result = get_next_page(1, city)
    totalPage = result['totalCount']
    resultSize = result['resultSize']
    pageCount = math.ceil(totalPage / resultSize)

    salary_list = get_salary_avg(result['result'])

    for p in range(2, pageCount+1):
        page_result = get_next_page(p, city)['result']
        salary_list += get_salary_avg(page_result)

    salary_sum = 0
    for i in salary_list:
        salary_sum += i
    average_salary = salary_sum / len(salary_list)
    return average_salary

def get_salary_avg(page_content):
    salary_list = []
    for r in range(0, len(page_content)):
    #     print(page_result[r]["companyFullName"], page_result[r]["positionName"], page_result[r["salary"])
        salary_range = page_content[r]["salary"]
        salary_range = salary_range.split("-")
        slow = salary_range[0].replace('k', '')
        shigh = salary_range[1].replace('k', '')
        average = (int(slow) + int(shigh)) / 2
        print(page_content[r]["salary"], average)
        salary_list.append(average)
    return salary_list
        
def get_next_page(page, city):
    s = requests.Session()
    url = f'https://www.lagou.com/jobs/positionAjax.json?px=default&city={city}&needAddtionalResult=false'
    headers = {
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'User-Agent': ua.random,
            'Referer':'https://www.lagou.com/jobs/list_Python'
    }
    s.headers['User-Agent'] = ua.random
    from_data = {
        'first': 'true',
        'pn':1,
        'kd':'Python'
    }
    get_url = 'https://www.lagou.com/jobs/list_Python'
    s.get(get_url, headers=headers)
    cookies = s.cookies

    response = s.post(url, data=from_data, cookies=cookies, headers=headers)
    json_data = json.loads(response.text)

    return json_data['content']['positionResult']
    

city_list = ["北京"]
# city_list = ["2", "3", "213", "215"]
for c in city_list:
    print(f"{c}的Python平均工资是:{crawl_film(c)}")