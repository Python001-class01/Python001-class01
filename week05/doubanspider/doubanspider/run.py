import os
import sys
from scrapy.cmdline import execute

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
os.chdir(base_dir)
execute(['scrapy', 'runspider', 'spiders/douban.py'])