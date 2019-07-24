import threading
from socketserver import ThreadingTCPServer,BaseRequestHandler
import sys
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

class ChatHandler(BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.request

    def finish(self):
        super().finish()
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):
        super().handle()

        while not self.event.is_set():
            data = self.request.recv(1024).decode()
            print(data,'~~~~~~~~~~~~~~~~~')
            if not data or data == 'quit': #客户端主动断开，收到的data为空，空data也要进行判断
                break
            msg = "{} {}".format(self.client_address,data).encode()
            logging.info(msg)
            for c in self.clients.values():
                print('++++++++++++++++++')
                self.request.send(msg)
        print('the end')

addr = ('127.0.0.1',9999)
server = ThreadingTCPServer(addr,ChatHandler)

server_thread = threading.Thread(target=server.serve_forever,name='ChatServer',daemon=True)
server_thread.start()

try:
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            break
        print(threading.enumerate())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    pass
finally:
    print('Exit')
    sys.exit(0)
