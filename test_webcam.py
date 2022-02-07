import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("cam", frame)
        cv2.waitKey(1)
    else:
        print("can not read frame")
        break
print("can not open camera")