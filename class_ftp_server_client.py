from socket import AF_INET, socket, SOCK_STREAM
import os,shutil
from threading import Thread
import time
class server:
    def __init__(self,host,port):
        self.host = str(host)
        self.port = int(port)
        self.addr =(str(host),int(port))
        self.SERVER = None
        self.client = None
        self.client_address = None
        self.bufsiz = 8192
    def start(self):
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.addr)
        self.SERVER.listen(5)
        print("Waiting for connection...")
        self.accept_incoming_connections()
        self.SERVER.close()
    def accept_incoming_connections(self):
        while True:
            self.client, self.client_address = self.SERVER.accept()
            print("%s:%s has connected." % self.client_address)
    def send_text(self,text):
        self.client.send(text.encode("utf8"))
    def receive_text(self):
        received_text = self.client.recv(self.bufsiz).decode("utf8")
        return received_text

class client:
    def __init__(self,host,port):
        self.host = str(host)
        self.port = int(port)
        self.addr = (str(host),int(port))
        self.bufsiz = 8192
        self.client_socket = None
    def start(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.addr)
        self.send_text(str([ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]))
        while 1:
            x = self.receive_text()
            #####################################NEW FOLDER###################################
            if x[len(x)-10:len(x)] == "NEW FOLDER":
                x = x.split("#")
                os.makedirs(x[0])
            #####################################NEW FOLDER###################################
            #####################################COPY#########################################
            elif x[len(x)-4:len(x)] == "COPY":
                x = x.split("#")
                if x[2] == '':
                    Thread(target=shutil.copytree,args=(x[0], x[1],)).start()
                else:
                    Thread(target=shutil.copyfile,args=(x[0], x[1],)).start()
            #####################################COPY#########################################
            #####################################REFRESH######################################
            elif x[len(x)-7:len(x)] == "refresh":
                x = x.split()
                y = x[0]
                for i in range(1,len(x)-1):
                    y+=str(" "+x[i])

                self.send_text(os.listdir(y))
            #####################################REFRESH#######################################
            ######################################delete#######################################
            elif x[len(x)-6:len(x)] == "DELETE":
                x = x.split()
                y = x[0]
                for i in range(1, len(x) - 1):
                    y += str(" " + x[i])
                file_name, file_extension = os.path.splitext(y)
                try:
                    if file_extension == '':
                        shutil.rmtree(file_name + file_extension)
                    else:
                        os.remove(file_name + file_extension)
                except:
                    pass
                ##########################################################download#############################
            elif x[len(x) - 8:len(x)] == "download":
                x = x.split("#")[0]
                download_size = str(os.path.getsize(x))
                # print(download_size)
                self.send_text(download_size)
            ###############################################delete################################

            elif x == "BACKWARD":
                os.chdir("..")
                a = os.listdir()
