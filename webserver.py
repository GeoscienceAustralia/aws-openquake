#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer
from datetime import datetime
import json

data = {'done': 0, 'logs': []}
class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        json.dump(data, self.wfile)


    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        body = self.rfile.read(length)
        data['logs'].append({'time': str(datetime.now()), 'msg': body})

        if self.path == '/done':
            data['done'] = 1

        self.send_response(200)
        self.end_headers()


server = SocketServer.TCPServer(('0.0.0.0', 8080), HTTPRequestHandler, bind_and_activate=True)
server.allow_reuse_address = True
server.serve_forever()
