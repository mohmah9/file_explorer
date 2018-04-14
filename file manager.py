
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QInputDialog, QLineEdit,QAbstractItemView,QMessageBox
import shutil,os,threading,time
from socket import AF_INET, socket, SOCK_STREAM,gethostbyname,gethostname
from class_ftp_server_client import server
from class_ftp_server_client import client
from class_ftp_server_client import download_client
from class_ftp_server_client import download_server
ftp_counter = 0

class Ui_MainWindow(object):
    def __init__(self):
        self.host = ""
        self.file_name = ""
        self.icon_folder = QtGui.QIcon()
        self.icon_folder.addPixmap(QtGui.QPixmap("icons\\folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_exe = QtGui.QIcon()
        self.icon_exe.addPixmap(QtGui.QPixmap("icons\\exe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pdf = QtGui.QIcon()
        self.icon_pdf.addPixmap(QtGui.QPixmap("icons\\pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_txt = QtGui.QIcon()
        self.icon_txt.addPixmap(QtGui.QPixmap("icons\\txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_msi = QtGui.QIcon()
        self.icon_msi.addPixmap(QtGui.QPixmap("icons\\msi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_image = QtGui.QIcon()
        self.icon_image.addPixmap(QtGui.QPixmap("icons\\picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_settings = QtGui.QIcon()
        self.icon_settings.addPixmap(QtGui.QPixmap("icons\\settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_rar = QtGui.QIcon()
        self.icon_rar.addPixmap(QtGui.QPixmap("icons\\rar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_video = QtGui.QIcon()
        self.icon_video.addPixmap(QtGui.QPixmap("icons\\video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_unknown = QtGui.QIcon()
        self.icon_unknown.addPixmap(QtGui.QPixmap('icons\\unknown.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_music = QtGui.QIcon()
        self.icon_music.addPixmap(QtGui.QPixmap('icons\\music.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_desktop = QtGui.QIcon()
        self.icon_desktop.addPixmap(QtGui.QPixmap('icons\\desktop.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_download = QtGui.QIcon()
        self.icon_download.addPixmap(QtGui.QPixmap('icons\\download.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pictures = QtGui.QIcon()
        self.icon_pictures.addPixmap(QtGui.QPixmap('icons\\pictures.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_musics = QtGui.QIcon()
        self.icon_musics.addPixmap(QtGui.QPixmap('icons\\musics.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_videos = QtGui.QIcon()
        self.icon_videos.addPixmap(QtGui.QPixmap('icons\\videos.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_documents = QtGui.QIcon()
        self.icon_documents.addPixmap(QtGui.QPixmap('icons\\documents.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_drives = QtGui.QIcon()
        self.icon_drives.addPixmap(QtGui.QPixmap('icons\\drives.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_window_icon = QtGui.QIcon()
        self.main_window_icon.addPixmap(QtGui.QPixmap('icons\\main_icon.jpg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_back = QtGui.QIcon()
        self.icon_back.addPixmap(QtGui.QPixmap('icons\\back.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_go = QtGui.QIcon()
        self.icon_go.addPixmap(QtGui.QPixmap('icons\\go.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_copy = QtGui.QIcon()
        self.icon_copy.addPixmap(QtGui.QPixmap('icons\\copy.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_cut = QtGui.QIcon()
        self.icon_cut.addPixmap(QtGui.QPixmap('icons\\cut.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_new_folder = QtGui.QIcon()
        self.icon_new_folder.addPixmap(QtGui.QPixmap('icons\\new_folder.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_rename = QtGui.QIcon()
        self.icon_rename.addPixmap(QtGui.QPixmap('icons\\rename.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_delete = QtGui.QIcon()
        self.icon_delete.addPixmap(QtGui.QPixmap('icons\\delete.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drive_list =[ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
        self.Quick_access = ""
        self.logo_icon = QtGui.QIcon()
        self.logo_icon.addPixmap(QtGui.QPixmap('icons\\logo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_chat = QtGui.QIcon()
        self.icon_chat.addPixmap(QtGui.QPixmap('icons\\chat.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_ftp = QtGui.QIcon()
        self.icon_ftp.addPixmap(QtGui.QPixmap('icons\\ftp.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)




    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 800)
        MainWindow.setWindowIcon(self.main_window_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GoButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoButton.setGeometry(QtCore.QRect(1225, 88, 31, 31))
        self.GoButton.setObjectName("pushButton")
        self.GoButton.setFlat(True)
        self.GoButton.setIcon(self.icon_go)
        self.GoButton.setIconSize(QtCore.QSize(30,30))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 120, 1050, 655))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
        x = 2
        for drive in self.drive_list:
            item = QtWidgets.QTableWidgetItem()
            item.setText("Drive" + " "+str(drive))
            item.setIcon(self.icon_drives)
            self.tableWidget2.setItem(4+x, 0, item)
            x+=1
        self.tableWidget2.verticalHeader().setVisible(False)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 95, 695, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(485, 88, 31, 31))
        self.back_button.setObjectName("Back")
        self.back_button.setIcon(self.icon_back)
        self.back_button.setIconSize(QtCore.QSize(30,30))
        self.back_button.setFlat(True)

        self.chat_button = QtWidgets.QPushButton(self.centralwidget)
        self.chat_button.setGeometry(QtCore.QRect(1027, 12, 78, 78))
        self.chat_button.setObjectName("Back")
        self.chat_button.setIcon(self.icon_chat)
        self.chat_button.setIconSize(QtCore.QSize(50, 50))
        self.chat_button.setFlat(False)

        self.ftp_button = QtWidgets.QPushButton(self.centralwidget)
        self.ftp_button.setGeometry(QtCore.QRect(1105, 12, 78, 78))
        self.ftp_button.setObjectName("Back")
        self.ftp_button.setIcon(self.icon_ftp)
        self.ftp_button.setIconSize(QtCore.QSize(65, 65))
        self.ftp_button.setFlat(False)

        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(1183, 12, 78, 78))
        self.download_button.setObjectName("Back")
        self.download_button.setIcon(self.icon_download)
        self.download_button.setIconSize(QtCore.QSize(65, 65))
        self.download_button.setFlat(False)





        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 85, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 7, 20, 88))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(460, 7, 20, 88))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(365, 7, 20, 88))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(278, 7, 20, 88))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(185, 7, 20, 88))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(91, 7, 20, 88))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.pushButton.setText("")
        self.pushButton.setIcon(self.icon_new_folder)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("new_folder")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 81, 81))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(self.icon_copy)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("copy")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 10, 81, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(self.icon_cut)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("cut")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 10, 81, 81))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(self.icon_delete)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("delete")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 10, 81, 81))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(self.icon_rename)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("rename")

        self.progressBar = QtWidgets.QProgressBar(MainWindow)
        self.progressBar.setGeometry(QtCore.QRect(10, 123, 460,22 ))
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setProperty("value", 0)





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
        self.chat_button.clicked.connect(self.chat)
        self.actionNew_folder.triggered.connect(self.new_folder)
        self.actionCopy.triggered.connect(self.copy_file)
        self.actionCut.triggered.connect(self.cut)
        self.actionDelete.triggered.connect(self.delete)
        self.actionRename.triggered.connect(self.rename)
        self.ftp_button.clicked.connect(self.ftp)
        self.download_button.clicked.connect(self.download_Button)
        global ftp_flag
        ftp_flag = False
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
            in_directory = os.listdir(self.lineEdit.text())
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
        global ftp_counter
        global ftp_server
        second_item = self.tableWidget.currentRow()
        client_format = self.tableWidget.item(second_item, 1).text()
        if client_format[len(client_format)-1] != "2":
            try:
                r = self.tableWidget.currentRow()
                self.file_name = self.tableWidget.item(r,0).text()
                file_name2 , file_extension2 = os.path.splitext(self.lineEdit.text() + "\\"+self.file_name)
                if file_extension2 == "":
                    if len(self.file_name) == 2:
                        next_address = self.file_name+ '\\'
                    else:
                        current_address = self.lineEdit.text()
                        next_address = current_address +"\\" + self.file_name
                    self.lineEdit.setText(next_address)
                    in_directory = os.listdir(next_address)
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

        else:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + '\\' + self.file_name)
            if file_extension == "":
                ftp_counter+=1
                r = self.tableWidget.currentRow()
                self.file_name = self.tableWidget.item(r, 0).text()
                if len(self.file_name) == 2:
                    self.lineEdit.setText(str(self.file_name+ '\\'))
                elif self.lineEdit.text()!="":
                    self.lineEdit.setText(str(self.lineEdit.text()+"\\"+self.file_name))
                else:
                    self.lineEdit.setText(str(self.file_name))

                if ftp_server.client != None:
                    ftp_server.send_text(self.file_name)
                    in_directory = ftp_server.receive_text()
                    in_directory = eval(in_directory)
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
                            if j == 1:
                                item.setText(
                                    str("connected pc 2"))

            else:
                threading.Thread(target=self.download).start()


    def Back_button(self):
        global ftp_server
        global ftp_counter
        if ftp_counter<0:
            ftp_counter=0
        if ftp_counter == 0:
            if self.lineEdit.text()!= "":
                current_address = self.lineEdit.text()
                current_address_list = current_address.split("\\")
                if len(current_address_list) > 2:
                    back_address = current_address_list[:len(current_address_list)-1]
                    back_address = "\\".join(back_address)
                    self.lineEdit.setText(back_address)
                    try:
                        self.tableWidget.setRowCount(0)
                        in_directory = os.listdir(back_address)
                        in_directory = in_directory[::-1]
                        self.tableWidget.setRowCount(len(in_directory))
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
                    self.lineEdit.setText(back_address)
                    try:
                        self.tableWidget.setRowCount(0)
                        in_directory = os.listdir(back_address)
                        in_directory = in_directory[::-1]
                        self.tableWidget.setRowCount(len(in_directory))
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
                    if ftp_flag==True and ftp_server.client != None:
                        back_address = ""
                        self.lineEdit.setText(back_address)

                        self.tableWidget.setRowCount(len(drives_list) + len(self.drive_list) + 1)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText("connected PC")
                        self.tableWidget.setItem(len(self.drive_list), 0, item)
                        v = len(self.drive_list) + 1
                        for i in range(len(drives_list)):
                            item = QtWidgets.QTableWidgetItem()
                            item.setIcon(self.icon_drives)
                            item.setText(drives_list[i])
                            self.tableWidget.setItem(v, 0, item)
                            v += 1
                        b = len(self.drive_list) + 1

                        for j in range(len(drives_list)):
                            item = QtWidgets.QTableWidgetItem()
                            item.setText("Drive2")
                            self.tableWidget.setItem(b, 1, item)
                            b += 1
                        for i in range(len(self.drive_list)):
                            for j in range(3):
                                item = QtWidgets.QTableWidgetItem()
                                self.tableWidget.setItem(i, j, item)
                                if j == 0:
                                    item.setText(str(self.drive_list[i]))
                                    item.setIcon(self.icon_drives)
                                if j == 1:
                                    item.setText("Drive")
                    else:
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


        if ftp_counter<0:
            ftp_counter=0
        if ftp_counter != 0:
            ftp_counter -= 1
            current_address = self.lineEdit.text()
            current_address_list = current_address.split("\\")
            if len(current_address_list) > 2:
                back_address = current_address_list[:len(current_address_list) - 1]
                back_address = "\\".join(back_address)
                self.lineEdit.setText(back_address)
            if len(current_address_list) == 2 and current_address_list[len(current_address_list) - 1] != '':
                back_address = current_address_list[0] + "\\"
                self.lineEdit.setText(back_address)
            ftp_server.send_text("BACKWARD")
            in_directory = ftp_server.receive_text()
            in_directory = eval(in_directory)
            self.tableWidget.setRowCount(len(in_directory))
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
                    if j == 1:
                        item.setText("connected pc 2")
            if len(current_address_list) == 2 and current_address_list[len(current_address_list) - 1] == '':
                back_address = ""
                self.lineEdit.setText(back_address)


                self.tableWidget.setRowCount(len(drives_list) + len(self.drive_list) + 1)
                item = QtWidgets.QTableWidgetItem()
                item.setText("connected PC")
                self.tableWidget.setItem(len(self.drive_list), 0, item)
                v = len(self.drive_list) + 1
                for i in range(len(drives_list)):
                    item = QtWidgets.QTableWidgetItem()
                    item.setIcon(self.icon_drives)
                    item.setText(drives_list[i])
                    self.tableWidget.setItem(v, 0, item)
                    v += 1
                b = len(self.drive_list) + 1

                for j in range(len(drives_list)):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText("Drive2")
                    self.tableWidget.setItem(b, 1, item)
                    b += 1
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Desktop')
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Downloads')
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Pictures')
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Documents')
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Music')
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
            in_directory = os.listdir("C:\\Users\\"+str(os.getlogin())+'\\Videos')
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
            in_directory = os.listdir(self.Quick_access[6:]+"\\")
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
        global ftp_counter
        global ftp_server
        if ftp_counter<0:
            ftp_counter=0
        if ftp_counter == 0:
            try:
                newtext, ok = QtWidgets.QInputDialog.getText( self.centralwidget,'Text Input Dialog', 'Enter your new folder name:')
                if ok:
                    current_address2=self.lineEdit.text()
                    current_address2=current_address2+'/'+newtext
                    os.makedirs(current_address2)
                    self.refresh()
            except:
                pass
        else:
            newtext, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog',
                                                         'Enter your new folder name:')
            if ok:
                current_address2 = self.lineEdit.text()
                current_address2 = current_address2 + '/' + newtext
                ftp_server.send_text(current_address2+"#"+"NEW FOLDER")
                time.sleep(0.5)
                self.ftp_refresh()
    def copy_thread(self):
        if file_extension == '':
            threading.Thread(target=self.progress_bar_dir).start()
            shutil.copytree(source, destination)
            self.refresh()
        else:
            threading.Thread(target=self.progress_bar_file).start()
            shutil.copyfile(source, destination)
            self.refresh()
    def copy_file(self):
        global ftp_counter
        global ftp_server
        global file_name, file_extension, destination, source
        if ftp_counter < 0:
            ftp_counter=0
        if ftp_counter == 0:
            try:
                r = self.tableWidget.currentRow()
                self.file_name = self.tableWidget.item(r, 0).text()
                file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
                destination, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog',
                                                                 'Enter your destination address:')
                source = file_name + file_extension
                source_list = source.split('\\')
                file_name_paste = source_list[len(source_list) - 1]
                destination = destination + '\\' + file_name_paste
                if ok:
                    threading.Thread(target=self.copy_thread).start()
            except:
                pass
        else:
            r = self.tableWidget.currentRow()
            self.file_name = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
            destination, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Text Input Dialog','Enter your destination address:')
            source = file_name + file_extension
            source_list = source.split('\\')
            file_name_paste = source_list[len(source_list) - 1]
            destination = destination + '\\' + file_name_paste
            if ok:
                ftp_server.send_text(str(source+"#"+destination+"#"+file_extension+"#"+"COPY"))

    def progress_bar_file(self):
        time.sleep(0.5)
        total_size=os.path.getsize(source)
        paste_size=0
        while not total_size == paste_size:
            time.sleep(0.5)
            paste_size=os.path.getsize(destination)
            percent=(paste_size/total_size)*100
            self.progressBar.setProperty("value", percent)
        percent = 0
        self.progressBar.setProperty("value", percent)

    def progress_bar_dir(self):
        time.sleep(0.5)
        folder_size = 0
        for (path, dirs, files) in os.walk(source):
            for file in files:
                filename = os.path.join(path, file)
                folder_size += os.path.getsize(filename)
        total_size=folder_size
        paste_size=0
        while not total_size==paste_size:
            time.sleep(0.5)
            folder_size = 0
            for (path, dirs, files) in os.walk(destination):
                for file in files:
                    filename = os.path.join(path, file)
                    folder_size += os.path.getsize(filename)
            paste_size = folder_size
            percent=(paste_size/total_size)*100
            self.progressBar.setProperty("value", percent)
        percent = 0
        self.progressBar.setProperty("value", percent)
    def progress_bar_download(self):
        time.sleep(0.2)
        total_size = int(download_size)
        print(total_size)
        paste_size =0
        print(file_name+file_extension)
        addr=file_name+file_extension
        destination=(addr).split('\\')
        destination=destination[len(destination)-1]
        print(destination)
        while not total_size == paste_size:
            time.sleep(0.1)
            paste_size=int(os.path.getsize(destination))
            percent=(paste_size/total_size)*100
            self.progressBar.setProperty("value", percent)
        percent = 100
        self.progressBar.setProperty("value", percent)
        time.sleep(1)
        percent = 0
        self.progressBar.setProperty("value", percent)


    def delete(self):
        global ftp_server
        global ftp_counter
        if ftp_counter <0:
            ftp_counter = 0
        if ftp_counter != 0:
            r = self.tableWidget.currentRow()
            file_name2 = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + file_name2)
            send = str(file_name+file_extension +" " +"DELETE")
            ftp_server.send_text(send)
            time.sleep(0.5)
            self.ftp_refresh()
        else:
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
        global source , destination ,file_name , file_extension
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
                    threading.Thread(target=self.progress_bar_dir).start()
                    shutil.copytree(source, destination)
                    self.refresh()
                else:
                    threading.Thread(target=self.progress_bar_file).start()
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
            in_directory = os.listdir(self.lineEdit.text())
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


    def chat(self):
        newtext, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Make server or not','Do you want to make a server? yes/no')
        if ok:
            if newtext == "yes" or newtext == "Yes" or newtext == "y":
                host_ip = open('chatHostPort.txt', 'w')
                host_ip.write(str("127.0.0.1" + " "))
                host_ip.write(str(33000))
                host_ip.close()
                server = threading.Thread(target=make_chat_server)
                client = threading.Thread(target=make_chat_client)
                server.start()
                client.start()
            if newtext == "no" or newtext == "No" or newtext == "n":
                Host, ok1 = QtWidgets.QInputDialog.getText(self.centralwidget, 'Host',
                                                           'Enter Host address:')
                Port, ok2 = 33000, True

                # making a text file that has the host and ip address
                if ok1 and ok2:
                    host_ip = open('chatHostPort.txt', 'w')
                    host_ip.write(str(Host + " "))
                    host_ip.write(str(Port))
                    host_ip.close()
                # making a text file that has the host and ip address
                client = threading.Thread(target=make_chat_client)
                client.start()

    def ftp(self):
        global ftp_server
        global ftp_client
        global ftp_server2
        global ftp_client2
        global drives_list
        global ftp_flag
        text,ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'Make server or not','Do you want to make a server? yes/no')
        if ok:
            if text == "yes" or text == "Yes" or text == "y":
                Host, ok1 = "0.0.0.0", True
                Port, ok2 = 32000, True
                ftp_server = server(str(Host),Port)
                threading.Thread(target=ftp_server.start).start()


                ftp_server2 = download_server("0.0.0.0", 35000)
                threading.Thread(target=ftp_server2.start).start()

                self.message_box_wait()
                while 1:
                    if ftp_server.client !=None:
                        ftp_flag=True
                        drives_list = ftp_server.receive_text()
                        drives_list = eval(drives_list)
                        self.tableWidget.setRowCount(len(drives_list)+len(self.drive_list)+1)
                        item = QtWidgets.QTableWidgetItem()
                        item.setText("connected PC")
                        self.tableWidget.setItem(len(self.drive_list),0,item)
                        v = len(self.drive_list)+1
                        for i in range(len(drives_list)):
                            item = QtWidgets.QTableWidgetItem()
                            item.setIcon(self.icon_drives)
                            item.setText(drives_list[i])
                            self.tableWidget.setItem(v,0,item)
                            v+=1
                        b = len(self.drive_list)+1
                        for j in range(len(drives_list)):
                            item = QtWidgets.QTableWidgetItem()
                            item.setText("Drive2")
                            self.tableWidget.setItem(b, 1,item)
                            b+=1


                        break



            if text == "no" or text == "No" or text == "n":
                global Host123
                self.host, ok1 = QtWidgets.QInputDialog.getText(self.centralwidget, 'Host',
                                                           'Enter Host address:')
                Port, ok2 = 32000, True
                if ok1:
                    ftp_client = client(str(self.host),Port)
                    threading.Thread(target=ftp_client.start).start()
                    ftp_client2 = download_client(str(self.host), 35000)
                    threading.Thread(target=ftp_client2.start).start()
    def ftp_refresh(self):
        global ftp_server
        send = str(self.lineEdit.text()+" refresh")
        ftp_server.send_text(send)
        in_directory = ftp_server.receive_text()
        in_directory = eval(in_directory)
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
    def download(self):
        global ftp_client
        global ftp_counter
        global ftp_server
        global ftp_server2
        global download_size , file_name , file_extension
        if ftp_counter<0:
            ftp_counter=0
        if ftp_counter != 0:

            r = self.tableWidget.currentRow()
            file_name_download = self.tableWidget.item(r, 0).text()
            file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + file_name_download)
            saved_name = file_name.split("\\")
            saved_name = saved_name[len(saved_name)-1]
            if file_extension != "":
                while True:
                    if ftp_server2.client != None:
                        break
                ftp_server.send_text(file_name+file_extension+'#download')
                download_size=ftp_server.receive_text()
                threading.Thread(target=self.progress_bar_download).start()
                ftp_server2.send_text(file_name+file_extension+"#DOWNLOAD")
                ftp_server2.receive_file(saved_name+file_extension)
    def download_Button(self):
        global ftp_counter
        r = self.tableWidget.currentRow()
        self.file_name = self.tableWidget.item(r, 0).text()
        file_name, file_extension = os.path.splitext(self.lineEdit.text() + "\\" + self.file_name)
        if ftp_counter<0:
            ftp_counter=0
        if ftp_counter != 0 and file_extension!="":

            threading.Thread(target=self.download).start()
    def message_box_wait(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("click ok when the client is connected. ")
        msg.setWindowTitle("please wait...")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        print("value of pressed message box button:", retval)

def make_chat_client():
        import chat_client
def make_chat_server():
        import chat_server
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
