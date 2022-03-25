# -*- coding: utf-8 -*-

import traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import easygui as eg 
from requests import post
from base64 import b64encode
from json import dumps
from threading import Thread
from datetime import datetime
from os import mkdir
import os.path

def logYaz(mesaj):
    now = datetime.now()
    tarih = now.strftime("%d-%m-%Y")
    saat  = now.strftime("%H:%M")
    try:
        mkdir("log")
    except:
        pass
    file = open(f"log/{tarih}_LOG.txt","a+")
    file.write(f"[{saat}]{mesaj}\n")
    file.close()

def controlCreate(file,icerik=""):
    if not os.path.isfile(file):
        file = open(file,"w+",encoding="utf-8")
        file.write(icerik)
        file.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('./fav.ico'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(312, 400))
        MainWindow.setMaximumSize(QtCore.QSize(680, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"    color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: 000000;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.chkMedya = QtWidgets.QCheckBox(self.tab)
        self.chkMedya.setGeometry(QtCore.QRect(10, 300, 331, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chkMedya.setFont(font)
        self.chkMedya.setStyleSheet("background-color:#DDD;")
        self.chkMedya.setObjectName("chkMedya")
        self.btnGonder = QtWidgets.QPushButton(self.tab)
        self.btnGonder.setGeometry(QtCore.QRect(10, 330, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnGonder.setFont(font)
        self.btnGonder.setStyleSheet("border:1px solid;")
        self.btnGonder.setObjectName("btnGonder")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(350, 67, 321, 251))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.txtNumaralar = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.txtNumaralar.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNumaralar.setFont(font)
        self.txtNumaralar.setObjectName("txtNumaralar")
        self.verticalLayout_6.addWidget(self.txtNumaralar)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 331, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txtMesaj = QtWidgets.QTextEdit(self.widget)
        self.txtMesaj.setObjectName("txtMesaj")
        self.verticalLayout.addWidget(self.txtMesaj)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(350, 10, 321, 52))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.cmbTip = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cmbTip.setFont(font)
        self.cmbTip.setObjectName("cmbTip")
        self.cmbTip.addItem("")
        self.cmbTip.addItem("")
        self.verticalLayout_3.addWidget(self.cmbTip)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 260, 661, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget2 = QtWidgets.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 641, 93))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.txtDosyaAd = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDosyaAd.setFont(font)
        self.txtDosyaAd.setText("")
        self.txtDosyaAd.setObjectName("txtDosyaAd")
        self.horizontalLayout_3.addWidget(self.txtDosyaAd)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.widget2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtKonum = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtKonum.setFont(font)
        self.txtKonum.setText("")
        self.txtKonum.setObjectName("txtKonum")
        self.horizontalLayout_4.addWidget(self.txtKonum)
        self.btnSec = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnSec.setFont(font)
        self.btnSec.setStyleSheet("border:1px solid;")
        self.btnSec.setObjectName("btnSec")
        self.horizontalLayout_4.addWidget(self.btnSec)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.widget3 = QtWidgets.QWidget(self.tab_4)
        self.widget3.setGeometry(QtCore.QRect(10, 210, 661, 41))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMedyaEkle = QtWidgets.QPushButton(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnMedyaEkle.setFont(font)
        self.btnMedyaEkle.setStyleSheet("border:1px solid;")
        self.btnMedyaEkle.setObjectName("btnMedyaEkle")
        self.horizontalLayout_2.addWidget(self.btnMedyaEkle)
        self.btnMedyaSil = QtWidgets.QPushButton(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnMedyaSil.setFont(font)
        self.btnMedyaSil.setStyleSheet("border:1px solid;")
        self.btnMedyaSil.setObjectName("btnMedyaSil")
        self.horizontalLayout_2.addWidget(self.btnMedyaSil)
        self.widget4 = QtWidgets.QWidget(self.tab_4)
        self.widget4.setGeometry(QtCore.QRect(10, 0, 661, 201))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.listMedya = QtWidgets.QListWidget(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.listMedya.setFont(font)
        self.listMedya.setObjectName("listMedya")
        self.verticalLayout_7.addWidget(self.listMedya)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tblKisiler = QtWidgets.QTableWidget(self.tab_3)
        self.tblKisiler.setGeometry(QtCore.QRect(10, 40, 661, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tblKisiler.setFont(font)
        self.tblKisiler.setStyleSheet("border:1px solid;")
        self.tblKisiler.setWordWrap(True)
        self.tblKisiler.setRowCount(0)
        self.tblKisiler.setObjectName("tblKisiler")
        self.tblKisiler.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tblKisiler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblKisiler.setHorizontalHeaderItem(1, item)
        self.tblKisiler.horizontalHeader().setCascadingSectionResizes(False)
        self.tblKisiler.horizontalHeader().setDefaultSectionSize(130)
        self.tblKisiler.horizontalHeader().setMinimumSectionSize(70)
        self.tblKisiler.horizontalHeader().setSortIndicatorShown(False)
        self.tblKisiler.horizontalHeader().setStretchLastSection(True)
        self.tblKisiler.verticalHeader().setVisible(False)
        self.tblKisiler.verticalHeader().setCascadingSectionResizes(False)
        self.tblKisiler.verticalHeader().setDefaultSectionSize(25)
        self.tblKisiler.verticalHeader().setMinimumSectionSize(25)
        self.tblKisiler.verticalHeader().setStretchLastSection(False)
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 661, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnKisiEkle = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnKisiEkle.setFont(font)
        self.btnKisiEkle.setStyleSheet("border:1px solid;")
        self.btnKisiEkle.setObjectName("btnKisiEkle")
        self.horizontalLayout.addWidget(self.btnKisiEkle)
        self.btnKisiSil = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnKisiSil.setFont(font)
        self.btnKisiSil.setStyleSheet("border:1px solid;")
        self.btnKisiSil.setObjectName("btnKisiSil")
        self.horizontalLayout.addWidget(self.btnKisiSil)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 661, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtToken = QtWidgets.QLineEdit(self.tab_2)
        self.txtToken.setGeometry(QtCore.QRect(10, 30, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtToken.setFont(font)
        self.txtToken.setText("")
        self.txtToken.setObjectName("txtToken")
        self.btnTokenKaydet = QtWidgets.QPushButton(self.tab_2)
        self.btnTokenKaydet.setGeometry(QtCore.QRect(10, 70, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnTokenKaydet.setFont(font)
        self.btnTokenKaydet.setStyleSheet("border:1px solid;")
        self.btnTokenKaydet.setObjectName("btnTokenKaydet")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 661, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#DDD;padding:4px;")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.mime_types = {
            'video': [
                'mp4',
                '3gp'
            ],
            'document': [
                'doc',
                'docx',
                'xls',
                'xlsx',
                'ppt',
                'pptx',
                'mdb',
                'mdbx',
                'pdf',
                'odt',
                'txt',
                'ott',
                'rtf',
                'htm',
                'html',
                'php',
                'rar',
                'zip',
                '7z',
                'gz'
            ],
            'picture':[
                'jpeg',
                'jpg',
                'bmp',
                'gif',
                'png',
                'tiff'
            ]
        }

        try:
            mkdir("ayarlar")
        except:
            pass

        controlCreate("./ayarlar/api.db","http://api.mhatsapp.com/api/v3/message/send/")
        controlCreate("./ayarlar/mesaj.db","TEST MESAJI\n*KALIN MESAJ*\n\n_İTALİK MESAJ_\n\nTEST BİTTİ")
        controlCreate("./ayarlar/kisiler.db")
        controlCreate("./ayarlar/medya.db")
        controlCreate("./ayarlar/token.db","\n")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        try:
            self.kisiler = []
            self.metin   = []
            self.medya   = []
            self.mesaj   = ""
            self.token   = ""
            self.apiurl  = ""
            self.gonderimTipi=False

            self.getMedyalar()
            self.getToken()
            self.getKisiler()
            self.getAPI()
            self.getMesaj()

            self.btnSec.clicked.connect(self.openFile)
            self.btnMedyaEkle.clicked.connect(self.medyaEkle)
            self.btnMedyaSil.clicked.connect(self.medyaSil)
            self.btnTokenKaydet.clicked.connect(self.setToken)
            self.btnKisiEkle.clicked.connect(self.ekleKisiler)
            self.btnKisiSil.clicked.connect(self.silKisi)
            self.btnGonder.clicked.connect(self.mesajGonderimBaslat)
            self.txtMesaj.textChanged.connect(self.setMesaj)
            self.cmbTip.currentIndexChanged.connect(self.gonderimTip)

            self.mesajThread = QTimer() 
            self.mesajThread.timeout.connect(self.mesajlariGonder)
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def gonderimTip(self):
        try:
            self.gonderimTipi=not self.gonderimTipi
            self.txtNumaralar.setEnabled(self.gonderimTipi)
            if self.gonderimTipi==False:
                self.txtNumaralar.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Telefon numaralarını,</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">her satıra bir telefon gelecek şekilde yazmalısınız.</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Örnek;</p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+90-555-444-33-22</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0545-123-45-67</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">90547-987-65-43</p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
            else:
                self.txtNumaralar.setText("")
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def mesajGonderimBaslat(self):
        try:
            mesajThreading = Thread(target=self.mesajlariGonder)
            mesajThreading.start()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def mesajlariGonder(self):
        try:
            self.btnGonder.setEnabled(False)
            mesajGidecekler=[]
            if self.gonderimTipi:
                for kisi in self.txtNumaralar.toPlainText().split("\n"):
                    mesajGidecekler.append({'adsoyad':'','telefon':kisi.strip().rstrip()})
            else:
                mesajGidecekler=self.kisiler
            
            for kisi in mesajGidecekler:
                if self.chkMedya.isChecked():
                    for medya in self.medya:
                        extension = medya['yol'].split(".")[-1]
                        file_type = ""
                        for type, type_list in self.mime_types.items():
                                if extension in type_list:
                                    file_type = type
                        try:
                            file = open(medya['yol'],"rb")
                            encoded_string= b64encode(file.read())
                        except:
                            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
                            logYaz(traceback.format_exc())
                        try:
                            data = {'action':{'token':[self.token],'numbers':kisi['telefon'],
                                'type':file_type,
                                'filename':medya['ad'],
                                'message':medya['ad'],
                                'file':encoded_string.decode()}}
                            req = post('http://api.mhatsapp.com/api/v3/message/send/', headers={'Content-Type': 'application/json'}, data=dumps(data))  
                        except:
                            logYaz(traceback.format_exc())
                try:
                    data = {'action':{'token':[self.token],'numbers':kisi['telefon'],
                            'type':'text',
                            'message':self.txtMesaj.toPlainText().replace("{{adsoyad}}",kisi['adsoyad'])}}
                    req = post('http://api.mhatsapp.com/api/v3/message/send/', headers={'Content-Type': 'application/json'}, data=dumps(data))
                except:
                    logYaz(traceback.format_exc())
            self.btnGonder.setEnabled(True)
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def getAPI(self):
        try:
            file = open("./ayarlar/api.db","r+")
            self.apiurl = file.read(100)
            file.close()
            self.apiurl = self.apiurl.rstrip().strip()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def getKisiler(self):
        try:
            file = open("./ayarlar/kisiler.db","r+")
            lines = file.readlines()
            file.close()
            kisiler = []
            for line in lines:
                kisiler.append({"adsoyad":line[:-1].split("<:>")[0],"telefon":line[:-1].split("<:>")[1]})
            self.kisiler=kisiler

            self.tblKisiler.clear()
            self.tblKisiler.setRowCount(0)
            for kisi in self.kisiler:
                self.tblKisiler.insertRow(self.kisiler.index(kisi))
                for i in range(0,2):
                    self.tblKisiler.setItem(self.kisiler.index(kisi), i, QtWidgets.QTableWidgetItem(kisi['adsoyad'] if i==0 else kisi['telefon']))
            self.tblKisiler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tblKisiler.setHorizontalHeaderLabels(['Ad Soyad','Telefon'])
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def ekleKisiler(self):
        try:
            kisi = {'adsoyad':'','telefon':''}
            adsoyad, okPressed = QInputDialog.getText(MainWindow,"Kişi Ekle","Ad soyad:")
            if okPressed and adsoyad != '':
                kisi['adsoyad']=adsoyad
            else:
                self.msgBoxWarning("HATA","İşlem iptal edildi.")
                return
            
            telefon, okPressed = QInputDialog.getText(MainWindow,"Kişi Ekle","Telefon:")
            if okPressed and telefon != '':
                kisi['telefon']=telefon
            else:
                self.msgBoxWarning("HATA","İşlem iptal edildi.")
                return
            
            self.kisiler.append(kisi)

            file = open("./ayarlar/kisiler.db","w+")
            kisiler = ""
            for kisi in self.kisiler:
                kisiler = kisiler+kisi['adsoyad']+"<:>"+kisi['telefon']+"\n"
            file.write(kisiler)
            file.close()
            self.getKisiler()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def silKisi(self):
        try:
            itemRow = int(self.tblKisiler.currentRow())
            del self.kisiler[itemRow]
            self.tblKisiler.removeRow(itemRow)
            file = open("./ayarlar/kisiler.db","w+")
            kisiler = ""
            for kisi in self.kisiler:
                kisiler = kisiler+kisi['adsoyad']+"<:>"+kisi['telefon']+"\n"
            file.write(kisiler)
            file.close()
        except:
            logYaz(traceback.format_exc())
            self.msgBoxWarning("Hata","Kişi seçmeden silme işlemi yapamazsınız.")
   
    def getMedyalar(self):
        try:
            file = open("./ayarlar/medya.db","r+")
            lines = file.readlines()
            file.close()
            medya = []
            for line in lines:
                medya.append({"ad":line[:-1].split("<:>")[0],"yol":line[:-1].split("<:>")[1]})
            self.medya=medya
            for medya in self.medya:
                self.listMedya.addItem(medya["ad"])
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def getMesaj(self):
        try:
            file = open("./ayarlar/mesaj.db","r+", encoding="utf8")
            self.mesaj = file.read()
            file.close()
            self.txtMesaj.setPlainText(self.mesaj)
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def setMesaj(self):
        try:
            file = open("./ayarlar/mesaj.db","w", encoding="utf8")
            file.write(self.txtMesaj.toPlainText())
            file.close()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def getToken(self):
        try:
            file = open("./ayarlar/token.db","r+")
            self.token = file.readlines()[0].split("\n")[0]
            file.close()
            self.txtToken.setText(self.token)
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def setToken(self):
        try:
            file = open("./ayarlar/token.db","w")
            file.write(self.txtToken.text()+"\n")
            file.close()
            self.msgBoxInfo("Başarılı","Telefon token'ı başarıyla kaydedildi.")
            self.getToken()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())

    def openFile(self):
        selectedFile = eg.fileopenbox(msg='Göndermek istediğiniz dosyayı seçin',
                    title='Göndermek istediğiniz dosyayı seçin')

        try:
            extension = selectedFile.split(".")[-1]
            file_type = ""

            for type, type_list in self.mime_types.items():
                    if extension in type_list:
                        file_type = type

            if file_type=="":
                self.msgBoxWarning("Hata","Göndermek istediğiniz dosya tipi geçersiz.")
                return
            
            self.txtDosyaAd.setText(str(selectedFile.split("\\")[-1]))
            self.txtKonum.setText(str(selectedFile))
            self.txtKonum.setCursorPosition(0)
        except:
            pass
    
    def medyaEkle(self):
        if self.txtDosyaAd.text()=="":
            self.msgBoxWarning("Hata","Dosya adı boş bırakılamaz.")
            return
        
        if self.txtKonum.text()=="":
            self.msgBoxWarning("Hata","Dosya konumu boş bırakılamaz.")
            return

        self.listMedya.addItem(self.txtDosyaAd.text())
        self.medya.append({'ad':self.txtDosyaAd.text(),'yol':self.txtKonum.text()})
        self.txtDosyaAd.setText("")
        self.txtKonum.setText("")
        try:
            file = open("./ayarlar/medya.db","w+")
            medyalar = ""
            for medya in self.medya:
                medyalar = medyalar+medya['ad']+"<:>"+medya['yol']+"\n"
            file.write(medyalar)
            file.close()
        except:
            self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
            logYaz(traceback.format_exc())
    
    def medyaSil(self):
        try:
            itemRow = int(self.listMedya.currentRow())
            del self.medya[itemRow]
            for item in self.listMedya.selectedItems():
                self.listMedya.takeItem(self.listMedya.row(item))

            try:
                file = open("./ayarlar/medya.db","w+")
                medyalar = ""
                for medya in self.medya:
                    medyalar = medyalar+medya['ad']+"<:>"+medya['yol']+"\n"
                file.write(medyalar)
                file.close()
            except:
                self.msgBoxWarning("Hata",f"Bir hata oluştu.\n{traceback.format_exc()}")
                logYaz(traceback.format_exc())
        except:
            self.msgBoxWarning("Hata","Medya seçmeden silme işlemi yapamazsınız.")

    def msgBoxWarning(self,title,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def msgBoxInfo(self,title,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Toplu Mesaj"))
        self.chkMedya.setText(_translate("MainWindow", "Medya Gönderilsin"))
        self.btnGonder.setText(_translate("MainWindow", "GÖNDER"))
        self.label_7.setText(_translate("MainWindow", "Telefon numaraları"))
        self.txtNumaralar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Telefon numaralarını,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">her satıra bir telefon gelecek şekilde yazmalısınız.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Örnek;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+90-555-444-33-22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0545-123-45-67</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">90547-987-65-43</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Mesajınız"))
        self.label_8.setText(_translate("MainWindow", "Gönderim Tipi"))
        self.cmbTip.setItemText(0, _translate("MainWindow", "Kişilere toplu gönderim"))
        self.cmbTip.setItemText(1, _translate("MainWindow", "Aşağıya girilecek telefon numaralarına"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Metin"))
        self.groupBox.setTitle(_translate("MainWindow", "Medya Detay"))
        self.label_5.setText(_translate("MainWindow", "Dosya adı"))
        self.label_3.setText(_translate("MainWindow", "Dosya Konumu"))
        self.btnSec.setText(_translate("MainWindow", "..."))
        self.btnMedyaEkle.setText(_translate("MainWindow", "Ekle"))
        self.btnMedyaSil.setText(_translate("MainWindow", "Sil"))
        self.label_2.setText(_translate("MainWindow", "Gönderilecek Medyalar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Medya"))
        item = self.tblKisiler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad Soyad"))
        item = self.tblKisiler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Telefon"))
        self.btnKisiEkle.setText(_translate("MainWindow", "Ekle"))
        self.btnKisiSil.setText(_translate("MainWindow", "Sil"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Kişiler"))
        self.label.setText(_translate("MainWindow", "TELEFON TOKEN"))
        self.btnTokenKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\"><br/>-&gt; Metin :</span> Bu bölümden göndermek istediğiniz metin mesajının içeriğini yazabilirsiniz.<br/>Mesaj içeriğine <span style=\" font-weight:600;\">{{adsoyad}}</span> eklerseniz, kişiye mesaj adı ile gönderilecektir.</p><p>Yine bu bölümden &quot;Mesaj gönderim&quot; tipini değiştirerek ister &quot;Kişiler&quot; bölümüne eklediğiniz kişilere isterseniz &quot;Telefon numaraları&quot; bölümüne yazdığınız kişilere mesaj gönderebilirsiniz.</p><p>O kısımda her satıra bir telefon gelecek şekilde telefonları yazabilirsiniz.</p><p><span style=\" font-weight:600;\">-&gt; Medya :</span> Mesaj içeriğinde göndermek istediğiniz dosyaları ekleyebilirsiniz.<br/>Eğer dosya geçerli ise bu bölüme eklenecek ve daha sonra gönderim için kayıt edilecektir.</p><p><span style=\" font-weight:600;\">-&gt; Kişiler : </span>Mesajı göndermek istediğiniz kişileri buraya ekleyebilirsiniz. Her işlem sırasında kayıt edilecektir.</p><p><span style=\" font-weight:600;\">-&gt; Ayarlar : </span>Bu bölümden websitemizden aldığınız aktif haldeki telefonun tokenını yazıp kaydedebilirsiniz.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ayarlar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())