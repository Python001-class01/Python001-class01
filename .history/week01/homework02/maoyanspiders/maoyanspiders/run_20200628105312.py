import os
import sys
from scrapy.cmdline import execute

base_dir = os.path.dirname(os.path.abspath(_file_))
sys.path.append(base_dir)
os.chdir(base_dir)
execute(['scrapy','crawl','movies'])