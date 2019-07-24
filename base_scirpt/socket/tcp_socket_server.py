import socket
import logging
import threading
import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)s %(thread)d %(message)s")
#在pycharm里执行quit退出，出现报错：OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。未解决，但是不影响功能，作为一个bug后续修复



class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9998):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accept).start()

    def accept(self):
        while not self.event.is_set():
            sock, client = self.sock.accept()
            f = sock.makefile('rw')
            self.clients[client] = f
            threading.Thread(target=self.recv, args=(f, client),name='recv').start()

    def recv(self, f, client):
        while not self.event.is_set():
            try:
                data = f.readline()
            except Exception as e:
                logging.error(e)
                data='quit'
            msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *client,data)
            msg = data.strip()
            if msg == 'quit':
                self.clients.pop(client)
                f.close()
                logging.info('{} quits'.format(client))
                break
            logging.info(msg)
            for s in self.clients.values():
                s.write(msg)
                s.flush()

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()

def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            cs.stop()
            print('===================')
            threading.Event().wait(3)
            print('+++++++++++++++++++')
            break
        logging.info(threading.enumerate())

if __name__ == '__main__':
    main()


