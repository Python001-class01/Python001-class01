import threading
import requests
from queue import Queue
import json
from lxml import etree

dataQueue = Queue()

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
                page = self.queue.get()
                print(f"Thread id is {self.thread_id}, page is {page}")
                url=""

                try:
                    response = requests.get(url)
                    dataQueue.put(response.text)
                except Exception as e:
                    print(f"Download error:{e}")

class ParseThread(threading.Thread):
    def __init__(self, thread_id, queue, db_config):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.db_config = db_config

    def run(self):
        print(f"Start thread:{self.thread_id}")
        

