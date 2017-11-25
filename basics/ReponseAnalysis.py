# -*- coding: utf-8 -*-
'''
Created on Nov, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial usage or without the consent of the author
'''
from bs4 import BeautifulSoup
import re
from basics import AnalysisUtils
from basics.DataType import SaleHistory
from basics.DataType import Product
from basics.DataStore import CsvFileWriter

class ProductsAnalysisAgent:
    
    def __init__(self, productsUrlList, destination = None):
        self.__productsList = productsUrlList
        self.__destination = destination
        self.__analysisRecorder = CsvFileWriter()
        
    # return the SaleHistory object.
    def getProductSaleHistory(self, productContent):
        #TODO: 
        if productContent == None:
            print "product content should not be None."
            return None
        
        productSoup = BeautifulSoup(productContent, "lxml")
        
        product = Product(
            name = self.getProductName(productSoup),
            currentPrice = self.getProductPrice(productSoup),
            rating = self.getProductRating(productSoup),
            destination = self.__destination)
        
        saleHistory = SaleHistory(product, amount = self.getProductSaleAmount(productSoup))
        
        return saleHistory
        
    def getProductSaleAmount(self, productSoup):
        historyTag = productSoup.find("div", "comment_wrap")
        if historyTag == None :
            return "No Sale Amount"
        
        strs = unicode(historyTag.span.string)
        number = AnalysisUtils.stripNumberOutOfString(strs)
        return number[0]
        
    def getProductRating(self, productSoup):
        historyTag = productSoup.find("div", "comment_wrap")
        if historyTag == None :
            return "No Sale Amount"
        
        ratingTag = historyTag.find("a", "score")
        score = unicode(next(ratingTag.strings))
        return score
    
    def getProductName(self, productSoup):
        nameTag = productSoup.find("h1", itemprop = "name")
        if (nameTag == None):
            return "No Product Name"
        name = unicode(next(nameTag.strings))
        return name
    
    def getProductPrice(self, productSoup):
        pattern = re.compile(r'.+minPrice":(\d+),', re.DOTALL)
        scriptTag = productSoup.find("script", text = pattern)
        if scriptTag:
            match = pattern.search(scriptTag.text)
            if match:
                price = match.group(1)
                return price
        return "No Price"
        
    def analysisProducts(self):        
        for url in self.__productsList:
            productContent = AnalysisUtils.getUrlContentText(url)
            saleHistory = self.getProductSaleHistory(productContent)
            saleHistory.getProduct().setUrl(url)
            self.writeMyAnalysis(saleHistory)
    
    def writeMyAnalysis(self, saleHistory):
        self.__analysisRecorder.writeDataRow(saleHistory)
#         print "write success"
    
    def closeAnalysisRecorder(self):
        self.__analysisRecorder.closeFile()
        
class DomesticTravelAnalysisAgent:
    def __init__(self, homeUrl):
        self.TAG = "com.panha.ResponseAnalysisAgent"
        self.__homeUrl = homeUrl
        
    def getPopularCityUrls(self):
        content = AnalysisUtils.getUrlContentText(self.__homeUrl)
        if content == None :
            print self.TAG + "getAllCitiesTag() received None response"
            return None
        soup = BeautifulSoup(content, "lxml")
        allCitiesTag = soup.find("dt", text = "热门省份旅游").find_next_sibling()
        allCityUrls = []
        for child in allCitiesTag.children:
            if child.string == '\n':
                continue
            else:
                allCityUrls.append(AnalysisUtils.getUrlLinkFromTag(child))
        return allCityUrls
    
    def formCityUrl(self, cityUrl, page = 1):
        pageStr = "/p"+str(page)+"#_flta"
        return self.__homeUrl + cityUrl + pageStr

    
    def getProductsUrlFromCityContent(self, cityContent):
        if cityContent == None:
            print "city content none response Exception"
            return None
        
        citySoup = BeautifulSoup(cityContent, "lxml")
        productTags = citySoup.find_all("div", "product_main")
        
        productUrls = []
        for tag in productTags:
            productUrls.append(self.getProductUrlFromProductTag(tag))
        return productUrls
    
    def getProductUrlFromProductTag(self, tag):
        return AnalysisUtils.addUrlHeader(AnalysisUtils.getUrlLinkFromTag(tag.h2.a))
    
class Starter:
    def startDomesticTravelAnalysis(self, url):
        domesticeAgent = DomesticTravelAnalysisAgent(url)
        allCityUrls = domesticeAgent.getPopularCityUrls()
        for cityUrl in allCityUrls:
            wholeUrl = domesticeAgent.formCityUrl(cityUrl)
            #print "current Url: " + wholeUrl
            pageCount = int(AnalysisUtils.getPageCountFromContentText(AnalysisUtils.getUrlContentText(wholeUrl)))
            for page in range(pageCount):
#                 print "page " + str(page) + " is currently under searching"
                cityContent = AnalysisUtils.getUrlContentText(domesticeAgent.formCityUrl(cityUrl, page+1))
                productsUrlList = domesticeAgent.getProductsUrlFromCityContent(cityContent)
                productsAnalysis = ProductsAnalysisAgent(productsUrlList, AnalysisUtils.getDestinationNameFromUrlLink(cityUrl))
                productsAnalysis.analysisProducts()