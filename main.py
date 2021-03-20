
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(7)
host = input("Enter the I.P that you Want to Scan:")
port = int(input("Enter the port number:"))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("the port is open")

portScanner(port)

