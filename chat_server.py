from socket import AF_INET, socket, SOCK_STREAM

from threading import Thread







def accept_incoming_connections():
    """Sets up handling for incoming clients."""

    while True:
        client, client_address = SERVER.accept()

        print("%s:%s has connected." % client_address)

        client.send(bytes("Welcome to Pro File Manager chat! :) ", "utf8"))

        addresses[client] = client_address

        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.

    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")

    welcome = 'Welcome %s!, type {quit} to exit.' % name

    client.send(bytes(welcome, "utf8"))

    msg = "%s has joined the chat!" % name

    broadcast(bytes(msg, "utf8"))

    clients[client] = name
    while True:

        msg = client.recv(BUFSIZ)

        if msg != bytes("{quit}", "utf8"):

            broadcast(msg, name + ": ")
