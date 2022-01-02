import cv2
import numpy as np
import threading
import socket

IP ="127.0.0.1"
PORT = 8821
ADDR = (IP,PORT)

def main():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    cap = cv2.VideoCapture(0)

    print(f"[CONNECTED] Client connected")

    connected = True
    while connected:
        ret,frame = cap.read()

        frame = cv2.resize(frame, (540, 430))
        encimg = cv2.imencode(".jpg", frame)[1].tobytes()
        client_socket.sendall(encimg)

        cv2.imshow('Client', frame)

        if (cv2.waitKey(1) == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()


main()