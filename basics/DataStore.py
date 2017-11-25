# -*- coding: utf-8 -*-
'''
Created on Nov 23, 2017
@author: double_kingdoms
@attention: This code is for learning purpose. Don't propagate it for commercial use or without the consent of author
'''
import csv
from basics import DataType
class CsvFileWriter:
    
    def __init__(self, filePath = None, isNewFile = True):
        self.__filePath = filePath if filePath is not None else "/Users/haopan/Desktop/XCData/xiechengDomestic.csv"
        self.__isNewFile = isNewFile
        self.initFileWriter()
        
    def writeDataRow(self, saleHistory):
        if not isinstance(saleHistory, DataType.SaleHistory):
            print 'Data Type mis-match exception, required: DataType.SaleHistory'
            return
            
        saleAmount = str(saleHistory.getSaleAmount())
        product = saleHistory.getProduct()
            
        productName = product.getProductName()
        productPrice = product.getCurrentPrice()
        productRating =product.getProductRating()
        destination = product.getMainDestination()
        
        print destination + ", "+ productName + ",  people: " + saleAmount + ",  price: " + productPrice + ",  score: " + productRating
        #TODO: write data to .csv file
        
#         self.__writer.writerow({
#             'productName': productName,
#             'saleAmount': saleAmount})
    
    def initFileWriter(self):
        self.__csvfile = open(self.__filePath, 'a')
        self.__fieldNames = ['destination', 'productName', 'saleAmount', 'price', 'rating', 'url']
        self.__writer = csv.DictWriter(self.__csvfile, fieldnames = self.__fieldNames)
        
        if self.__isNewFile:
            self.__writer.writeheader()
            self.__isNewFile = False
            
    def closeFile(self):
        self.__csvfile.close()
        
    def getFilePath(self):
        return self.__filePath