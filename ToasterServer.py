import socket


if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocket.bind(('localhost',4004))
    serversocket.listen(1)
    (clientsocket,address) = serversocket.accept()
    print str(address)+" has connected"
    clientsocket.send("You've connected to The Toaster!\n")
    while 1:
        recv_statement = clientsocket.recv(256).strip()
        print recv_statement
	if 'changeState' in recv_statement:
	    clientsocket.send('0\n')
	else:
	    clientsocket.send('1\n')
