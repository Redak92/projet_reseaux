import cv2
from protocols.UDP import UDPSocket
import math
import pickle

max_length = 65000
host = "192.168.10.2"
port = 5000

sock = UDPSocket("192.168.10.1", 12345)
#sudo modprobe v4l2loopback devices=1 video_nr=10 card_label="FakeCam" exclusive_caps=1
#ffmpeg -re -stream_loop -1 -i sample.mp4 -f v4l2 /dev/video10

cap = cv2.VideoCapture("/dev/video10")
ret, frame = cap.read()

while ret:
    retval, buffer = cv2.imencode(".jpg", frame)

    if retval:
        buffer = buffer.tobytes()
        buffer_size = len(buffer)

        num_of_packs = 1
        if buffer_size > max_length:
            num_of_packs = math.ceil(buffer_size / max_length)

        frame_info = {"packs": num_of_packs}

        sock.sendto(pickle.dumps(frame_info), (host, port))

        left = 0
        right = max_length

        for i in range(num_of_packs):
            data = buffer[left:right]
            left = right
            right += max_length
            sock.sendto(data, (host, port))

    ret, frame = cap.read()

print("done")