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

    def do_POST(self):
        # Set the response code to 201 (Created)
        self.send_response(201)
        # Set the content type to JSON
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Read the request body
        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode()
        # Parse the request body as JSON
        data = json.loads(request_body)

        # Open the JSON file in the specified folder
        with open("/path/to/folder/file.json", "r") as f:
            # Read the contents of the file
            objects = json.load(f)
            # Append the new data to the list of objects
            objects.append(data)
        # Open the file in write mode
        with open("/path/to/folder/file.json", "w") as f:
            # Write the updated list of objects to the file
            json.dump(objects, f, indent=4)


# Create the server
server = HTTPServer(("localhost", 8000), JSONHandler)

# Start the server
server.serve_forever()
