'''
Created on Nov, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial usage or without the consent of the author
'''
import requests
import random
import time

class NetworkConnectionAgent:
    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"]
        
        self.hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        
        self.ipList = [
            '223.68.1.38:8000',
            '124.88.67.54:81',
            '183.62.196.10:3128',
            '120.132.71.212:80',
            '117.158.1.210:9999',
            '124.88.67.31:843',
            '218.56.132.156:8080',
            '125.217.199.148:8197',
            '220.248.229.45:3128',
            '202.106.16.36:3128',
            '124.47.7.45:80',
            '124.47.7.38:80',
            '219.145.244.250:3128',
            '122.226.62.90:3128',
            '121.201.24.248:8088',
            '60.15.8.130:3128',
            '111.1.3.36:8000',
            '60.191.168.181:3128',
            '218.56.132.155:8080',
            '123.57.58.164:80',
            '124.88.67.32:81',
            '120.52.21.132:8082',
            '119.29.246.212:8888',
            '60.191.170.148:3128',
            '101.251.199.66:3128',
            '116.242.227.201:3128',
            '121.40.108.76:80',
            '59.51.27.213:3128',
            '123.13.204.109:9999',
            '58.59.68.91:9797']
        
        self.assignAgentProperties()
        
    def getResponse(self,url,tryTime, useFakeIp):
        try:
            time.sleep(1)
            if useFakeIp:
                return requests.get(url, headers=self.hdr, proxies=self.proxy, timeout=10)
            else :
                return requests.get(url, headers=self.hdr, timeout=10)
        except:
            tryTime -= 1
            print 'We are encountering connection error, retry times: '+ str(tryTime)
            self.assignAgentProperties()
            if tryTime == 0:
                print "Connection failed."
                return None
            else:
                return self.getResponse(url, tryTime, useFakeIp)
    
    def assignAgentProperties(self):
        self.hdr['User-Agent'] = random.choice(self.user_agent)
        self.proxy = {'http':''.join(str(random.choice(self.ipList)))}
        
                