import cv2
import mediapipe as mp

webcan = cv2.VideoCapture(0)
head_track = mp.solutions.face.detection
head_recognize = head_track.face.detection()
draw = mp.solutions.drawing_utils

while True:
    checker, frame = webcan.read()

    if not checker:
        break

    face_list = head_recognize.process(frame)

    if face_list.detections:
        for face in face_list.detections:
            draw.draw_detection(frame, face)

webcan.release()