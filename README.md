# RPC Client-Server System (Python)

## Project Description
This project implements a simple Remote Procedure Call (RPC) system using Python.
The system consists of a client and a server running on separate Amazon EC2 instances.
The client sends a remote request to the server, the server executes the requested
procedure, and returns the result to the client.

## System Architecture
The system follows a client-server architecture:
- The RPC server runs on an EC2 instance and listens for incoming TCP connections.
- The RPC client runs on another EC2 instance and communicates with the server over TCP.
- Requests and responses are serialized using JSON format.

## Implementation Details
- Programming language: Python 3
- Communication protocol: TCP sockets
- Data serialization: JSON
- Remote method implemented: `add(a, b)`
- Failure handling: timeout and retry mechanism on the client side


Failure handling is demonstrated by intentionally delaying the server response.
The client is configured with a shorter timeout value, which causes request timeouts.
When a timeout occurs, the client retries the request instead of terminating.
This demonstrates at-least-once RPC semantics.

The project demonstrates a working RPC system with basic fault tolerance.
The implementation confirms correct remote communication, request handling,
and failure recovery in a distributed environment.
