# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ipcv111.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog,QMessageBox)

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import glob
from IPython.display import Image
import sys
# import external file vam11

import os


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(893, 605)
        self.ToolBoxIP = QtWidgets.QToolBox(Dialog)
        self.ToolBoxIP.setGeometry(QtCore.QRect(20, 40, 871, 551))
        self.ToolBoxIP.setObjectName("ToolBoxIP")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 871, 435))
        self.page.setObjectName("page")
        self.ImageTab = QtWidgets.QTabWidget(self.page)
        self.ImageTab.setGeometry(QtCore.QRect(20, 250, 821, 161))
        self.ImageTab.setStyleSheet("background-color: rgb(235, 255, 222);")
        self.ImageTab.setObjectName("ImageTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 20, 651, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.GrayButton = QtWidgets.QPushButton(self.groupBox_2)
        self.GrayButton.setGeometry(QtCore.QRect(80, 40, 89, 25))
        self.GrayButton.setObjectName("GrayButton")
        self.HSVButton = QtWidgets.QPushButton(self.groupBox_2)
        self.HSVButton.setGeometry(QtCore.QRect(270, 40, 89, 25))
        self.HSVButton.setObjectName("HSVButton")
        self.YUVButton = QtWidgets.QPushButton(self.groupBox_2)
        self.YUVButton.setGeometry(QtCore.QRect(460, 40, 89, 25))
        self.YUVButton.setObjectName("YUVButton")
        self.ImageTab.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 10, 561, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.HistEquiButton = QtWidgets.QPushButton(self.groupBox_4)
        self.HistEquiButton.setGeometry(QtCore.QRect(300, 50, 201, 25))
        self.HistEquiButton.setObjectName("HistEquiButton")
        self.HistogramButton = QtWidgets.QPushButton(self.groupBox_4)
        self.HistogramButton.setGeometry(QtCore.QRect(40, 50, 201, 25))
        self.HistogramButton.setObjectName("HistogramButton")
        self.ImageTab.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(80, 10, 561, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.LaplacianButton = QtWidgets.QPushButton(self.groupBox_5)
        self.LaplacianButton.setGeometry(QtCore.QRect(310, 50, 201, 25))
        self.LaplacianButton.setObjectName("LaplacianButton")
        self.SobelButton = QtWidgets.QPushButton(self.groupBox_5)
        self.SobelButton.setGeometry(QtCore.QRect(40, 50, 201, 25))
        self.SobelButton.setObjectName("SobelButton")
        self.ImageTab.addTab(self.tab_3, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_6.setGeometry(QtCore.QRect(80, 10, 561, 111))
        self.groupBox_6.setObjectName("groupBox_6")
        self.ClosingButton = QtWidgets.QPushButton(self.groupBox_6)
        self.ClosingButton.setGeometry(QtCore.QRect(350, 80, 80, 23))
        self.ClosingButton.setObjectName("ClosingButton")
        self.ErodeButton = QtWidgets.QPushButton(self.groupBox_6)
        self.ErodeButton.setGeometry(QtCore.QRect(100, 80, 80, 23))
        self.ErodeButton.setObjectName("ErodeButton")
        self.OpeningBotton = QtWidgets.QPushButton(self.groupBox_6)
        self.OpeningBotton.setGeometry(QtCore.QRect(350, 30, 80, 23))
        self.OpeningBotton.setObjectName("OpeningBotton")
        self.DilateButton = QtWidgets.QPushButton(self.groupBox_6)
        self.DilateButton.setGeometry(QtCore.QRect(100, 30, 80, 23))
        self.DilateButton.setObjectName("DilateButton")
        self.ImageTab.addTab(self.tab_8, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(110, 10, 551, 101))
        self.groupBox_7.setObjectName("groupBox_7")
        self.BBButton = QtWidgets.QPushButton(self.groupBox_7)
        self.BBButton.setGeometry(QtCore.QRect(90, 50, 151, 25))
        self.BBButton.setObjectName("BBButton")
        self.MECButton = QtWidgets.QPushButton(self.groupBox_7)
        self.MECButton.setGeometry(QtCore.QRect(340, 50, 161, 25))
        self.MECButton.setObjectName("MECButton")
        self.ImageTab.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 10, 641, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.HLButton = QtWidgets.QPushButton(self.groupBox_3)
        self.HLButton.setGeometry(QtCore.QRect(80, 50, 141, 25))
        self.HLButton.setObjectName("HLButton")
        self.HCButton = QtWidgets.QPushButton(self.groupBox_3)
        self.HCButton.setGeometry(QtCore.QRect(390, 50, 131, 25))
        self.HCButton.setObjectName("HCButton")
        self.ImageTab.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_8.setGeometry(QtCore.QRect(40, 0, 651, 111))
        self.groupBox_8.setObjectName("groupBox_8")
        self.SIFTButton = QtWidgets.QPushButton(self.groupBox_8)
        self.SIFTButton.setGeometry(QtCore.QRect(170, 30, 89, 25))
        self.SIFTButton.setObjectName("SIFTButton")
        self.SURFButton = QtWidgets.QPushButton(self.groupBox_8)
        self.SURFButton.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.SURFButton.setObjectName("SURFButton")
        self.FASTButton = QtWidgets.QPushButton(self.groupBox_8)
        self.FASTButton.setGeometry(QtCore.QRect(10, 30, 89, 25))
        self.FASTButton.setObjectName("FASTButton")
        self.HomoFButton = QtWidgets.QPushButton(self.groupBox_8)
        self.HomoFButton.setGeometry(QtCore.QRect(240, 70, 191, 25))
        self.HomoFButton.setObjectName("HomoFButton")
        self.ISButton = QtWidgets.QPushButton(self.groupBox_8)
        self.ISButton.setGeometry(QtCore.QRect(410, 30, 191, 23))
        self.ISButton.setObjectName("ISButton")
        self.FMButton = QtWidgets.QPushButton(self.groupBox_8)
        self.FMButton.setGeometry(QtCore.QRect(500, 70, 131, 23))
        self.FMButton.setObjectName("FMButton")
        self.ImageTab.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 711, 111))
        self.groupBox_9.setObjectName("groupBox_9")
        self.EHCBotton = QtWidgets.QPushButton(self.groupBox_9)
        self.EHCBotton.setGeometry(QtCore.QRect(440, 30, 231, 25))
        self.EHCBotton.setObjectName("EHCBotton")
        self.CCOButton = QtWidgets.QPushButton(self.groupBox_9)
        self.CCOButton.setGeometry(QtCore.QRect(420, 70, 261, 25))
        self.CCOButton.setObjectName("CCOButton")
        self.EDCButton = QtWidgets.QPushButton(self.groupBox_9)
        self.EDCButton.setGeometry(QtCore.QRect(30, 70, 231, 25))
        self.EDCButton.setObjectName("EDCButton")
        self.BlurButton = QtWidgets.QPushButton(self.groupBox_9)
        self.BlurButton.setGeometry(QtCore.QRect(300, 30, 91, 23))
        self.BlurButton.setObjectName("BlurButton")
        self.LogoButton = QtWidgets.QPushButton(self.groupBox_9)
        self.LogoButton.setGeometry(QtCore.QRect(300, 70, 91, 23))
        self.LogoButton.setObjectName("LogoButton")
        self.SPButton = QtWidgets.QPushButton(self.groupBox_9)
        self.SPButton.setGeometry(QtCore.QRect(30, 30, 231, 23))
        self.SPButton.setObjectName("SPButton")
        self.ImageTab.addTab(self.tab_7, "")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(0, 40, 141, 181))
        self.groupBox.setStyleSheet("background-color: rgb(255, 252, 208);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(237, 235, 130, 230), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox.setObjectName("groupBox")
        self.LoadButton = QtWidgets.QPushButton(self.groupBox)
        self.LoadButton.setGeometry(QtCore.QRect(20, 80, 89, 25))
        self.LoadButton.setObjectName("LoadButton")
        self.groupBox_10 = QtWidgets.QGroupBox(self.page)
        self.groupBox_10.setGeometry(QtCore.QRect(160, 0, 601, 241))
        self.groupBox_10.setObjectName("groupBox_10")
        self.OutputLabel = QtWidgets.QLabel(self.groupBox_10)
        self.OutputLabel.setGeometry(QtCore.QRect(340, 30, 251, 191))
        self.OutputLabel.setObjectName("OutputLabel")
        self.Inputlabel = QtWidgets.QLabel(self.groupBox_10)
        self.Inputlabel.setGeometry(QtCore.QRect(40, 30, 251, 191))
        self.Inputlabel.setObjectName("Inputlabel")
        self.groupBox_10.raise_()
        self.ImageTab.raise_()
        self.groupBox.raise_()
        self.ToolBoxIP.addItem(self.page, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 871, 425))
        self.page_4.setObjectName("page_4")
        self.Textlabel_2 = QtWidgets.QLabel(self.page_4)
        self.Textlabel_2.setGeometry(QtCore.QRect(30, 0, 831, 20))
        self.Textlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Textlabel_2.setObjectName("Textlabel_2")
        self.groupBox_12 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_12.setGeometry(QtCore.QRect(0, 60, 171, 181))
        self.groupBox_12.setStyleSheet("background-color: rgb(255, 252, 208);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(237, 235, 130, 230), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_12.setObjectName("groupBox_12")
        self.LoadCButton = QtWidgets.QPushButton(self.groupBox_12)
        self.LoadCButton.setGeometry(QtCore.QRect(40, 80, 89, 25))
        self.LoadCButton.setObjectName("LoadCButton")
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_13.setGeometry(QtCore.QRect(180, 20, 601, 241))
        self.groupBox_13.setObjectName("groupBox_13")
        self.Inputlabel_2 = QtWidgets.QLabel(self.groupBox_13)
        self.Inputlabel_2.setGeometry(QtCore.QRect(30, 30, 251, 191))
        self.Inputlabel_2.setObjectName("Inputlabel_2")
        self.OutputLabel_2 = QtWidgets.QLabel(self.groupBox_13)
        self.OutputLabel_2.setGeometry(QtCore.QRect(330, 30, 251, 191))
        self.OutputLabel_2.setObjectName("OutputLabel_2")
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_14.setGeometry(QtCore.QRect(140, 280, 291, 131))
        self.groupBox_14.setStyleSheet("background-color: rgb(238, 241, 255);\n"
"")
        self.groupBox_14.setObjectName("groupBox_14")
        self.CapIButton = QtWidgets.QPushButton(self.groupBox_14)
        self.CapIButton.setGeometry(QtCore.QRect(50, 60, 201, 23))
        self.CapIButton.setObjectName("CapIButton")
        self.groupBox_15 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_15.setGeometry(QtCore.QRect(470, 280, 291, 121))
        self.groupBox_15.setStyleSheet("background-color: rgb(238, 241, 255);\n"
"")
        self.groupBox_15.setObjectName("groupBox_15")
        self.CapVButton = QtWidgets.QPushButton(self.groupBox_15)
        self.CapVButton.setGeometry(QtCore.QRect(50, 60, 201, 23))
        self.CapVButton.setObjectName("CapVButton")
        self.ToolBoxIP.addItem(self.page_4, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 871, 425))
        self.page_2.setObjectName("page_2")
        self.groupBox_16 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_16.setGeometry(QtCore.QRect(20, 40, 151, 181))
        self.groupBox_16.setStyleSheet("background-color: rgb(255, 252, 208);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(237, 235, 130, 230), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox_16.setObjectName("groupBox_16")
        self.LoadButton_2 = QtWidgets.QPushButton(self.groupBox_16)
        self.LoadButton_2.setGeometry(QtCore.QRect(20, 80, 89, 25))
        self.LoadButton_2.setObjectName("LoadButton_2")
        self.groupBox_17 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_17.setGeometry(QtCore.QRect(190, 0, 601, 241))
        self.groupBox_17.setObjectName("groupBox_17")
        self.OutputLabel_3 = QtWidgets.QLabel(self.groupBox_17)
        self.OutputLabel_3.setGeometry(QtCore.QRect(340, 30, 251, 191))
        self.OutputLabel_3.setObjectName("OutputLabel_3")
        self.Inputlabel_3 = QtWidgets.QLabel(self.groupBox_17)
        self.Inputlabel_3.setGeometry(QtCore.QRect(40, 30, 251, 191))
        self.Inputlabel_3.setObjectName("Inputlabel_3")
        self.CCTab = QtWidgets.QTabWidget(self.page_2)
        self.CCTab.setGeometry(QtCore.QRect(70, 250, 761, 161))
        self.CCTab.setStyleSheet("background-color: rgb(235, 255, 222);")
        self.CCTab.setObjectName("CCTab")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.groupBox_18 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_18.setGeometry(QtCore.QRect(50, 20, 651, 91))
        self.groupBox_18.setObjectName("groupBox_18")
        self.CamCalButton1 = QtWidgets.QPushButton(self.groupBox_18)
        self.CamCalButton1.setGeometry(QtCore.QRect(10, 40, 171, 25))
        self.CamCalButton1.setObjectName("CamCalButton1")
        self.CUDSPButton = QtWidgets.QPushButton(self.groupBox_18)
        self.CUDSPButton.setGeometry(QtCore.QRect(210, 40, 211, 25))
        self.CUDSPButton.setObjectName("CUDSPButton")
        self.CUDCPButton = QtWidgets.QPushButton(self.groupBox_18)
        self.CUDCPButton.setGeometry(QtCore.QRect(440, 40, 201, 25))
        self.CUDCPButton.setObjectName("CUDCPButton")
        self.CCTab.addTab(self.tab_9, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox_22.setGeometry(QtCore.QRect(20, 10, 711, 101))
        self.groupBox_22.setObjectName("groupBox_22")
        self.SevButton = QtWidgets.QPushButton(self.groupBox_22)
        self.SevButton.setGeometry(QtCore.QRect(40, 50, 181, 25))
        self.SevButton.setObjectName("SevButton")
        self.EigButton = QtWidgets.QPushButton(self.groupBox_22)
        self.EigButton.setGeometry(QtCore.QRect(280, 50, 181, 25))
        self.EigButton.setObjectName("EigButton")
        self.RanButton = QtWidgets.QPushButton(self.groupBox_22)
        self.RanButton.setGeometry(QtCore.QRect(490, 50, 181, 25))
        self.RanButton.setObjectName("RanButton")
        self.CCTab.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab_14)
        self.groupBox_23.setGeometry(QtCore.QRect(40, 10, 641, 101))
        self.groupBox_23.setObjectName("groupBox_23")
        self.ELButton = QtWidgets.QPushButton(self.groupBox_23)
        self.ELButton.setGeometry(QtCore.QRect(80, 50, 141, 25))
        self.ELButton.setObjectName("ELButton")
        self.EPButton = QtWidgets.QPushButton(self.groupBox_23)
        self.EPButton.setGeometry(QtCore.QRect(390, 50, 131, 25))
        self.EPButton.setObjectName("EPButton")
        self.CCTab.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_15)
        self.groupBox_24.setGeometry(QtCore.QRect(40, 10, 651, 111))
        self.groupBox_24.setObjectName("groupBox_24")
        self.HomoButton = QtWidgets.QPushButton(self.groupBox_24)
        self.HomoButton.setGeometry(QtCore.QRect(10, 60, 301, 25))
        self.HomoButton.setObjectName("HomoButton")
        self.HomoButton_2 = QtWidgets.QPushButton(self.groupBox_24)
        self.HomoButton_2.setGeometry(QtCore.QRect(330, 60, 301, 25))
        self.HomoButton_2.setObjectName("HomoButton_2")
        self.CCTab.addTab(self.tab_15, "")
        self.ToolBoxIP.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 871, 425))
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(20, 330, 61, 81))
        self.label.setObjectName("label")
        self.groupBox_20 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_20.setGeometry(QtCore.QRect(20, 10, 141, 181))
        self.groupBox_20.setStyleSheet("background-color: rgb(255, 252, 208);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(237, 235, 130, 230), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox_20.setObjectName("groupBox_20")
        self.LoadButton_3 = QtWidgets.QPushButton(self.groupBox_20)
        self.LoadButton_3.setGeometry(QtCore.QRect(20, 80, 89, 25))
        self.LoadButton_3.setObjectName("LoadButton_3")
        self.groupBox_19 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_19.setGeometry(QtCore.QRect(180, 0, 601, 241))
        self.groupBox_19.setObjectName("groupBox_19")
        self.OutputLabel_4 = QtWidgets.QLabel(self.groupBox_19)
        self.OutputLabel_4.setGeometry(QtCore.QRect(340, 30, 251, 191))
        self.OutputLabel_4.setObjectName("OutputLabel_4")
        self.Inputlabel_4 = QtWidgets.QLabel(self.groupBox_19)
        self.Inputlabel_4.setGeometry(QtCore.QRect(40, 30, 251, 191))
        self.Inputlabel_4.setObjectName("Inputlabel_4")
        self.FDFRTab = QtWidgets.QTabWidget(self.page_3)
        self.FDFRTab.setGeometry(QtCore.QRect(90, 260, 761, 141))
        self.FDFRTab.setStyleSheet("background-color: rgb(235, 255, 222);")
        self.FDFRTab.setObjectName("FDFRTab")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.groupBox_47 = QtWidgets.QGroupBox(self.tab_25)
        self.groupBox_47.setGeometry(QtCore.QRect(50, 20, 651, 81))
        self.groupBox_47.setObjectName("groupBox_47")
        self.FDDLButton = QtWidgets.QPushButton(self.groupBox_47)
        self.FDDLButton.setGeometry(QtCore.QRect(80, 40, 211, 25))
        self.FDDLButton.setObjectName("FDDLButton")
        self.CCFDButton = QtWidgets.QPushButton(self.groupBox_47)
        self.CCFDButton.setGeometry(QtCore.QRect(370, 40, 231, 25))
        self.CCFDButton.setObjectName("CCFDButton")
        self.FDFRTab.addTab(self.tab_25, "")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.groupBox_48 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_48.setGeometry(QtCore.QRect(20, 10, 711, 91))
        self.groupBox_48.setObjectName("groupBox_48")
        self.DLFRButton = QtWidgets.QPushButton(self.groupBox_48)
        self.DLFRButton.setGeometry(QtCore.QRect(40, 50, 181, 25))
        self.DLFRButton.setObjectName("DLFRButton")
        self.LBPButton = QtWidgets.QPushButton(self.groupBox_48)
        self.LBPButton.setGeometry(QtCore.QRect(280, 50, 181, 25))
        self.LBPButton.setObjectName("LBPButton")
        self.PCAButton = QtWidgets.QPushButton(self.groupBox_48)
        self.PCAButton.setGeometry(QtCore.QRect(490, 50, 181, 25))
        self.PCAButton.setObjectName("PCAButton")
        self.FDFRTab.addTab(self.tab_26, "")
        self.ToolBoxIP.addItem(self.page_3, "")
        self.TitleLabel = QtWidgets.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(0, 10, 891, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TitleLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TitleLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.252632 rgba(122, 148, 70, 249), stop:1 rgba(255, 255, 255, 255));")
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")

        self.retranslateUi(Dialog)
        self.ToolBoxIP.setCurrentIndex(0)
        self.ImageTab.setCurrentIndex(0)
        self.CCTab.setCurrentIndex(0)
        self.FDFRTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IPCV TOOLBOX - PyQt5/OpenCV-3.4.2.17/Ubuntu/Atom"))
        self.ToolBoxIP.setToolTip(_translate("Dialog", "<html><head/><body><p>Image Processing Panel</p></body></html>"))
        self.ImageTab.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose a Image Processing Tool</p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "Select a Color Space"))
        self.GrayButton.setText(_translate("Dialog", "RGB2Gray"))
        self.HSVButton.setText(_translate("Dialog", "RGB2HSV"))
        self.YUVButton.setText(_translate("Dialog", "RGB2YUV"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab), _translate("Dialog", "Color Space"))
        self.groupBox_4.setTitle(_translate("Dialog", "Choose to Perform and Display"))
        self.HistEquiButton.setText(_translate("Dialog", "Histogram Equalization"))
        self.HistogramButton.setText(_translate("Dialog", "Histogram"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_6), _translate("Dialog", "Histogram"))
        self.groupBox_5.setTitle(_translate("Dialog", "Choosing a Type of Operator to Apply on Image"))
        self.LaplacianButton.setText(_translate("Dialog", "Laplacian"))
        self.SobelButton.setText(_translate("Dialog", "Sobel"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_3), _translate("Dialog", "Operators"))
        self.groupBox_6.setTitle(_translate("Dialog", "Choosing a Type of Morphological Operation"))
        self.ClosingButton.setText(_translate("Dialog", "Closing"))
        self.ErodeButton.setText(_translate("Dialog", "Erode"))
        self.OpeningBotton.setText(_translate("Dialog", "Opening"))
        self.DilateButton.setText(_translate("Dialog", "Dilate"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_8), _translate("Dialog", "Morphology"))
        self.groupBox_7.setTitle(_translate("Dialog", "Choosing a Type of Descriptor"))
        self.BBButton.setText(_translate("Dialog", "Bounding Box"))
        self.MECButton.setText(_translate("Dialog", "Max Enclosing Circles"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_4), _translate("Dialog", "Shape Descriptors"))
        self.groupBox_3.setTitle(_translate("Dialog", "Apply and Extract"))
        self.HLButton.setText(_translate("Dialog", "Hough Lines"))
        self.HCButton.setText(_translate("Dialog", "Hough Circles"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_2), _translate("Dialog", "Hough"))
        self.groupBox_8.setTitle(_translate("Dialog", "Choose to Apply"))
        self.SIFTButton.setText(_translate("Dialog", "SIFT"))
        self.SURFButton.setText(_translate("Dialog", "SURF"))
        self.FASTButton.setText(_translate("Dialog", "FAST"))
        self.HomoFButton.setText(_translate("Dialog", "Homography"))
        self.ISButton.setText(_translate("Dialog", "Image Stitching"))
        self.FMButton.setText(_translate("Dialog", "Feat Matching"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_5), _translate("Dialog", "Extract Features"))
        self.groupBox_9.setTitle(_translate("Dialog", "Other Miscelleneous"))
        self.EHCBotton.setText(_translate("Dialog", "Extract Harris Corners"))
        self.CCOButton.setText(_translate("Dialog", "Find Contours of Connected Objects"))
        self.EDCButton.setText(_translate("Dialog", "Edge Detection with Canny"))
        self.BlurButton.setText(_translate("Dialog", "Blur:Avg"))
        self.LogoButton.setText(_translate("Dialog", "Add Logo"))
        self.SPButton.setText(_translate("Dialog", "Add Noise::Salt-n-Pepper"))
        self.ImageTab.setTabText(self.ImageTab.indexOf(self.tab_7), _translate("Dialog", "Others"))
        self.groupBox.setToolTip(_translate("Dialog", "<html><head/><body><p>Click on the Load Button and Choose a Input Image!</p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "Image Input Control"))
        self.LoadButton.setText(_translate("Dialog", "Load"))
        self.groupBox_10.setTitle(_translate("Dialog", "Display"))
        self.OutputLabel.setText(_translate("Dialog", "Output Image"))
        self.Inputlabel.setText(_translate("Dialog", "Input Image"))
        self.ToolBoxIP.setItemText(self.ToolBoxIP.indexOf(self.page), _translate("Dialog", "Image Processing Panel"))
        self.Textlabel_2.setText(_translate("Dialog", "Here we are going to capture Image and Video :: Using Camera"))
        self.groupBox_12.setToolTip(_translate("Dialog", "<html><head/><body><p>Click on the Load Button and Choose a Input Image!</p></body></html>"))
        self.groupBox_12.setTitle(_translate("Dialog", "Camera Input Control"))
        self.LoadCButton.setText(_translate("Dialog", "Load"))
        self.groupBox_13.setTitle(_translate("Dialog", "Display"))
        self.Inputlabel_2.setText(_translate("Dialog", "Live Im/Vid"))
        self.OutputLabel_2.setText(_translate("Dialog", "Processed Im/Video"))
        self.groupBox_14.setToolTip(_translate("Dialog", "<html><head/><body><p>Press Capture Image or Capture Video to Capture Im/Vid by webCam</p></body></html>"))
        self.groupBox_14.setTitle(_translate("Dialog", "Camera Processing::"))
        self.CapIButton.setText(_translate("Dialog", "Capture Image "))
        self.groupBox_15.setToolTip(_translate("Dialog", "<html><head/><body><p>Press Capture Image or Capture Video to Capture Im/Vid by webCam</p></body></html>"))
        self.groupBox_15.setTitle(_translate("Dialog", "Camera Processing::"))
        self.CapVButton.setText(_translate("Dialog", "Capture Video"))
        self.ToolBoxIP.setItemText(self.ToolBoxIP.indexOf(self.page_4), _translate("Dialog", "Camera:: Image and/ Video Capture"))
        self.groupBox_16.setToolTip(_translate("Dialog", "<html><head/><body><p>Click on to load Camera input Image!</p></body></html>"))
        self.groupBox_16.setTitle(_translate("Dialog", "Camera Input Control"))
        self.LoadButton_2.setText(_translate("Dialog", "Load"))
        self.groupBox_17.setTitle(_translate("Dialog", "Display"))
        self.OutputLabel_3.setText(_translate("Dialog", "Output Image"))
        self.Inputlabel_3.setText(_translate("Dialog", "Input Image"))
        self.CCTab.setToolTip(_translate("Dialog", "<html><head/><body><p>Choose a Camera Calib Tool</p></body></html>"))
        self.groupBox_18.setTitle(_translate("Dialog", "Select an option:"))
        self.CamCalButton1.setText(_translate("Dialog", "Camera Calibration"))
        self.CUDSPButton.setText(_translate("Dialog", "Camera UndistortShortestPath"))
        self.CUDCPButton.setText(_translate("Dialog", "Camera UndistortCurvePath"))
        self.CCTab.setTabText(self.CCTab.indexOf(self.tab_9), _translate("Dialog", "Calibration"))
        self.groupBox_22.setTitle(_translate("Dialog", "Choose a method to Compute:"))
        self.SevButton.setText(_translate("Dialog", "7-pont method"))
        self.EigButton.setText(_translate("Dialog", "8-point method"))
        self.RanButton.setText(_translate("Dialog", "RANSAC"))
        self.CCTab.setTabText(self.CCTab.indexOf(self.tab_13), _translate("Dialog", "Fundamental Mat"))
        self.groupBox_23.setTitle(_translate("Dialog", "Find/Draw Epipoles and Epipolar lines:"))
        self.ELButton.setText(_translate("Dialog", "EpiLines"))
        self.EPButton.setText(_translate("Dialog", "Epipoles"))
        self.CCTab.setTabText(self.CCTab.indexOf(self.tab_14), _translate("Dialog", "Epipolar Geometry"))
        self.groupBox_24.setTitle(_translate("Dialog", "Find Homography:"))
        self.HomoButton.setText(_translate("Dialog", "Find Homography of two images: R-Rbar"))
        self.HomoButton_2.setText(_translate("Dialog", "Add R-Rbar: Mosaic"))
        self.CCTab.setTabText(self.CCTab.indexOf(self.tab_15), _translate("Dialog", "Homography"))
        self.ToolBoxIP.setItemText(self.ToolBoxIP.indexOf(self.page_2), _translate("Dialog", "Computer Vision Panel"))
        self.label.setText(_translate("Dialog", "FD/FR"))
        self.groupBox_20.setToolTip(_translate("Dialog", "<html><head/><body><p>Click on the Load Button and Choose a Input Image!</p></body></html>"))
        self.groupBox_20.setTitle(_translate("Dialog", "FD/FR Input Control"))
        self.LoadButton_3.setText(_translate("Dialog", "Load"))
        self.groupBox_19.setTitle(_translate("Dialog", "Display"))
        self.OutputLabel_4.setText(_translate("Dialog", "Output Image"))
        self.Inputlabel_4.setText(_translate("Dialog", "Input Image"))
        self.FDFRTab.setToolTip(_translate("Dialog", "<html><head/><body><p>Face Detection and Face Recognition Tools Available Here!</p></body></html>"))
        self.groupBox_47.setTitle(_translate("Dialog", "Choose Face Detection Method:"))
        self.FDDLButton.setText(_translate("Dialog", "Face Detect: Deep Learning"))
        self.CCFDButton.setText(_translate("Dialog", "Face Detect: Cascade classifiers"))
        self.FDFRTab.setTabText(self.FDFRTab.indexOf(self.tab_25), _translate("Dialog", "Face Detection"))
        self.groupBox_48.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox_48.setTitle(_translate("Dialog", "Choose Face Recognition Method:"))
        self.DLFRButton.setText(_translate("Dialog", "Deep Leaning based"))
        self.LBPButton.setText(_translate("Dialog", "Local Binary Patterns"))
        self.PCAButton.setText(_translate("Dialog", "PCA based"))
        self.FDFRTab.setTabText(self.FDFRTab.indexOf(self.tab_26), _translate("Dialog", "Face Recognition"))
        self.ToolBoxIP.setItemText(self.ToolBoxIP.indexOf(self.page_3), _translate("Dialog", "Face Detection and Face Recognition Panel"))
        self.TitleLabel.setToolTip(_translate("Dialog", "This is an IPCV ToolBox User-Interface"))
        self.TitleLabel.setText(_translate("Dialog", "IMAGE PROCESSING AND COMPUTER VISION TOOLBOX"))



# ==========================================================================================================================================================================
# Connections to the Buttons linking Section ===================================================

        self.LoadButton.clicked.connect(self.on_LoadButton_clicked)
        self.GrayButton.clicked.connect(self.on_GrayButton_clicked)
        self.LogoButton.clicked.connect(self.on_LogoButton_clicked)
        self.SPButton.clicked.connect(self.on_SPButton_clicked)

        self.HSVButton.clicked.connect(self.on_HSVButton_clicked)
        self.YUVButton.clicked.connect(self.on_YUVButton_clicked)

        self.BlurButton.clicked.connect(self.on_BlurButton_clicked)
        self.HistogramButton.clicked.connect(self.on_HistogramButton_clicked)
        self.HistEquiButton.clicked.connect(self.on_HistEquiButton_clicked)

        self.SobelButton.clicked.connect(self.on_SobelButton_clicked)
        self.LaplacianButton.clicked.connect(self.on_LaplacianButton_clicked)
        self.EDCButton.clicked.connect(self.on_EDCButton_clicked)

        self.DilateButton.clicked.connect(self.on_DilateButton_clicked)
        self.ErodeButton.clicked.connect(self.on_ErodeButton_clicked)
        self.OpeningBotton.clicked.connect(self.on_OpeningButton_clicked)
        self.ClosingButton.clicked.connect(self.on_ClosingButton_clicked)

        self.CapIButton.clicked.connect(self.on_CapIButton_clicked)
        self.CapVButton.clicked.connect(self.on_CapVButton_clicked)

        self.HLButton.clicked.connect(self.on_HLButton_clicked)
        self.HCButton.clicked.connect(self.on_HCButton_clicked)
        self.CCOButton.clicked.connect(self.on_CCOButton_clicked)
        self.BBButton.clicked.connect(self.on_BBButton_clicked)

        self.EHCBotton.clicked.connect(self.on_EHCButton_clicked)
        self.SIFTButton.clicked.connect(self.on_SIFTButton_clicked)
        self.SURFButton.clicked.connect(self.on_SURFButton_clicked)
        self.FASTButton.clicked.connect(self.on_FASTButton_clicked)

        self.CamCalButton1.clicked.connect(self.on_CamCalButton1_clicked)

        self.CCFDButton.clicked.connect(self.on_CCFDButton_clicked)
        self.ELButton.clicked.connect(self.on_ELButton_clicked)
        self.HomoFButton.clicked.connect(self.on_HomoFButton_clicked)
    #    self.FMButton.clicked.connect(self.on_FMatchButton_clicked)
    #    self.ISButton.clicked.connect(self.on_ISButton_clicked)

    #    self.EigButton_3.clicked.connect(self.on_EigButton_3_clicked)
    #    self.CCFDButton.clicked.connect(self.on_CCFDButton_clicked)


    #    self.FMatchButton.clicked.connect(self.on_FMatchButton_clicked)
    #    self.MECButton.clicked.connect(self.on_MECButton_clicked)

# =============================================================================================================================================================================
#   Load Image ----------------------------------------------------------------------------------------
    def on_LoadButton_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(Dialog,"Load Image", "","All Files (*)", options=options)
        img = cv.imread(fileName)
        cv.imshow('Input',img)
        global a
#        global zz
        a = img
        msgBox = QMessageBox()
        msgBox.setText("Image Loaded Successfully")
        msgBox.exec_()
# Add Salt and Papper Noise ----------------------------------------------------------------------------
    def on_SPButton_clicked(self):
        row,col,ch = a.shape
        sNp = 0.9
        amount = 0.05
        out = np.copy(a)

        # Salt mode
        num_salt = np.ceil(amount * a.size * sNp)
        coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in a.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* a.size * (1. - sNp))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in a.shape]
        out[coords] = 0

        cv.imshow('Salt & Pepper',out)
        cv.imwrite("Salt&PepperResults.jpg", out)

