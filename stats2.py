# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats2.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSlider,
    QTableWidget, QTableWidgetItem, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(627, 638)
        Form.setStyleSheet(u"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 91, 20))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.listWidget = QListWidget(Form)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 91, 271))
        self.listWidget.setStyleSheet(u"/* \u7ed9QFrame\u8bbe\u7f6e\u6df1\u8272\u78e8\u7802\u80cc\u666f */\n"
"QFrame {\n"
"    /* \u6df1\u8272\u534a\u900f\u660e\u80cc\u666f\uff0c\u6a21\u62df\u78e8\u7802 */\n"
"    background-color: rgba(40, 40, 40, 50);\n"
"    /* \u5706\u89d2\u8fb9\u6846 */\n"
"    border-radius: 10px;\n"
"    /* \u8f7b\u5fae\u8fb9\u6846\u589e\u5f3a\u8d28\u611f */\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 91, 271))
        self.frame.setStyleSheet(u"/* \u7ed9QFrame\u8bbe\u7f6e\u6df1\u8272\u78e8\u7802\u80cc\u666f */\n"
"QFrame {\n"
"    /* \u6df1\u8272\u534a\u900f\u660e\u80cc\u666f\uff0c\u6a21\u62df\u78e8\u7802 */\n"
"    background-color: rgba(40, 40, 40, 50);\n"
"    /* \u5706\u89d2\u8fb9\u6846 */\n"
"    border-radius: 10px;\n"
"    /* \u8f7b\u5fae\u8fb9\u6846\u589e\u5f3a\u8d28\u611f */\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 30, 131, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(380, 30, 83, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(85, 255, 255, 50);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 30, 83, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgba(85, 255, 255, 50);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1)
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(110, 60, 351, 31))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(110, 90, 351, 171))
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(110, 260, 351, 41))
        self.plainTextEdit.setStyleSheet(u"/* \u7ed9QFrame\u8bbe\u7f6e\u6df1\u8272\u78e8\u7802\u80cc\u666f */\n"
"QFrame {\n"
"    /* \u6df1\u8272\u534a\u900f\u660e\u80cc\u666f\uff0c\u6a21\u62df\u78e8\u7802 */\n"
"    background-color: rgb(255, 255, 255)\n"
"    /* \u5706\u89d2\u8fb9\u6846 */\n"
"    border-radius: 10px;\n"
"    /* \u8f7b\u5fae\u8fb9\u6846\u589e\u5f3a\u8d28\u611f */\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(110, 303, 88, 31))
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(190, 310, 191, 16))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 300, 81, 41))
        self.pushButton.setStyleSheet(u"background-color: rgba(85, 255, 255, 50);\n"
"color: rgb(0, 0, 0);")
        self.frame.raise_()
        self.label_2.raise_()
        self.listWidget.raise_()
        self.comboBox.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.tableWidget.raise_()
        self.textBrowser.raise_()
        self.plainTextEdit.raise_()
        self.checkBox.raise_()
        self.horizontalSlider.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"AI\u667a\u80fd\u52a9\u624b", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"AI\u5bf9\u8bdd", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"AI\u7ed8\u753b", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u7ffb\u8bd1", None))
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"\u5386\u53f2\u8bb0\u5f55", None))
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u901a\u7528\u5927\u6a21\u578b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u4ee3\u7801\u5927\u6a21\u578b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u6587\u751f\u56fe\u5927\u6a21\u578b", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u6a21\u578b", None))

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u667a\u80fd\u5bf9\u8bdd", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"AI\u7ed8\u56fe", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e\u5207\u6362", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u6d41\u5f0f\u8f93\u51fa", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u751f\u6210", None))
    # retranslateUi

