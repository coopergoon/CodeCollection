# coding=utf8
"""
爬取西刺代理网站，但是发现爬取下来的都是垃圾
想放弃.......
"""

import csv
import random
import sys
import telnetlib
import time

import arrow
import requests
from lxml import etree

import config

reload(sys)
sys.setdefaultencoding("utf-8")


class Baisc(object):
    def __init__(self):
        pass

    def down_load(self, url):
        headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': random.choice(setting.USER_AGENT),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        time.sleep(random.uniform(1, 3))
        response = requests.get(url, headers=headers)
        return response

    def save(self, content, save_path):
        # content_temp = [x.decode('utf-8').encode('GB2312') for x in content]
        with open(save_path, 'ab+', ) as f:
            writer = csv.writer(f)
            writer.writerow(content)


class ProxyCrawler(Baisc):
    def __init__(self):
        super(Baisc, self).__init__()
        self.file1 = open('./ip.csv', 'w+')  # 打开文件
        self.file1.truncate()  # 清空文件内容

    def start(self):
        for number in range(1, setting.PAGE_NUMBER):
            url = 'http://www.xicidaili.com/wt/' + str(number)
            response = self.down_load(url=url)
            self.parse(response=response)


    def parse(self, response):
        html = etree.HTML(response.content)
        # odd标签下
        ip_list_odd = html.xpath("//tr[@class='odd']/td[2]/text()")
        port_list_odd  = html.xpath("//tr[@class='odd']/td[3]/text()")
        speed_list_odd  = html.xpath("//tr[@class='odd']/td[7]/div/@title")
        live_time_list_odd  = html.xpath("//tr[@class='odd']/td[9]/text()")
        verify_time = html.xpath("//tr[@class='odd']/td[10]/text()")

        for temp in range(len(ip_list_odd)):
            current_time = arrow.now()
            verify_time_each = arrow.get('20' + verify_time[temp] )

            # 转换为秒
            if '分钟' in live_time_list_odd[temp]:
                live_time_list_odd[temp] = int(live_time_list_odd[temp][:-2])*60
            elif '天' in  live_time_list_odd[temp]:
                live_time_list_odd[temp] = int(live_time_list_odd[temp][:-1])*24*60*60
            else:
                live_time_list_odd[temp] = int(live_time_list_odd[temp][:-2])*60*60


            if (current_time - verify_time_each).seconds > live_time_list_odd[temp]:
                content = [ip_list_odd[temp], port_list_odd[temp], speed_list_odd[temp], live_time_list_odd[temp]]
                save_path = './ip.csv'
                self.save(content=content, save_path=save_path)

        # 空值
        ip_list = html.xpath("//tr[@class='odd']/following-sibling::*[1]/td[2]/text()")
        port_list = html.xpath("//tr[@class='odd']/following-sibling::*[1]/td[3]/text()")
        speed_list = html.xpath("//tr[@class='odd']/following-sibling::*[1]/td[7]/div/@title")
        live_time_list = html.xpath("//tr[@class='odd']/following-sibling::*[1]/td[9]/text()")

        for temp in range(len(ip_list)):
            content = [ip_list[temp], port_list[temp], speed_list[temp], live_time_list[temp]]
            save_path = './ip.csv'
            self.save(content=content, save_path=save_path)


    def verify_ip(self):
        try:
            telnetlib.Telnet('121.232.145.57', port=9000, timeout=5)
        except:
            pass
        else:
            pass


if __name__ == '__main__':

    proxy_crawler = ProxyCrawler()
    # proxy_crawler.start()
    proxy_crawler.verify_ip()
