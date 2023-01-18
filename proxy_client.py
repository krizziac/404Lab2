'''

Code was developed from following TA demo on Monday, Jan 16 2023 lab.

'''


import socket

BYTES_TO_READ = 4096

def get(host,port):

    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        print("waiting for response...")
        chunk = s.recv(BYTES_TO_READ)
        result = b''+ chunk

        while (len(chunk)> 0):
            chunk = s.recv(BYTES_TO_READ)
            result += chunk

        return result

print(get('127.0.0.1',8080))