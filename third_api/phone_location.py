# coding=utf-8
"""
@version: 2017/12/15 015
@author: Suen
@contact: sunzh95@hotmail.com
@file: phone_location
@time: 18:19
@note:  ??
"""
#

import requests
import re
from bs4 import BeautifulSoup

db_local = 'A_MONGOCLIENT_DB'
db_xadmin = 'ANOTHER_MONGOCLIENT_DB'
cursor = 'A_MYSQL_CURSOR'


def get_area2(mobile):
    url = 'http://www.ip138.com:8080/search.asp?action=mobile&mobile=%s' % mobile
    resp = requests.get(url).content.decode('gbk')
    soup = BeautifulSoup(resp)
    data = soup.find_all('table', attrs={'style': 'border-collapse: collapse'})
    if not data:
        return '', ''
    data = data[0].text.replace('\n', '').replace(' ', '')
    res = re.search(r'卡号归属地(?P<city>(.+))卡类型(?P<style>(.+))区', data, re.MULTILINE)
    if res:
        city = res.groupdict().get('city', '')
        style = res.groupdict().get('style', '')
        return city, style
    return '', ''


def get_area(mobile):
    url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=%s' % mobile
    resp = requests.get(url).content
    resp = resp.decode('gbk')
    data = re.search(r'\s+province:\'(?P<city>(\W+))\',', resp, re.MULTILINE)
    city = data.groupdict().get('city') if data else ''
    data = re.search(r'\s+carrier:\'(?P<style>(\W+))\',', resp, re.MULTILINE)
    style = data.groupdict().get('style') if data else ''
    return city, style


def main():
    mobile = '18190331859'
    city, style = get_area(mobile)
    if not city and not style:
        city, style = get_area2(mobile)
    print(city, style)


if __name__ == '__main__':
    main()
