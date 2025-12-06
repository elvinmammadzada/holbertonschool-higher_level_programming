#!/usr/bin/python3
"""Restful API basic"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
"""Web app for sending jsons"""
PORT = 8000
dict = {"name": "John", "age": 30, "city": "New York"}
dict_info = {"version": "1.0", "description": "A simple API built with http.server"}


class MyServer(BaseHTTPRequestHandler):
    """Creating my server"""

    def do_GET(self):
        """Do get for handling endpoints"""
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dict).encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dict_info).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

server = HTTPServer(("localhost", PORT), MyServer)
server.serve_forever()
