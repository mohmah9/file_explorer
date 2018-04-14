from socket import AF_INET, socket, SOCK_STREAM

from threading import Thread

import tkinter




def receive():

    """Handles receiving of messages."""

    while True:

        try:

            msg = client_socket.recv(BUFSIZ).decode("utf8")

            msg_list.insert(tkinter.END, msg)

        except OSError:  # Possibly client has left the chat.

            break





def send(event=None):  # event is passed by binders.

    """Handles sending of messages."""

    msg = my_msg.get()

    my_msg.set("")  # Clears input field.

    client_socket.send(bytes(msg, "utf8"))

    if msg == "{quit}":

        client_socket.close()

        top.quit()





def on_closing(event=None):

    """This function is to be called when the window is closed."""

    my_msg.set("{quit}")

    send()



top = tkinter.Tk()
top.title("Pro File Manager Chat")

