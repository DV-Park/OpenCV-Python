import cv2

capture = cv2.VideoCapture("../Src/video_cars.avi")
if capture.isOpened()==False:
    raise Exception("카메라 연결 안됨")

print("너비%d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이%d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame=capture.read()
    if not ret:break
    if cv2.waitKey(30)>=0: break

    frame=cv2.Canny(frame, 150, 200)
    cv2.imshow("Video", frame)
capture.release()