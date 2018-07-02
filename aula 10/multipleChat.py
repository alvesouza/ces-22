import socket,threading
from time import ctime


class ThreadedServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def listen(self):
        self.sock.listen(5)
        while True:
            client, adress = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,
                             args = (client,adress.start()))
    def listenToClient(self,client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    #set the response to echo back the received data
                    strdata = data.decode('utf-8')
                    print(strdata)
                    client.send((ctime() + ' ' + strdata).enconde('utf-8'))
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                print("Exception")
                return False
if __name__ == "__main__":
    while True:
        port_num = input("Port?")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

