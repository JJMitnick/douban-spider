# -*-coding:utf-8-*-
# @time: 2020/5/2 13:33
# @author: Mitnick
# @description: 豆瓣租房爬虫


import datetime
import time

import requests
import urllib3
from bs4 import BeautifulSoup

from mail import Mail
from settings import *

urllib3.disable_warnings()

url_set = set()


def spider():
    while True:
        # 爬虫休息时间，单位：秒
        sleep_time = random.randint(100, 300)
        try:
            # 邮件内容包含豆瓣的title和url
            mail_html = []
            # 支持多个key
            for k in KEYWORDS:
                url = INIT_URL.format(k)
                response = requests.get(url=url, headers=HEADERS, verify=False).content.decode('utf8')
                if '异常请求' in response:
                    time.sleep(sleep_time*100000)
                # 解析
                parse(response, mail_html)
                time.sleep(random.randint(10, 30))
            # 发邮件
            if len(mail_html) != 0:
                # 主题
                subject = '，'.join(k for k in KEYWORDS)
                # 邮件内容
                html = '<br>'.join(m for m in mail_html)
                mail = Mail()
                mail.send(receiver=RECEIVER, subject=subject[0:10], html=html)
            time.sleep(sleep_time)
        except:
            pass


def parse(response, mail_html):
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('tr', {'class': 'pl'})
    for item in items:
        td_time = item.find('td', {'class': 'td-time'})
        release_time_str = td_time.get('title')
        release_date_str = release_time_str.split(' ')[0]
        today = datetime.date.today()
        # 只要当天的数据
        if str(today) != release_date_str:
            break
        td_subject = item.find('td', {'class': 'td-subject'})
        ts_a = td_subject.find('a')
        url = ts_a.get('href')
        # 去重
        if url in url_set:
            continue
        title = ts_a.get('title')
        mail_html.append(title)
        mail_html.append(url)
        # 新增的数据加入去重队列
        url_set.add(url)


if __name__ == '__main__':
    spider()
