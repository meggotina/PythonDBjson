import os
import time
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response code to 200 (OK)
        self.send_response(200)
        # Set the content type to JSON
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Open the JSON file in the specified folder
        with open("D:\DataBaseJson\data.json", "r") as f:
            # Read the contents of the file
            data = json.load(f)
            # Convert the data to a pretty-printed JSON string
            json_data = json.dumps(data, indent=4)
            # Send the data to the client
            self.wfile.write(json_data.encode())

# Create the server
server = HTTPServer(("localhost", 8000), JSONHandler)

# Start the server
server.serve_forever()