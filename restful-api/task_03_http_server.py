#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Api_Get(BaseHTTPRequestHandler):
    def do_GET(self):
        call = {
            "/": self.root,
            "/data": self.data,
            "/status": self.status
        }
        handle = call.get(self.path)
        handle()

    def root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def data(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        data_js = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(data_js).encode("utf-8"))

    def status(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Status 404")

host = "localhost"
port = 8000
server = (host, port)

httpd = HTTPServer(server, Api_Get)
httpd.serve_forever()
