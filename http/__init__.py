import socket, os, threading

def log(*argv):
    print("[INFO ::]", *argv)

def init(port=3000, thread=False):
    addr = ("127.0.0.1", port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(1)
    return {"socket": sock, "addr": addr, "thread": thread}

def read_file(path):
    with open(path, "r") as f:
        content = f.read()
        f.close()
        return content

def normalize_path(path, root):
    path = f"./{root}/{path}"

    if path.endswith("/"):
        path = path[:-1]

    if os.path.isdir(path):
        path += "/index.html"
    
    return path

def __on_request(csock, root):
    msg = csock.recv(4096).decode()

    head = msg.rstrip().split("\n")[0].split()
    path = normalize_path(head[1], root)

    if not os.path.exists(path):
        csock.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        csock.close()
        return

    content = read_file(path)
    csock.send(f"HTTP/1.1 200 OK\n\n{content}\r\n".encode())
    csock.close()

def serve(http, root, callback=lambda host, port: None):
    callback(http["addr"][0], http["addr"][1])

    while True:
        log("Listening for connection..")
        (csock, addr) = http["socket"].accept()

        log("Connection hit!")
        if http["thread"]:
            threading \
                .Thread(target=__on_request, args=[csock, root]) \
                .start()
        else:
            __on_request(csock, root)
        
def close(http):
    http["socket"].close()
