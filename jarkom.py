import http

def main():
    server = http.init()
    http.serve(server, lambda addr: print(f"Listening on http://{addr[0]}:{addr[1]}"))

if __name__ == "__main__":
    main()
