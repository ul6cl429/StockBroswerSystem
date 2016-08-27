# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockDataBroswer.ui'
#
# Created: Sun Jul 27 14:11:03 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(470, 440, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.StocktableWidget = QtGui.QTableWidget(Dialog)
        self.StocktableWidget.setGeometry(QtCore.QRect(20, 40, 521, 261))
        self.StocktableWidget.setObjectName(_fromUtf8("StocktableWidget"))
        item = QtGui.QTableWidgetItem()
        self.StocktableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.StocktableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.StocktableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.StocktableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.StocktableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 380, 198, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PBRrButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.PBRrButton.setObjectName(_fromUtf8("PBRrButton"))
        self.gridLayout.addWidget(self.PBRrButton, 2, 0, 1, 1)
        self.YieldRaterButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.YieldRaterButton.setObjectName(_fromUtf8("YieldRaterButton"))
        self.gridLayout.addWidget(self.YieldRaterButton, 1, 0, 1, 1)
        self.YieldRatelineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.YieldRatelineEdit.setObjectName(_fromUtf8("YieldRatelineEdit"))
        self.gridLayout.addWidget(self.YieldRatelineEdit, 1, 1, 1, 1)
        self.PBRlineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.PBRlineEdit.setObjectName(_fromUtf8("PBRlineEdit"))
        self.gridLayout.addWidget(self.PBRlineEdit, 2, 1, 1, 1)
        self.PERrButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.PERrButton.setObjectName(_fromUtf8("PERrButton"))
        self.gridLayout.addWidget(self.PERrButton, 0, 0, 1, 1)
        self.PERlineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.PERlineEdit.setObjectName(_fromUtf8("PERlineEdit"))
        self.gridLayout.addWidget(self.PERlineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 380, 160, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.SearchHLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.SearchHLayout.setMargin(0)
        self.SearchHLayout.setObjectName(_fromUtf8("SearchHLayout"))
        self.StocklineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.StocklineEdit.setObjectName(_fromUtf8("StocklineEdit"))
        self.SearchHLayout.addWidget(self.StocklineEdit)
        self.SearchStockpButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.SearchStockpButton.setObjectName(_fromUtf8("SearchStockpButton"))
        self.SearchHLayout.addWidget(self.SearchStockpButton)
        self.FetchDatapButton = QtGui.QPushButton(Dialog)
        self.FetchDatapButton.setGeometry(QtCore.QRect(20, 320, 111, 23))
        self.FetchDatapButton.setObjectName(_fromUtf8("FetchDatapButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.StocktableWidget.horizontalHeaderItem(0)
#        item.setText(_translate("Dialog", "ID", None))
        item = self.StocktableWidget.horizontalHeaderItem(1)
#        item.setText(_translate("Dialog", "証卷名稱", None))
        item = self.StocktableWidget.horizontalHeaderItem(2)
#        item.setText(_translate("Dialog", "本益比", None))
        item = self.StocktableWidget.horizontalHeaderItem(3)
#        item.setText(_translate("Dialog", "殖利率", None))
        item = self.StocktableWidget.horizontalHeaderItem(4)
#        item.setText(_translate("Dialog", "股價淨值比", None))
        self.PBRrButton.setText(_translate("Dialog", "股價淨值比 >=", None))
        self.YieldRaterButton.setText(_translate("Dialog", "殖利率 >=", None))
        self.PERrButton.setText(_translate("Dialog", "本益比 >=", None))
        self.label.setText(_translate("Dialog", "%", None))
        self.label_2.setText(_translate("Dialog", "%", None))
        self.label_3.setText(_translate("Dialog", "%", None))
        self.SearchStockpButton.setText(_translate("Dialog", "Search ", None))
        self.FetchDatapButton.setText(_translate("Dialog", "Fetch sotck data", None))

