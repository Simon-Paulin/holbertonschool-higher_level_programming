#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Api_Get(BaseHTTPRequestHandler):
    def do_GET(self):
        call = {
            "/": self.root,
            "/data": self.data,
            "/status": self.status,
            "/info": self.info,
        }
        handle = call.get(self.path, self.not_found)
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
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def not_found(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

    def info(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        return_info = {
            "version": "1.0", "description":
            "A simple API built with http.server"
            }
        self.wfile.write(json.dumps(return_info).encode("utf-8"))



host = "localhost"
port = 8000
server = (host, port)

httpd = HTTPServer(server, Api_Get)
httpd.serve_forever()
