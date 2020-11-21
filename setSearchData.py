"""
@ encoding:utf-8
@ author:nxc
@ GitHub:
@ 获取语料资源存储为CSV格式
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


def get_html(url):
    try:
        header_reset = {'user-agent': 'Mozilla/5.0'}                # 防反爬
        r = requests.get(url, timeout=30, headers=header_reset)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        source = r.text
    except:
        raise Exception('链接访问失败,错误链接:' + url)
    return source


def get_max_page(soup):                 # 调整文件页数
    return 2534


def read_url_file():                    # 函数待用，用以在特殊情况下扩充语料库
    parents_url = " "
    parents_urls = list()
    with open('ParentsURL.txt', 'r', encoding='utf-8') as url_file:
        for line in url_file:
            if line[-1] == '\n':
                parents_urls.append(parents_url + line[:-1])
            else:
                parents_urls.append(parents_url + line)
    if not len(parents_urls):
        raise Exception('源url流读取失败或url文件为空')
    return parents_urls


def main():
    parents_url = "http://sousuo.gov.cn/s.htm?t=zhengcelibrary&q=&p="
    parents_source = get_html(parents_url)
    parents_soup = BeautifulSoup(parents_source, 'html.parser')
    max_page = get_max_page(parents_soup)
    pd_data = {'href': [], 'name': [], 'summary': [], 'type': [], 'time': []}
    pd_columns = ['href', 'name', 'summary', 'type', 'time']
    for p in range(max_page):
        print('*'*7 + "正在处理第{:d}页".format(p + 1) + '*'*7)
        try:
            child_url = parents_url + str(p)
            child_source = get_html(child_url)
            child_soup = BeautifulSoup(child_source, 'html.parser')
            child_data = child_soup.find_all(name='div', attrs={"class": "dys_middle_result_content_item"})
            for data in child_data:
                href = data.find_all(name='a')[0].attrs['href']
                name = data.find_all(name='h5')[0].getText()
                summary = data.find_all(name='p')[0].getText()
                _type_ = data.find_all(name='span')[0].getText()
                time = data.find_all(name='span')[1].getText()
                # 全部找到后再统一传入，防止程序报错对齐失败
                pd_data['href'].append(href)
                pd_data['name'].append(name)
                pd_data['summary'].append(summary)
                pd_data['type'].append(_type_)
                pd_data['time'].append(time)
        except:
            print("第{:d}页访问失败".format(p + 1))
        sleep(randint(3, 9))            # 随机睡眠程序4~8秒
    pd_data_frame = pd.DataFrame(data=pd_data, columns=pd_columns)
    pd_data_frame.to_csv('searchData.csv', encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    main()
