import http, signal, sys

def main():
    server = http.init()
    http.serve(server)

if __name__ == "__main__":
    main()
