from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # HTTP status
        self.send_header("Content-type", "text/html")  # use text/html instead of text/plain
        self.end_headers()

        html = """
        <html>
            <head>
                <title>Hello Page</title>
            </head>
            <body>
                <p>Hello from tarik!</p>
                <br>
                <p>Testiing from scratch</p>
            </body>
        </html>
        """

        self.wfile.write(html.encode('utf-8'))

# Run server
server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
