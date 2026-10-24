#!/usr/bin/python3
"""A simple API using Python's http.server module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests for the simple API"""

    def do_GET(self):
        """Handle GET requests for different endpoints"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header(
                "Content-Type", "application/json"
            )
            self.end_headers()
            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header(
                "Content-Type", "application/json"
            )
            self.end_headers()
            self.wfile.write(
                json.dumps(info).encode("utf-8")
            )

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, APIHandler)

    print("Server running on port 8000...")
    httpd.serve_forever()