import cv2
import socket
import pickle
import numpy as np
import threading

host = "0.0.0.0"
port = 5000
max_length = 65540

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

clients = {}  # Dictionnaire pour stocker les flux des clients

print("-> waiting for connections")

def handle_client(address):
    global clients
    frame_info = None
    buffer = None
    
    while True:
        data, _ = sock.recvfrom(max_length)
        
        if len(data) < 100:
            frame_info = pickle.loads(data)
            if frame_info:
                nums_of_packs = frame_info["packs"]
                
                for i in range(nums_of_packs):
                    data, _ = sock.recvfrom(max_length)
                    buffer = data if i == 0 else buffer + data
                
                frame = np.frombuffer(buffer, dtype=np.uint8)
                frame = frame.reshape(frame.shape[0], 1)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                frame = cv2.flip(frame, 1)
                
                if frame is not None and isinstance(frame, np.ndarray):
                    clients[address] = frame  # Stocke le frame du client
        
        if cv2.waitKey(1) == 27:
            break

def display_streams():
    while True:
        if clients:
            frames = list(clients.values())[:4]  # Prendre au maximum 4 flux
            height, width, _ = frames[0].shape if frames else (240, 320, 3)
            grid_size = 2
            canvas = np.zeros((height * grid_size, width * grid_size, 3), dtype=np.uint8)
            
            for idx, frame in enumerate(frames):
                row, col = divmod(idx, grid_size)
                canvas[row * height:(row + 1) * height, col * width:(col + 1) * width] = cv2.resize(frame, (width, height))
            
            cv2.imshow("Video Conference", canvas)
        
        if cv2.waitKey(1) == 27:
            break

# Thread pour gérer l'affichage
display_thread = threading.Thread(target=display_streams, daemon=True)
display_thread.start()

while True:
    data, address = sock.recvfrom(max_length)
    if address not in clients:
        threading.Thread(target=handle_client, args=(address,), daemon=True).start()
