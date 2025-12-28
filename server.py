import socket
import json
import time

def add(a, b):
    return a + b

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("RPC Server running on port 5000")

while True:
    conn, addr = server.accept()
    print("Client connected:", addr)

    data = conn.recv(1024).decode()
    request = json.loads(data)
    print("Request:", request)

    time.sleep(5)

    if request["method"] == "add":
        result = add(
            request["params"]["a"],
            request["params"]["b"]
        )
        response = {
            "request_id": request["request_id"],
            "result": result,
            "status": "OK"
        }
    else:
        response = {
            "request_id": request["request_id"],
            "status": "ERROR"
        }

    conn.send(json.dumps(response).encode())
    conn.close()
