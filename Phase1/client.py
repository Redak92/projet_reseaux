import cv2
import socket
import math
import pickle
from IP.UDP import SocketUDP

max_length = 65000
host = "127.0.0.1"
port = 5000

sock = SocketUDP(host)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while ret:
    # compress frame
    retval, buffer = cv2.imencode(".jpg", frame)

    if retval:
        # convert to byte array
        buffer = buffer.tobytes()
        # get size of the frame
        buffer_size = len(buffer)

        num_of_packs = 1
        if buffer_size > max_length:
            num_of_packs = math.ceil(buffer_size/max_length)

        frame_info = {"packs":num_of_packs}

        sock.send_udp((host, port), pickle.dumps(frame_info))
        
        left = 0
        right = max_length

        for i in range(num_of_packs):
            data = buffer[left:right]
            left = right
            right += max_length
            sock.send_udp((host, port), data)
    
    ret, frame = cap.read()

print("done")