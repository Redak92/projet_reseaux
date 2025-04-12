import cv2
from protocols.UDP import UDPSocket 
import pickle

HOST_ADDR = ('192.168.10.1', 12345)
SERV_ADDR = ('192.168.10.2', 5001)
# Lire l'image
img = cv2.imread("../Media/test_image.jpeg")
if img is None:
    raise FileNotFoundError("Image non trouvée : test_image.jpeg")

# Encoder l'image en mémoire (format JPEG)
_, buffer = cv2.imencode(".jpg", img)


# Créer un socket UDP
sock = UDPSocket(*HOST_ADDR)
# Envoyer l'image
sock.sendto(buffer, SERV_ADDR)  # ou l'IP du serveur distant
print("Image envoyée avec succès.")
