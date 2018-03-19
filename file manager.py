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
        for i in range(len(self.drive_list)):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(self.drive_list[i])))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 581, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.GoButton.clicked.connect(self.go_button)
        self.tableWidget.clicked.connect(self.row_press)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "file name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "size"))
        self.lineEdit.setText("")
        self.GoButton.setText("GO")
    def go_button(self):
        try:
            self.tableWidget.setRowCount(0)
            os.chdir(self.lineEdit.text())
            in_directory = os.listdir()
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                self.tableWidget.setRowHeight(i,25)
            self.tableWidget.setRowHeight(0,25)
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j ==0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(self.lineEdit.text()+'\\'+in_directory[i])
                        if file_extension == ".exe":
                            item.setIcon(self.icon_exe)
                        elif file_extension == '':
                            item.setIcon(self.icon_folder)
                        elif file_extension == ".pdf":
                            item.setIcon(self.icon_pdf)
                        elif file_extension == ".txt":
                            item.setIcon(self.icon_txt)
                        elif file_extension == ".MSI" or file_extension == ".Msi":
                            item.setIcon(self.icon_msi)
                        elif file_extension == ".jpg" or file_extension == ".bmp" or file_extension == ".png" or file_extension == ".ico":
                            item.setIcon(self.icon_image)
                        elif file_extension == ".dll" or file_extension == ".sys" or file_extension == ".ini" or file_extension == ".SAV":
                            item.setIcon(self.icon_settings)
                        elif file_extension == '.rar' or file_extension == ".zip" or file_extension == ".cab" or file_extension == '.iso':
                            item.setIcon(self.icon_rar)
                        elif file_extension == '.mkv' or file_extension == ".mpg" or file_extension == ".mov" or file_extension == '.mp4' or file_extension == '.3gp' or file_extension == ".VOB":
                            item.setIcon(self.icon_video)
                        else:
                            item.setIcon(self.icon_unknown)
        except FileNotFoundError:
            self.lineEdit.setText("not valid address")
    def row_press(self):
        r = self.tableWidget.currentRow()
        self.file_name = self.tableWidget.item(r,0).text()
        if len(self.file_name) == 2:
            next_address = self.file_name+ '\\'
        else:
            current_address = os.getcwd()
            next_address = current_address +"\\" + self.file_name
