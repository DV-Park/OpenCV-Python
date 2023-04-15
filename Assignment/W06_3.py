import numpy as np
import cv2

while True:
    no=int(input("차량 영상 번호( 0:종료): "))
    if no ==0: break

    fname="../SrcCode/chap07/images/test_car/{0:02d}.jpg".format(no)
    img=cv2.imread(fname,cv2.IMREAD_COLOR)
    if img is None:
        print(str(no)+"번 영상 파일이 없습니다.")
        continue

    # 이미지 전처리
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    # 윤곽선 검출
    cnts, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

    screenCnt = None

    # 윤곽선에서 직사각형 찾기
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    # 번호판 후보가 없으면 종료
    if screenCnt is None:
        print("번호판 후보 영역을 찾을 수 없습니다.")
    else:
        # 번호판 후보 영역 표시
        cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)
        cv2.imshow("img", img)
        cv2.waitKey(0)