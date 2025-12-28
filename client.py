import socket
import json
import uuid

SERVER_IP = "18.215.179.48"
PORT = 5000
TIMEOUT = 2
RETRIES = 3

request = {
    "request_id": str(uuid.uuid4()),
    "method": "add",
    "params": {"a": 5, "b": 7}
}

for attempt in range(RETRIES):
    try:
        print(f"Attempt {attempt + 1}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((SERVER_IP, PORT))
        sock.send(json.dumps(request).encode())

        response = sock.recv(1024).decode()
        print("Response:", response)
        break

    except socket.timeout:
        print("Timeout → retry")

    finally:
        sock.close()
