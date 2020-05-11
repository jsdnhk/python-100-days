"""
使用socketserver模塊創建時間服務器

Version: 0.1
Author: 駱昊
Date: 2018-03-22
"""
from socketserver import TCPServer, StreamRequestHandler
from time import *


class EchoRequestHandler(StreamRequestHandler):

    def handle(self):
        currtime = localtime(time())
        timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
        self.wfile.write(timestr.encode('utf-8'))


server = TCPServer(('localhost', 6789), EchoRequestHandler)
server.serve_forever()
