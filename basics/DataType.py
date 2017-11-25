'''
Created on Nov, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial usage or without the consent of the author
'''

class SaleHistory:
    
    def __init__(self, product, amount = 5):
        self.__product = product
        self.__amount = amount
        
    def getProduct(self):
        return self.__product
    
    def getSaleAmount(self):
        return self.__amount
    
class Product:
    
    def __init__(self, name, destination = None, url = None, currentPrice = -1, rating = 0):
        self.__name = name
        self.__curentPrice = currentPrice
        self.__rating = rating
        self.__destination = destination
        self.__productUrl = url
        
    def getProductName(self):
        return self.__name
    
    def getCurrentPrice(self):
        return self.__curentPrice
    
    def getProductRating(self):
        return self.__rating
    
    def getMainDestination(self):
        return self.__destination
    
    def getProductUrl(self):
        return self.__productUrl
    
    def setDestination(self, destination):
        self.__destination = destination
    
    def setUrl(self, url):
        self.__productUrl = url
        