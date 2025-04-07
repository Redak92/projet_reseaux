import cv2
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5001))

print("En attente de l'image...")
data, addr = sock.recvfrom(65535)
buffer = pickle.loads(data)
img = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
cv2.imshow("Image reçue via UDP", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
