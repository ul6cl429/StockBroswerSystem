# -*- coding: utf-8 -*-

from lxml import etree
from lxml import html
import urllib2

class StockID(object):

    def __init__(self):
        '''self.stockid = stockid
        self.Name = Name
        self.PER = PER
        self.YRate = YRate 
'''
    def fetchTWSEStockID(self):
        url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php'
        stockid = []
        Name = []
        PER = []
        YRate = []
        PBR = []
    
        output = []
        try:
            response = urllib2.urlopen(url)
            content = response.read()
#        print content
#        html = etree.HTML(content)
            html = etree.HTML(content)       
            table = html.xpath('//div[@id="tbl-containerx"]/table//tr/td[@class="basic2"][1]')
#        print table
            t0 = html.xpath('//div[@id="tbl-containerx"]/table//tr/td[@class="basic2"][2]') 
            t1 = html.xpath('//div[@id="tbl-containerx"]/table//tr/td[@class="basic2"][3]')    
            t2 = html.xpath('//div[@id="tbl-containerx"]/table//tr/td[@class="basic2"][4]')  
            t3 = html.xpath('//div[@id="tbl-containerx"]/table//tr/td[@class="basic2"][5]')     
            tt = []
            for id  in table:
                #tt.append(str(id.text))
                tt.append(id.text)
                stockid.append(tt)  
                tt = []
#            print tt
#            print stockid
            for id  in t0:
                Name.append(', '.join(id.text).encode('utf-8').decode('utf-8'))
#            print id.text      
            for id  in t1:
                #PER.append(str(id.text))
                PER.append(id.text)
#            print id.text      
            for id  in t2:
                #YRate.append(str(id.text))
                YRate.append(id.text)
#            print id.text  
            for id  in t3:
                #PBR.append(str(id.text))
                PBR.append(id.text)
#            print id.text   
#        print "len of stock id = %s"%len(stockid)
#        print "len of stock id = %s"%len(Name)
#        print "len of stock id = %s"%len(PER)
#        print "len of stock id = %s"%len(YRate)
#        print "len of stock id = %s"%len(PBR)
            tt = []
            for l in range(0,len(stockid)):
                tt = stockid[l]
                tt.append(Name[l])
                tt.append(PER[l])
                tt.append(YRate[l])
                tt.append(PBR[l])
#            output.append((stockid[l],Name[l],PER[l],YRate[l],PBR[l]))
                output.append(tt)
                tt = []

#            print output
#            print "len of stock id = %s"%len(output)
#        return tuple(stockid+Name+PER+YRate+PBR)
        
            return tuple(output) 
        #todo parse stock id from content
        except urllib2.HTTPError:
            print "%s not found!!"%url
    def fetchYahoo(self , stockid):
        Yahooid = []
        out = []
        print stockid
        url = ( 'https://tw.stock.yahoo.com/d/s/' +
                'company_%d.html') % stockid
        try:
            response = urllib2.urlopen(url)
            content = response.read()
#        print content
            html = etree.HTML(content)
                
            table = html.xpath("/html/body/table/tr[2]/td/table/tr//td")
#        print table
        
            for id  in table:
#       for data in range(0,len(table)):
                Yahooid.append(str(id.text).replace("元","").replace("%","").replace("每股淨值: ", ""))
#            print id.text   

            for l in range(0,len(Yahooid)):
                if l == 5:      
                #�{���ѧQ
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 9:    
                #�Ѳ��ѧQ
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 13:   #'�վl�t��'
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 17:   #���n�t��
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 40:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 42:
                    out.append(Yahooid[l])
#                print Yahooid[l]                
                elif l == 44:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 46:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 48:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 50:
                    out.append(Yahooid[l])                                
#                print Yahooid[l]
                elif l == 52:
                    out.append(Yahooid[l])
#                print Yahooid[l]                          
                elif l == 54:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 56:
                    out.append(Yahooid[l])  
#                print Yahooid[l]
                elif l == 58:
                    out.append(Yahooid[l])  
#                print Yahooid[l]
                elif l == 60:
                    out.append(Yahooid[l])
#                print Yahooid[l]
                elif l == 62:
                    out.append(Yahooid[l])  
#                print Yahooid[l]
                elif l == 64:
                    out.append(Yahooid[l])  
#                print Yahooid[l]
                elif l == 65:
                    out.append(Yahooid[l])
#                print Yahooid[l]
        #return tuple(Yahooid) 
#        print out
#        return tuple(out) 
            return out   
        except urllib2.HTTPError:
            print "%s not found!!"%url
    def fetchStatementDog(self,stockid):
        Yahooid = []
        out = []
        print stockid
        url = ( 'http://statementdog.com/analysis/tpe/' +
                '#%d') % stockid   
        print url             
        try:
            response = urllib2.urlopen(url)
            content = response.read()
            print content
            html = etree.HTML(content)
            table = html.xpath("/html/body/div[5]/ul/li[2]/tr[2]")
            for id  in table:
#                Yahooid.append(str(id.text).replace("元","").replace("%","").replace("每股淨值: ", ""))
                print id.text   

            for l in range(0,len(Yahooid)):
                if l == 5:      
                #�{���ѧQ
                    out.append(Yahooid[l])
            return out
        except urllib2.HTTPError:
            print "%s not found!!"%url        
        
        
