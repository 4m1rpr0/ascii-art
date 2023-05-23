import cv2

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera", frame)
    if cv2.waitKey(0.5) == 113:
        break
video.release()
cv2.destroyAllWindows()