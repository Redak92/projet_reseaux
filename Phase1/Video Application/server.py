import cv2
import socket
import pickle
import numpy as np
import queue

host = "192.168.10.2"
port = 5000
max_length = 65540

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

frame_info = None
buffer = None
frame = None

packet_queue = queue.Queue()

print("-> waiting for connection")

while True:
    data, address = sock.recvfrom(max_length)
    
    if len(data) < 100:  
        frame_info = pickle.loads(data)

        if frame_info:
            nums_of_packs = frame_info["packs"]
            
            for i in range(nums_of_packs):
                data, address = sock.recvfrom(max_length)
                
                packet_queue.put(data)

            buffer = b""
            while not packet_queue.empty():
                packet = packet_queue.get()
                buffer += packet

            frame = np.frombuffer(buffer, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            if frame is not None:
                frame = cv2.flip(frame, 1)
                cv2.imshow("Thanks to the server for displaying the captured images sent by the client.", frame)
                
                if cv2.waitKey(1) == 27:  
                    break

print("goodbye")