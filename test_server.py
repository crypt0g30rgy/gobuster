from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"UA: {self.headers.get('User-Agent')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(('127.0.0.1', port), RequestHandler)
    print(f"Starting server on port {port}")
    server.serve_forever()
