import numpy as np
import cv2
from skimage import data, filters

cap = cv2.VideoCapture("../Src/cctv_88jc.mp4")

bg_image = cv2.imread("cctv_bacgr.jpg")

frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    diff = cv2.absdiff(bg_image, frame)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # 너무 작은 값은 무시 (잡음 제거)
        if cv2.contourArea(c) < 10:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(30)==27:
        break

cap.release()