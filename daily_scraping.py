import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import time


os.chdir("/scripts")

if os.path.exists(".env"):
    load_dotenv()



SCRAPER_LOGIN = os.environ["SCRAPER_LOGIN"]
SCRAPER_PASSWORD = os.environ["SCRAPER_PASSWORD"]
SCRAPER_URL = os.environ["SCRAPER_URL"] 

data = {
    'spider': 'news_spider',
    'project': 'default',
    'search_from': 'FROM',
    'search_to': 'TO',
    'locale': 'LOCALE',
    'crimes_file': 'CRIMES',
}


for line in open("scraping_map.txt"):
    locale = line.split(" ")[0].rstrip()
    crimes_file = line.split(" ")[1].rstrip()
    data["search_from"] = datetime.today().strftime('%Y-%m-%d')
    data["search_to"] = (datetime.strptime(data["search_from"], '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    data["locale"] = locale
    data["crimes_file"] = crimes_file
    response = requests.post(SCRAPER_URL, data=data, auth=(SCRAPER_LOGIN, SCRAPER_PASSWORD))
    print("Request for: ", locale, crimes_file)
    print(response.json())
    time.sleep(5)
    