# -*- coding: utf-8 -*-
from grs import Stock as stock

import urllib
import string
import sqlite3 
import csv
import os

from operator import itemgetter, attrgetter
from FetchData import *
import sys
from StockDataBroswer import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui 
from PyQt4.QtCore import *


class Ui(QtGui.QDialog,Ui_Dialog):
    def __init__(self,PBR,PER,YieldRate,row):
        QtGui.QDialog.__init__(self )
        Ui_Dialog.__init__(self)
                
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.PBRlineEdit.setText('0')
        self.ui.PERlineEdit.setText('0')
        self.ui.YieldRatelineEdit.setText('0')

        self.connect(self.ui.FetchDatapButton, QtCore.SIGNAL("clicked()"),self.refreshStockItem)
        
        self.connect(self.ui.PBRrButton,QtCore.SIGNAL("toggled(bool)"),self.ReArrengeStockList)
        self.connect(self.ui.PERrButton,QtCore.SIGNAL("toggled(bool)"),self.ReArrengeStockList)
        self.connect(self.ui.YieldRaterButton,QtCore.SIGNAL("toggled(bool)"),self.ReArrengeStockList)
        
        self.connect(self.ui.PBRlineEdit,QtCore.SIGNAL("textChanged (const QString&)"),self.getPBR)
        self.connect(self.ui.PERlineEdit,QtCore.SIGNAL("textChanged (const QString&)"),self.getPER)
        self.connect(self.ui.YieldRatelineEdit,QtCore.SIGNAL("textChanged (const QString&)"),self.getYieldRate)
        
        self.connect(self.ui.StocktableWidget,QtCore.SIGNAL("cellClicked (int,int)"),self.check_stock_exist)
    def check_stock_exist(self):
        print self.ui.StocktableWidget.currentItem().text()
        print self.ui.StocktableWidget.currentItem().column()
        print self.ui.StocktableWidget.currentItem().row()
    def getPBR(self,str):
        PBR = str
        print str
    def getPER(self,str):
        PER = str
        print str
    def getYieldRate(self,str):
        YieldRate = str
        print str
    def ReArrengeStockList(self):
        self.ui.label.setText('reArrenge list')
        self.clear()
#        PBR = self.ui.PBRlineEdit.text()
        self.PBR = int(self.ui.PBRlineEdit.text())
        self.PER = int(self.ui.PERlineEdit.text())
        self.YieldRate = int(self.ui.YieldRatelineEdit.text())
        
        print self.PBR
        print self.PER
        print self.YieldRate
        num = 0
        for i, ll in enumerate(row):
            for j, col in enumerate(ll):
                if(num %2 == 0 & num >1 & int(col) > self.PBR):
                    item = QtGui.QTableWidgetItem(col)
                    self.ui.StocktableWidget.setItem(i, j, item)  
                elif(num %3 == 0 & num >1 & int(col) > self.PER):
#                elif(num %3 == 0 & num >1):
                    item = QtGui.QTableWidgetItem(col)
                    self.ui.StocktableWidget.setItem(i, j, item)  
                elif(num %4 == 0 & num >1 & int(col) > self.YieldRate):
                    item = QtGui.QTableWidgetItem(col)
                    self.ui.StocktableWidget.setItem(i, j, item)  
#                print col
#                print num
                num +=1
                
        
    def label_change_str(self,str):
        self.ui.label.setText(str) 
    def clear(self):
        self.ui.StocktableWidget.clear()
    def list(self):
        self.ui.lineEdit.setText('123')   
    def SetRow(self,Row):
        self.ui.StocktableWidget.setRowCount(Row)
    def TableWidgetInit(self):

        self.ui.StocktableWidget.setColumnCount(5)

        ll = QtCore.QStringList()
        ll.append(QtCore.QString('ID'))
        ll.append(QtCore.QString(u'政卷名稱'))
        ll.append(QtCore.QString(u'本益比'))
        ll.append(QtCore.QString(u'殖利率'))
        ll.append(QtCore.QString(u'股價淨值比'))        
        self.ui.StocktableWidget.setHorizontalHeaderLabels(ll )

    def AddItem (self,row):  
#        self.row = row
        for i, ll in enumerate(row):
            for j, col in enumerate(ll):
                item = QtGui.QTableWidgetItem(col)
                self.ui.StocktableWidget.setItem(i, j, item)  
    def refreshStockItem(self):
        self.clear
        new_row = sorted(row, key=lambda x:x[4])
        for i, ll in enumerate(new_row):
            for j, col in enumerate(ll):
                item = QtGui.QTableWidgetItem(col)    
                if(j == 2):     #PBRlineEdit
                    print 'PBR = '+col
                elif (j == 3):  #PERlineEdit
                    print 'PER = '+col
                elif (j == 4):  #YieldRatelineEdit
                    print '現金殖利率 = '+col
                self.ui.StocktableWidget.setItem(i, j, item)  
    def doubleclicked(self):
        print 'clicked'
        
class ButtonBlock(QtGui.QWidget):

    def __init__(self, *args):
        super(QtGui.QWidget, self).__init__()
        grid = QtGui.QGridLayout()
        names = ('One', 'Two', 'Three', 'Four', 'Five',
                 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
        for i, name in enumerate(names):
            button = QtGui.QPushButton(name, self)
            button.clicked.connect(self.make_calluser(name)) 
            row, col = divmod(i, 5)
            grid.addWidget(button, row, col)
        self.setLayout(grid)

    def make_calluser(self, name):
        def calluser():
            print(name)
        return calluser

def tuple_without(original_tuple, element_to_remove):
    new_tuple = []
    for s in list(original_tuple):
        if not s == element_to_remove:
            new_tuple.append(s)
    return tuple(new_tuple)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    stockid = StockID()
#    q3 = Sqlite3()
    row = stockid.fetchTWSEStockID()

#    for x in row[1:len(row)]:
#        print x
    
    ui = Ui(0,0,0,row)
    ui.show()
    ui.TableWidgetInit()
    
    ui.SetRow(len(row))
    ui.AddItem(row[1:len(row)])  
    
#    for l in row:        
#        print stockid.fetchYahoo(int(l[0]))  
#    tb = ButtonBlock()
#    tb.show()
    sys.exit(app.exec_())


