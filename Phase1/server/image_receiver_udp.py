import cv2
import socket
import pickle
import numpy as np  # ← Needed to handle the buffer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5001))

print("En attente de l'image...")
data, addr = sock.recvfrom(65535)

with open("received_image.jpg", "wb") as f:
    f.write(data)