# Add Logo to the image ---------------------------------------------------------------------------------
    def on_LogoButton_clicked(self):
        logo = cv.imread("face.jpg")
        h, w, ch = logo.shape
        output = cv.resize(logo,(w,h),interpolation = cv.INTER_AREA)
        r = cv.selectROI(output)
        resized = cv.resize(logo, (r[2],r[3]), interpolation = cv.INTER_AREA)
        output[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] = resized
        cv.imshow("",output)
        cv.waitKey()

# =====================================================================================================================================================

# Convert RGB to Gray Image ColourSpace----------------------------------------------------------------------
    def on_GrayButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_BGR2GRAY)
        gray = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
        #--- Here I am creating the border---
        black = [0,0,0]     #---Color of the border---
        constant=cv.copyMakeBorder(a,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        constant2=cv.copyMakeBorder(gray,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        text1 = "Input Image"
        text2 = "Output Image"
        img1 = cv.putText(constant.copy(), text1, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
        img2 = cv.putText(constant2.copy(), text2, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))

        result = cv.hconcat((img1, img2))
        cv.imshow('Display',result)
        cv.waitKey()

# Convert RGB to HSV Image ColourSpace----------------------------------------------------------------------
    def on_HSVButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_BGR2HSV)
        #--- Here I am creating the border---
        black = [0,0,0]     #---Color of the border---
        constant=cv.copyMakeBorder(a,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        constant2=cv.copyMakeBorder(gray,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        text1 = "Input Image"
        text2 = "Output Image"
        img1 = cv.putText(constant.copy(), text1, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
        img2 = cv.putText(constant2.copy(), text2, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (129,254,254))

        result = cv.hconcat((img1, img2))
        cv.imshow('Display',result)
        cv.waitKey()

# Convert RGB to YUV Image ColorSpace ---------------------------------------------------------------------------
    def on_YUVButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_BGR2YUV)
        #--- Here I am creating the border---
        black = [0,0,0]     #---Color of the border---
        constant=cv.copyMakeBorder(a,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        constant2=cv.copyMakeBorder(gray,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        text1 = "Input Image"
        text2 = "Output Image"
        img1 = cv.putText(constant.copy(), text1, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
        img2 = cv.putText(constant2.copy(), text2, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))

        result = cv.hconcat((img1, img2))
        cv.imshow('Display',result)
        cv.waitKey()

# Convert Normal Image to Blur Image ---------------------------------------------------------------------------
    def on_BlurButton_clicked(self):
        gray = cv.blur(a,(5,5))
        #--- Here I am creating the border---
        black = [0,0,0]     #---Color of the border---
        constant=cv.copyMakeBorder(a,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        constant2=cv.copyMakeBorder(gray,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        text1 = "Input Image"
        text2 = "Output Image"
        img1 = cv.putText(constant.copy(), text1, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
        img2 = cv.putText(constant2.copy(), text2, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))

        result = cv.hconcat((img1, img2))
        cv.imshow('Display',result)
        cv.waitKey()

# Display Histogram of the Input Image-----------------------------------------------------------------------------
    def on_HistogramButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        plt.hist(gray.ravel(),256,[0,256])
        plt.show()
        cv.waitKey()

# Display Histogram Equalized version of the Input Image-----------------------------------------------------------
    def on_HistEquiButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        equ = cv.equalizeHist(gray)
        res = np.hstack((gray,equ)) #stacking images side-by-side
        cv.imwrite('res.png',res)
        #--- Here I am creating the border---
        black = [0,0,0]     #---Color of the border---
        constant=cv.copyMakeBorder(gray,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        constant2=cv.copyMakeBorder(res,50,10,10,10,cv.BORDER_CONSTANT,value=black)
        text1 = "Input Image"
        text2 = "Output Image"
        img1 = cv.putText(constant.copy(), text1, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
        img2 = cv.putText(constant2.copy(), text2, (50, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0))

        result = cv.hconcat((img1, img2))
        cv.imshow('Display',result)
        cv.waitKey()

# Apply Sobel Operator on the Input IMAGE ------------------------------------------------------------------------
    def on_SobelButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_BGR2GRAY)
        gray1 =  cv.Sobel(gray,cv.CV_64F,1,0,ksize=5)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(gray1,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Apply Laplacian Operator on the Input Image---------------------------------------------------------------------------------
    def on_LaplacianButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        gray1 = cv.Laplacian(gray,cv.CV_64F)
        plt.subplot(1,2,1),plt.imshow(a,cmap = 'gray')
        plt.subplot(1,2,2),plt.imshow(gray1,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Applt Canny Edge Detector on the Input Image -----------------------------------------------------------------------
    def on_EDCButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        edges = cv.Canny(gray,100,200)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(edges,cmap = 'gray')
        plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Apply Dilation on Input Image ----------------------------------------------------------------------------------
    def on_DilateButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        kernel = np.ones((5,5),np.uint8)
        dilate = cv.dilate(gray,kernel,iterations = 1)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(dilate,cmap = 'gray')
        plt.title('Dilated Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Apply Erosion on Input Image -------------------------------------------------------------------------------------------
    def on_ErodeButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        kernel = np.ones((5,5),np.uint8)
        erode = cv.erode(gray,kernel,iterations = 1)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(erode,cmap = 'gray')
        plt.title('Erode Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Apply Opening on Input Image -------------------------------------------------------------------------------------------
    def on_OpeningButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        kernel = np.ones((5,5),np.uint8)
        opening = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(opening,cmap = 'gray')
        plt.title('Opening Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

#  Apply Closing on Input Image ----------------------------------------------------------------------------------
    def on_ClosingButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        kernel = np.ones((5,5),np.uint8)
        closing = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)
        plt.subplot(1,2,1),plt.imshow(gray,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(closing,cmap = 'gray')
        plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        cv.waitKey()

# Apply HoughLines on Input Image ----------------------------------------------------------------------------------
    def on_HLButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray,50,150,apertureSize = 3)
        lines = cv.HoughLines(edges,1,np.pi/180,510)
        for line in lines:
            rho,theta = line[0]
            aa = np.cos(theta)
            b = np.sin(theta)
            x0 = aa*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(aa))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(aa))
            cv.line(gray,(x1,y1),(x2,y2),(0,0,255),2)
        cv.imwrite('houghlines3.jpg',gray)

# Apply HoughCircles on Input Image ----------------------------------------------------------------------------------
    def on_HCButton_clicked(self):
        img = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        img = cv.medianBlur(img,5)
        cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
        circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        cv.imshow('detected circles',cimg)
        cv.waitKey(0)
        cv.destroyAllWindows()

# Apply contour Connection Objects on Input Image ---------------------------------------------------------------------------
    def on_CCOButton_clicked(self):
        imgray = cv.cvtColor(a, cv.COLOR_RGB2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        im2,contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        ij=cv.drawContours(a, contours, -1, (0,0,0), 3)
        cv.imwrite('ccc.jpg',ij)

# Apply BoundingBox on Input Image ----------------------------------------------------------------------------------
    def on_BBButton_clicked(self):
        imgray = cv.cvtColor(a, cv.COLOR_RGB2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        im2,contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        cnt = contours[0]
        x,y,w,h = cv.boundingRect(cnt)
        ij=cv.rectangle(a,(x,y),(x+w,y+h),(255,255,255),4)
        cv.imwrite('uuu.jpg',ij)

# Extract Harris Corners on Input Image ----------------------------------------------------------------------------------
    def on_EHCButton_clicked(self):
        gray = cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        gray = np.float32(gray)
        dst = cv.cornerHarris(gray,2,3,0.0004)
        #result is dilated for marking the corners, not important
        dst = cv.dilate(dst,None)
        # Threshold for an optimal value, it may vary depending on the image.
        a[dst>0.01*dst.max()]=[255,255,255]
        cv.imshow('harris corners',a)
        if cv.waitKey(0) & 0xff == 27:
            cv.destroyAllWindows()

# Apply SIFT Feature Operation------------------------------------------------------------------------------------
    def on_SIFTButton_clicked(self):
        gray= cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        sift = cv.xfeatures2d.SIFT_create()
        kp = sift.detect(gray,None)
        img=cv.drawKeypoints(gray,kp,a,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv.imwrite('sift_keypoints.jpg',a)

# Apply SURF Feature Operation --------------------------------------------------------------------------------------------
    def on_SURFButton_clicked(self):
        gray= cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        surf = cv.xfeatures2d.SURF_create(300)
        kp, des = surf.detectAndCompute(a,None)
        img2 = cv.drawKeypoints(a,kp,None,(255,0,0),4)
        cv.imwrite('surf_keypoints.jpg',img2)
        plt.imshow(img2),plt.show()

# Apply FAST Feature Operation -----------------------------------------------------------------------------------------
    def on_FASTButton_clicked(self):
        gray= cv.cvtColor(a,cv.COLOR_RGB2GRAY)
        # Initiate FAST object with default values
        fast = cv.FastFeatureDetector_create()
        #    find and draw the keypoints
        kp = fast.detect(gray,None)
        img2 = cv.drawKeypoints(gray, kp, None, color=(255,0,0))
        cv.imwrite('fast_true.png',img2)
        # Disable nonmaxSuppression
        fast.setNonmaxSuppression(0)
        kp = fast.detect(a,None)
        img3 = cv.drawKeypoints(a, kp, None, color=(255,0,0))
        cv.imwrite('fast_false.png',img3)

#=====================================================================================================================================

# Capture Image from a Camera ----------------------------------------------------------------------------
    def on_CapIButton_clicked(self):
        msgBox = QMessageBox()
        msgBox.setFixedWidth(1500)
        msgBox.setText("Attention!")
        msgBox.setInformativeText("Press 'c' to Capture Image, then Press 'q' to Quit")
        msgBox.exec_()
        cap = cv.VideoCapture(0)#0 is internal cam : 1 is external webcam
        #i=0 #to save all the clicked images
        while(True):
            ret, frame = cap.read()
            cv.imshow("imshow",frame)
            key=cv.waitKey(30)
            if key==ord('q'):
                break
            if key==ord('c'):
            #i+=1
                cv.imshow("Captured Image",frame)
                global bb
                bb = frame
                # release the capture
        cap.release()
        cv.destroyAllWindows()

# Capture Video from a Camera ----------------------------------------------------------------------------
    def on_CapVButton_clicked(self):
        cap = cv.VideoCapture(0)
        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640,  480))
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = cv.flip(frame, 1)
            # write the flipped frame
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        # Release everything if job is finished
        cap.release()
        out.release()
        cv.destroyAllWindows()

# ====================================================================================================================================

# Perform Camera Calibration for the chessbord Pattern -------------------------------------------------------------------------------
    def on_CamCalButton1_clicked(self):
        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((6*7,3), np.float32)
        objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.
        images = glob.glob('*.jpg')
        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (7,6), None)
            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
                imgpoints.append(corners)
                # Draw and display the corners
                cv.drawChessboardCorners(img, (7,6), corners2, ret)
                cv.imshow('img', img)
                cv.waitKey(500)
        cv.destroyAllWindows()

        # ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        # img = cv.imread('left12.jpg')
        # h,  w = img.shape[:2]
        # newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
        # # undistort
        # #dst = cv.undistort(img, mtx, dist, None, newcameramtx)
        # crop the image
        # x, y, w, h = roi
        # dst = dst[y:y+h, x:x+w]
        # cv.imwrite('calibresult.png', dst)
# =================================================================================================================================
# Epipolar Lines and Epipoles
    def on_ELButton_clicked(self):
        img = cv.imread('myleft.jpg')
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img2 = cv.imread('myright.jpg')
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        img1 = cv.resize(img, (0,0), fx=0.2, fy=0.2)
        img2 = cv.resize(img2, (0,0), fx=0.2, fy=0.2)

        sift = cv.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)

        flann = cv.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(des1,des2,k=2)

        good = []
        pts1 = []
        pts2 = []

        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.8*n.distance:
                good.append(m)
                pts2.append(kp2[m.trainIdx].pt)
                pts1.append(kp1[m.queryIdx].pt)

        pts1 = np.int32(pts1)
        pts2 = np.int32(pts2)
        F, mask = cv.findFundamentalMat(pts1,pts2,cv.FM_LMEDS)

        # We select only inlier points
        pts1 = pts1[mask.ravel()==1]
        pts2 = pts2[mask.ravel()==1]


        def drawlines(img1,img2,lines,pts1,pts2):
            ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
            r,c = img1.shape
            img1 = cv.cvtColor(img1,cv.COLOR_GRAY2BGR)
            img2 = cv.cvtColor(img2,cv.COLOR_GRAY2BGR)
            for r,pt1,pt2 in zip(lines,pts1,pts2):
                color = tuple(np.random.randint(0,255,3).tolist())
                x0,y0 = map(int, [0, -r[2]/r[1] ])
                x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
                img1 = cv.line(img1, (x0,y0), (x1,y1), color,1)
                img1 = cv.circle(img1,tuple(pt1),5,color,-1)
                img2 = cv.circle(img2,tuple(pt2),5,color,-1)
            return img1,img2

        # Find epilines corresponding to points in right image (second image) and
        # drawing its lines on left image
        lines1 = cv.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2,F)
        lines1 = lines1.reshape(-1,3)
        img5,img6 = drawlines(img1,img2,lines1,pts1,pts2)

        # Find epilines corresponding to points in left image (first image) and
        # drawing its lines on right image
        lines2 = cv.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
        lines2 = lines2.reshape(-1,3)
        img3,img4 = drawlines(img2,img1,lines2,pts2,pts1)

        cv.imshow('img5', img5)
        cv.imshow('img3', img3)
        cv.imwrite("result_epipolar.jpg", img3)


#====================================================================================================================================
# Compute Hoomgraphy, Feature Matching and Display in a single Image ---------------------------------------------
    def on_HomoFButton_clicked(self):
        MIN_MATCH_COUNT = 5
        i1 = cv.imread("box.png")
        img1 = cv.cvtColor(i1, cv.COLOR_BGR2GRAY)
        i2 = cv.imread("box_in_scene.png")
        img2 = cv.cvtColor(i2, cv.COLOR_BGR2GRAY)

        # Initiate SIFT detector
        sift = cv.xfeatures2d.SIFT_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)

        flann = cv.FlannBasedMatcher(index_params, search_params)               # Feature FeatureMatching between two Images ===========================

        matches = flann.knnMatch(des1,des2,k=2)

        # store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)


        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)        # Compute Homography ===============================================
            matchesMask = mask.ravel().tolist()

            h,w = img1.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv.perspectiveTransform(pts,M)

            img2 = cv.polylines(img2,[np.int32(dst)],True,255,3, cv.LINE_AA)

        else:
            print ("Not enough matches are found - %d/%d"  (len(good),MIN_MATCH_COUNT))
            matchesMask = None

        draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

        img3 = cv.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

        cv.imshow('Compute Homography and Display Single Image Output ', img3)  # Singel Image Display ======================================
        cv.imwrite('result_homography.jpg', img3)


#  FaceDetection and Face Recognition Algorithms --**** SECTION 4  ****

#  Detect Faces using Cascade Classifier ------------------------------------------------------------------------------
    def on_CCFDButton_clicked(self):
        imagePath = 'images.jpg'
        faceCascPath = 'haarcascade_frontalface_default.xml'

        faceCascade = cv.CascadeClassifier(faceCascPath)

        image = cv.imread(imagePath)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        faces = ""
        faces = faceCascade.detectMultiScale( gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = 0)
                  # parametr flags został zmeiniony ze względów kompatybilności, ale defacto efekt jest ten sam
            # flags = cv2.CV_HAAR_SCALE_IMAGE

        print("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        plt.imshow(image, cmap='gray')
        plt.show()

        imagePath = 'face.jpg'

        eyeCascPath = 'eyecascade.xml'
        mouthCascPath = 'Mouth.xml'
        noseCascPath = 'nose.xml'

        eyeCascade = cv.CascadeClassifier(eyeCascPath)
        mouthCascade = cv.CascadeClassifier(mouthCascPath)
        noseCascade = cv.CascadeClassifier(noseCascPath)

        image = cv.imread(imagePath)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        faces = ""
        eyes = ""
        noses = ""
        noses = ""

        faces = faceCascade.detectMultiScale( gray,scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = 0)
        eyes = eyeCascade.detectMultiScale( gray,scaleFactor=1.9)
        noses = noseCascade.detectMultiScale(gray,scaleFactor=2.5)
        mouths = mouthCascade.detectMultiScale(gray,scaleFactor=5.5)

        print("Found {0} faces!".format(len(faces)))
        print("Found {0} eyes!".format(len(eyes)))
        print("Found {0} noses!".format(len(noses)))
        print("Found {0} mouths!".format(len(mouths)))
        for (x, y, w, h) in faces:
            cv.rectangle(image,(x, y), (x+w, y+h), (0, 255, 0), 2)
        for (x, y, w, h) in eyes:
            cv.rectangle(image,(x, y), (x+w, y+h), (255, 0, 0), 2)
        for (x, y, w, h) in noses:
            cv.rectangle(image,(x, y), (x+w, y+h), (255, 0, 255), 2)
        for (x, y, w, h) in mouths:
            cv.rectangle(image,(x, y), (x+w, y+h), (255, 255, 0), 2)

        plt.imshow(image, cmap='gray')
        plt.show()

# =================================================================================================================================================

# Face Recognition Algorithm Local BinaryPatterns -------------  Uncomment this code when not necessary
#   def on_LBPButton_clicked(self):
#       exec_(vam11.py)

# ==============================================================================================================================================


# Image Stitching ----------------------------------------------------------------------------
#    def on_ISButton_clicked(self):
#        i1 = cv.imread("frame.png")
#        img1 = cv.cvtColor(i1, cv.COLOR_BGR2GRAY)
#        i2 = cv.imread("frame2.png")
#        img2 = cv.cvtColor(i2, cv.COLOR_BGR2GRAY)
#        result = stitcher.stitch((img1,img2))

#        cv.imwrite("result_stitch.jpg", result[1])
#        original = "original.tif"
#        cropped = "cropped.jpeg"

# This is already implementedd in Homography
# Feature FeatureMatching between two images ----------------------------------------------------
#    def on_FMatchButton_clicked(self):
#        i1 = cv.imread("frame.jpg")
#        i2 = cv.imread("frame2.jpg")
#        sift = cv.SIFT_create()
#        kp1, des1, = sift.detectAndCompute(i1,None)
#        kp2, des2, = sift.detectAndCompute(i2,None)
#        bf = cv.BFMatcher()
#        matches = bf.knnMatch(des1,des2, k=2)
#        good = []
#        for m,n in matches:
#            if m.distance < .1*n.distance:
#                good.append([m])
#        result = cv.drawMatchesKnn(i1,kp1,i2,kp2,good)
#        cv.imshow('results',result)
# =================================================================================================================================

#=========================================================================================================================================================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
