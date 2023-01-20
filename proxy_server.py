import socket
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 4096


def handle_request(host, port, request):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(request.encode())
            s.shutdown(socket.SHUT_WR)
            full_data = s.recv(BUFFER_SIZE)
            return full_data
    except Exception as e:
        print(e)
        return None


def handle_connection(conn):
    with conn:
        request = conn.recv(BUFFER_SIZE)
        host = "www.google.com"
        full_data = handle_request(host, 80, request.decode())
        conn.sendall(full_data)
        conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            p = Process(target=handle_connection, args=(conn,))
            p.daemon = True
            p.start()
            print("Started process ", p)


if __name__ == "__main__":
    start_server()
