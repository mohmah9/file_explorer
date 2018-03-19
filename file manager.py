
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QInputDialog, QLineEdit
import os
import shutil
class Ui_MainWindow(object):
    def __init__(self):
        self.file_name = ""
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
        self.icon_unknown.addPixmap(QtGui.QPixmap('unknown.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_music = QtGui.QIcon()
        self.icon_music.addPixmap(QtGui.QPixmap('music.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_desktop = QtGui.QIcon()
        self.icon_desktop.addPixmap(QtGui.QPixmap('desktop.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_download = QtGui.QIcon()
        self.icon_download.addPixmap(QtGui.QPixmap('download.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pictures = QtGui.QIcon()
        self.icon_pictures.addPixmap(QtGui.QPixmap('pictures.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_musics = QtGui.QIcon()
        self.icon_musics.addPixmap(QtGui.QPixmap('musics.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_videos = QtGui.QIcon()
        self.icon_videos.addPixmap(QtGui.QPixmap('videos.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_documents = QtGui.QIcon()
        self.icon_documents.addPixmap(QtGui.QPixmap('documents.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_drives = QtGui.QIcon()
        self.icon_drives.addPixmap(QtGui.QPixmap('drives.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_window_icon = QtGui.QIcon()
        self.main_window_icon.addPixmap(QtGui.QPixmap('main_icon.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_back = QtGui.QIcon()
        self.icon_back.addPixmap(QtGui.QPixmap('back.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_go = QtGui.QIcon()
        self.icon_go.addPixmap(QtGui.QPixmap('go.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_copy = QtGui.QIcon()
        self.icon_copy.addPixmap(QtGui.QPixmap('copy.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_cut = QtGui.QIcon()
        self.icon_cut.addPixmap(QtGui.QPixmap('cut.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_new_folder = QtGui.QIcon()
        self.icon_new_folder.addPixmap(QtGui.QPixmap('new_folder.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_rename = QtGui.QIcon()
        self.icon_rename.addPixmap(QtGui.QPixmap('rename.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_delete = QtGui.QIcon()
        self.icon_delete.addPixmap(QtGui.QPixmap('delete.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drive_list =[ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
        self.Quick_access = ""
        self.logo_icon = QtGui.QIcon()
        self.logo_icon.addPixmap(QtGui.QPixmap('logo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setWindowIcon(self.main_window_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GoButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton.setGeometry(QtCore.QRect(1130, 88, 31, 31))
        self.GoButton.setObjectName("pushButton")
        self.GoButton.setFlat(True)
        self.GoButton.setIcon(self.icon_go)
        self.GoButton.setIconSize(QtCore.QSize(30,30))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 120, 950, 655))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,350)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setRowCount(len(self.drive_list))
        y = 0
        x = 0
        for i in range(len(self.drive_list)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(self.drive_list[i])
            item.setIcon(self.icon_drives)
            self.tableWidget.setItem(y, 0, item)
            y+=1
        for i in range(len(self.drive_list)):
            item = QtWidgets.QTableWidgetItem()
            item.setText("Drive")
            self.tableWidget.setItem(x, 1, item)
            x+=1
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(530, 11, 500, 81))
        self.logo.setIconSize(QtCore.QSize(80, 80))
        self.logo.setFlat(True)
        self.logo.setIcon(self.logo_icon)
        self.logo.setIconSize(QtCore.QSize(500, 81))
        self.logo.setObjectName("logo")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(10, 120, 230, 655))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0,item)
        self.tableWidget2.setColumnWidth(0,230)
        self.tableWidget2.setRowCount(len(self.drive_list)+6)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Desktop")
        item.setIcon(self.icon_desktop)
        self.tableWidget2.setItem(0,0,item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Downloads")
        item.setIcon(self.icon_download)
        self.tableWidget2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Pictures")
        item.setIcon(self.icon_pictures)
        self.tableWidget2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Musics")
        item.setIcon(self.icon_musics)
        self.tableWidget2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Videos")
        item.setIcon(self.icon_videos)
        self.tableWidget2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Documents")
        item.setIcon(self.icon_documents)
        self.tableWidget2.setItem(5, 0, item)
        x = 1
        for drive in self.drive_list:
            item = QtWidgets.QTableWidgetItem()
            item.setText("Drive" + " "+str(drive))
            item.setIcon(self.icon_drives)
            self.tableWidget2.setItem(5+x, 0, item)
            x+=1
        self.tableWidget2.verticalHeader().setVisible(False)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 95, 600, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(485, 88, 31, 31))
        self.back_button.setObjectName("Back")
        self.back_button.setIcon(self.icon_back)
        self.back_button.setIconSize(QtCore.QSize(30,30))
        self.back_button.setFlat(True)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 105, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 27, 20, 88))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(460, 27, 20, 88))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(365, 27, 20, 88))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(278, 27, 20, 88))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(185, 27, 20, 88))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(91, 27, 20, 88))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 81, 81))
        self.pushButton.setText("")
        self.pushButton.setIcon(self.icon_new_folder)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("new_folder")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 81, 81))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(self.icon_copy)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("copy")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 30, 81, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(self.icon_cut)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("cut")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 30, 81, 81))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(self.icon_delete)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("delete")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 30, 81, 81))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(self.icon_rename)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("rename")





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.actionNew_folder = QtWidgets.QAction(MainWindow)
        self.actionNew_folder.setObjectName("actionNew_folder")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.menuEdit.addAction(self.actionNew_folder)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionRename)
        self.menubar.addAction(self.menuEdit.menuAction())
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.GoButton.clicked.connect(self.go_button)
        self.tableWidget.doubleClicked.connect(self.row_press)
        self.back_button.clicked.connect(self.Back_button)
        self.tableWidget2.clicked.connect(self.quick_access)
        self.pushButton.clicked.connect(self.new_folder)
        self.pushButton_2.clicked.connect(self.copy_file)
        self.pushButton_3.clicked.connect(self.cut)
        self.pushButton_4.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.rename)
        self.actionNew_folder.triggered.connect(self.new_folder)
        self.actionCopy.triggered.connect(self.copy_file)
        self.actionCut.triggered.connect(self.cut)
        self.actionDelete.triggered.connect(self.delete)
        self.actionRename.triggered.connect(self.rename)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pro File Manager"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "file name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "size"))
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Quick access"))
        self.lineEdit.setText("")
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew_folder.setText(_translate("MainWindow", "new folder"))
        self.actionCopy.setText(_translate("MainWindow", "copy"))
        self.actionCut.setText(_translate("MainWindow", "cut"))
        self.actionDelete.setText(_translate("MainWindow", "delete"))
        self.actionRename.setText(_translate("MainWindow", "rename"))
    def go_button(self):
        try:
            os.chdir(self.lineEdit.text())
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(str(os.path.getsize(self.lineEdit.text()+'\\'+in_directory[i])/(1024**2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(self.lineEdit.text() + '\\' + in_directory[i])
                        if file_extension3!="":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        except:
            self.lineEdit.setText("not valid address")
    def row_press(self):
        try:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r,0).text()
            file_name2 , file_extension2 = os.path.splitext(self.lineEdit.text() + "\\"+self.file_name)
            if file_extension2 == "":
                if len(self.file_name) == 2:
                    next_address = self.file_name+ '\\'
                else:
                    current_address = os.getcwd()
                    next_address = current_address +"\\" + self.file_name
                self.lineEdit.setText(next_address)
                os.chdir(next_address)
                in_directory = os.listdir()
                in_directory = in_directory[::-1]
                self.tableWidget.setRowCount(0)
                self.tableWidget.setRowCount(len(in_directory))
                for i in range(len(in_directory)):
                    for j in range(3):
                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(i, j, item)
                        if j == 0:
                            item.setText(str(in_directory[i]))
                            file_name, file_extension = os.path.splitext(self.lineEdit.text() + '\\' + in_directory[i])
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
                            elif file_extension == '.mp3' or file_extension == ".wmv":
                                item.setIcon(self.icon_music)
                            else:
                                item.setIcon(self.icon_unknown)
                        if j == 2:
                            item.setText(str(os.path.getsize(self.lineEdit.text()+'\\'+in_directory[i])/(1024**2)))
                        if j == 1:
                            file_name3, file_extension3 = os.path.splitext(self.lineEdit.text() + '\\' + in_directory[i])
                            if file_extension3!="":
                                item.setText(file_extension3[1:])
                            else:
                                item.setText("folder")
            else:
                os.startfile(self.lineEdit.text() + "\\"+self.file_name)
        except:
            pass
    def Back_button(self):
        if self.lineEdit.text()!= "":
            current_address = self.lineEdit.text()
            current_address_list = current_address.split("\\")
            if len(current_address_list) > 2:
                back_address = current_address_list[:len(current_address_list)-1]
                back_address = "\\".join(back_address)
                os.chdir(back_address)
                self.lineEdit.setText(back_address)
                try:
                    self.tableWidget.setRowCount(0)
                    in_directory = os.listdir()
                    in_directory = in_directory[::-1]
                    self.tableWidget.setRowCount(len(in_directory))
                    for i in range(len(in_directory)):
                        self.tableWidget.setRowHeight(i, 25)
                    self.tableWidget.setRowHeight(0, 25)
                    for i in range(len(in_directory)):
                        for j in range(3):
                            item = QtWidgets.QTableWidgetItem()
                            self.tableWidget.setItem(i, j, item)
                            if j == 0:
                                item.setText(str(in_directory[i]))
                                file_name, file_extension = os.path.splitext(
                                    self.lineEdit.text() + '\\' + in_directory[i])
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
                                elif file_extension == '.mp3' or file_extension == ".wmv":
                                    item.setIcon(self.icon_music)
                                else:
                                    item.setIcon(self.icon_unknown)
                            if j == 2:
                                item.setText(
                                    str(os.path.getsize(self.lineEdit.text() + '\\' + in_directory[i]) / (1024 ** 2)))
                            if j == 1:
                                file_name3, file_extension3 = os.path.splitext(
                                    self.lineEdit.text() + '\\' + in_directory[i])
                                if file_extension3 != "":
                                    item.setText(file_extension3[1:])
                                else:
                                    item.setText("folder")
                except:
                    self.lineEdit.setText("not valid address")
            if len(current_address_list) == 2 and current_address_list[len(current_address_list)-1]!='':
                back_address = current_address_list[0] + "\\"
                os.chdir(back_address)
                self.lineEdit.setText(back_address)
                try:
                    self.tableWidget.setRowCount(0)
                    in_directory = os.listdir()
                    in_directory = in_directory[::-1]
                    self.tableWidget.setRowCount(len(in_directory))
                    for i in range(len(in_directory)):
                        self.tableWidget.setRowHeight(i, 25)
                    self.tableWidget.setRowHeight(0, 25)
                    for i in range(len(in_directory)):
                        for j in range(3):
                            item = QtWidgets.QTableWidgetItem()
                            self.tableWidget.setItem(i, j, item)
                            if j == 0:
                                item.setText(str(in_directory[i]))
                                file_name, file_extension = os.path.splitext(
                                    self.lineEdit.text() + '\\' + in_directory[i])
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
                                elif file_extension == '.mp3' or file_extension == ".wmv":
                                    item.setIcon(self.icon_music)
                                else:
                                    item.setIcon(self.icon_unknown)
                except:
                    self.lineEdit.setText("not valid address")
            elif len(current_address_list) == 2 and current_address_list[len(current_address_list)-1]=='':
                back_address = ""
                self.lineEdit.setText(back_address)
                self.tableWidget.setRowCount(len(self.drive_list))
                self.tableWidget.setRowCount(0)
                self.tableWidget.setRowCount(len(self.drive_list))
                for i in range(len(self.drive_list)):
                    for j in range(3):
                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(i, j, item)
                        if j == 0:
                            item.setText(str(self.drive_list[i]))
                            item.setIcon(self.icon_drives)
                        if j == 1:
                            item.setText("Drive")
    def quick_access(self):
        r = self.tableWidget2.currentRow()
        self.Quick_access = self.tableWidget2.item(r, 0).text()
        if self.Quick_access=="Desktop":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Desktop')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Desktop')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Desktop\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Desktop\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Desktop\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access=="Downloads":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Downloads')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Downloads')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Downloads\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Downloads\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Downloads\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access=="Pictures":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Pictures')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Pictures')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Pictures\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Pictures\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Pictures\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access=="Documents":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Documents')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Documents')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Documents\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Documents\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Documents\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access=="Musics":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Music')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Music')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Music\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Music\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Music\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access=="Videos":
            self.lineEdit.setText("C:\\Users\\"+str(os.getlogin())+'\\Videos')
            os.chdir("C:\\Users\\"+str(os.getlogin())+'\\Videos')
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Videos\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize("C:\\Users\\" + str(os.getlogin()) + '\\Videos\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            "C:\\Users\\" + str(os.getlogin()) + '\\Videos\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
        if self.Quick_access[:5] == "Drive":
            self.lineEdit.setText(self.Quick_access[6:]+"\\")
            os.chdir(self.Quick_access[6:]+"\\")
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(
                            self.Quick_access[5:] + "\\" + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(
                            str(os.path.getsize(self.Quick_access[6:]+"\\" + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(
                            self.Quick_access[5:]+"\\" + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")
    def new_folder(self):
        try:
            newtext, ok = QtWidgets.QInputDialog.getText( self.centralwidget,'Text Input Dialog', 'Enter your name:')
            if ok:
                current_address2=os.getcwd()
                current_address2=current_address2+'/'+newtext
                os.makedirs(current_address2)
                # print(os.listdir())
                self.refresh()
        except:
            pass
    def copy_file(self):
        try:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
            destination, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog', 'Enter your destination address:')
            source=file_name+file_extension
            source_list=source.split('\\')
            file_name_paste=source_list[len(source_list)-1]
            destination=destination + '\\' + file_name_paste
            if ok:
                if file_extension=='':
                    shutil.copytree(source, destination)
                    self.refresh()
                else:
                    shutil.copyfile(source, destination)
                    self.refresh()
        except:
            pass
    def delete(self):
        try:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
            if file_extension=='':
                shutil.rmtree(file_name+file_extension)
                self.refresh()
            else:
                os.remove(file_name+file_extension)
                self.refresh()
        except:
            pass
    def cut(self):
        try:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
            destination, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog','Enter your destination address:')
            source = file_name + file_extension
            source_list = source.split('\\')
            file_name_paste = source_list[len(source_list) - 1]
            destination = destination + '\\' + file_name_paste
            if ok:
                if file_extension=='':
                    shutil.copytree(source, destination)
                    self.refresh()
                else:
                    shutil.copyfile(source, destination)
                    self.refresh()
            if file_extension=='':
                shutil.rmtree(file_name+file_extension)
                self.refresh()
            else:
                os.remove(file_name+file_extension)
                self.refresh()
        except:
            pass
    def rename(self):
        try:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
            new_name, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog','Enter a name:')
            old = file_name+file_extension
            old_list = old.split('\\')
            new_list = old_list[:len(old_list)-1]
            if new_list[len(new_list)-1]=='':
                new_list.pop()
            new='\\'.join(new_list)
            new = new+"\\"+new_name+file_extension
            if ok:
                os.rename(old,new)
                self.refresh()
        except:
            pass


    def refresh(self):
        if self.lineEdit.text() != "":
            in_directory = os.listdir()
            in_directory = in_directory[::-1]
            self.tableWidget.setRowCount(len(in_directory))
            for i in range(len(in_directory)):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    if j == 0:
                        item.setText(str(in_directory[i]))
                        file_name, file_extension = os.path.splitext(self.lineEdit.text() + '\\' + in_directory[i])
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
                        elif file_extension == '.mp3' or file_extension == ".wmv":
                            item.setIcon(self.icon_music)
                        else:
                            item.setIcon(self.icon_unknown)
                    if j == 2:
                        item.setText(str(os.path.getsize(self.lineEdit.text() + '\\' + in_directory[i]) / (1024 ** 2)))
                    if j == 1:
                        file_name3, file_extension3 = os.path.splitext(self.lineEdit.text() + '\\' + in_directory[i])
                        if file_extension3 != "":
                            item.setText(file_extension3[1:])
                        else:
                            item.setText("folder")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

