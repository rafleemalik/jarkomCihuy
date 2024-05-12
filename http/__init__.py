import socket, threading as thread, time, signal, sys

def init(port = 3000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", port))
    sock.settimeout(1)
    sock.listen(1)
    return {"socket": sock}

def serve(http):
    def __sigint_handler(sig, frame):
        close(http)
        sys.exit(0)

    signal.signal(signal.SIGINT, __sigint_handler)

    while True:
        try:
            (csock, addr) = http["socket"].accept()
            msg = csock.recv(4096).decode()
            csock.send(msg.upper().encode())
            csock.close()
        except TimeoutError:
            pass

def close(http):
    if not http["socket"]:
        return True

    http["socket"].close()
    return True
