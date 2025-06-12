#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer

class Api_Get(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")

host = "localhost"
port = 8000
server = (host, port)

httpd = HTTPServer(server, Api_Get)
