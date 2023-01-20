import socket

HOST = "localhost"
PORT = 8001
payload = "GET / HTTP/1.1\nwww.google.com\n\n"


def connect(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = s.recv(1024)
        print(full_data)
        return s
    except Exception as e:
        print(e)
        return None


def main():
    connect(('127.0.0.1', 8001))


if __name__ == "__main__":
    main()
