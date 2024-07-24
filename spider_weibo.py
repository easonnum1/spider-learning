import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
依赖lib：
pip install selenium
pip3 install webdriver_manager 
"""


def get_weibo_hot_search():
    url = 'https://s.weibo.com/top/summary'

    # selenium 就是一个无UI的浏览器，为什么要引入它，因为要假装我们是浏览器，然后去加载JS后才能得到真正的html
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 无头模式，不打开浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)  # 等待页面加载

    html = etree.HTML(driver.page_source)
    driver.quit()

    hot_searches = []

    for i in range(1, 51):  # 通常热搜榜有50条
        xpath_title = f'/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr[{i}]/td[2]/a/text()'
        xpath_link = f'/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr[{i}]/td[2]/a/@href'
        title = html.xpath(xpath_title)
        link = html.xpath(xpath_link)

        if title and link:
            hot_searches.append({'title': title[0], 'link': 'https://s.weibo.com' + link[0]})

    return hot_searches


if __name__ == "__main__":
    hot_searches = get_weibo_hot_search()

    if hot_searches:
        for idx, search in enumerate(hot_searches):
            print(f"{idx + 1}. {search['title']}")
            print(f"   Link: {search['link']}")
