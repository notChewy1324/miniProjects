from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.close_request()
    print("Server Stopped")