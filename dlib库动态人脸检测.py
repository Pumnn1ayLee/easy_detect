import numpy as np
import cv2
import dlib

cap = cv2.VideoCapture(0)
win = dlib.image_window()
detector = dlib.get_frontal_face_detector()
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    rects = detector(gray)
    win.set_image(gray)
    win.add_overlay(rects)
    cv2.waitKey(1)
    win.clear_overlay()
    cv2.waitKey(1)
    win.add_overlay(rects)
    if cv2.waitKey(25) == ord('q'):
        break


cv2.destroyAllWindows()
print(ret)
cap.release()



