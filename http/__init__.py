import socket, signal, sys

def init(port=3000):
    addr = ("127.0.0.1", port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(1)
    return {"socket": sock, "addr": addr}

def serve(http, callback=lambda host, port: None):
    def __sigint_handler(sig, frame):
        close(http)
        sys.exit(0)

    signal.signal(signal.SIGINT, __sigint_handler)
    callback(http["addr"][0], http["addr"][1])

    while True:
        (csock, addr) = http["socket"].accept()
        msg = csock.recv(4096).decode()
        csock.send(msg.upper().encode())
        csock.close()

def close(http):
    http["socket"].close()
