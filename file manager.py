from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
import os
class Ui_MainWindow(object):
    def __init__(self):
        self.file_name = "COD4"
        self.icon_folder = QtGui.QIcon()
        self.icon_folder.addPixmap(QtGui.QPixmap("folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_exe = QtGui.QIcon()
        self.icon_exe.addPixmap(QtGui.QPixmap("exe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pdf = QtGui.QIcon()
        self.icon_pdf.addPixmap(QtGui.QPixmap("pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_txt = QtGui.QIcon()
        self.icon_txt.addPixmap(QtGui.QPixmap("txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_msi = QtGui.QIcon()
        self.icon_msi.addPixmap(QtGui.QPixmap("msi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_image = QtGui.QIcon()
        self.icon_image.addPixmap(QtGui.QPixmap("picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_settings = QtGui.QIcon()
        self.icon_settings.addPixmap(QtGui.QPixmap("settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_rar = QtGui.QIcon()
        self.icon_rar.addPixmap(QtGui.QPixmap("rar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_video = QtGui.QIcon()
        self.icon_video.addPixmap(QtGui.QPixmap("video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_unknown = QtGui.QIcon()
        self.icon_unknown.addPixmap(QtGui.QPixmap('unknown.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drive_list =[ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GoButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton.setGeometry(QtCore.QRect(720, 7, 51, 31))
        self.GoButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 90, 581, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,300)
        

