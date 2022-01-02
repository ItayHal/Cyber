import cv2
import numpy as np
import threading
import socket,time

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected")

    connected = True
    while connected:
        data = conn.recv(90456)
        nparr = np.fromstring(data, np.uint8)
        decimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if type(decimg) is type(None):
            pass
        else:
            cv2.imshow('Server', decimg)
            if cv2.waitKey(1) == ord('w'):
                break
    cv2.destroyAllWindows()

    conn.close()

def main():
    # create socket
    SERVER_IP = "0.0.0.0"
    PORT = 8821
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, PORT))
    server_socket.listen()
    print("listen")

    while True:
        conn, addr = server_socket.accept()
        t1 = threading.Thread(target=handle_client, args=(conn,addr))
        t1.start()

main()