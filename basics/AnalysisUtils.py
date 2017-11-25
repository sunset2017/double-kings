'''
Created on Nov, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial usage or without the consent of the author
'''

from basics.NetworkConnectionAgent import NetworkConnectionAgent
from bs4 import BeautifulSoup
from bs4 import element
import re

RETRY_TIMES = 100
USE_FAKE_IP = False

def getCurrentPagePosition():
    return None

def getUrlContentText(url):
    connectionAgent = NetworkConnectionAgent()
    response = connectionAgent.getResponse(url, RETRY_TIMES, USE_FAKE_IP)
    if response is not None: 
        return response.text
    else:
        print "Get Url content None response received"
        return None

def getUrlLinkFromTag(tag):
    if (tag == None) or (not isinstance(tag, element.Tag)):
        return None
    return tag.get('href')

def addUrlHeader(url, type = 0):
    if url == None:
        print "addUrlHeader none object received"
        return None
    
    if type == 0:
        return "http:" + url

def getPageCountFromContentText(content):
    soup = BeautifulSoup(content, "lxml")
    pageTag = soup.find("span", "c_page2_numtop")
    totalPage = stripNumberOutOfString(unicode(pageTag.string))[-1]
    return totalPage

def getCurrentPageIndex(content):
    soup = BeautifulSoup(content, "lxml")
    pageTag = soup.find("span", "c_page2_numtop")
    totalPage = stripNumberOutOfString(unicode(pageTag.string))[0]
    return totalPage

def stripNumberOutOfString(stringMsg):
    pattern = re.compile(r'\d+')
    result = re.findall(pattern, stringMsg)
    return result

def getDestinationNameFromUrlLink(url):
    pattern = re.compile(r'.+-([a-z]+)-')
    name = re.match(pattern, url)
    return name.group(1)
