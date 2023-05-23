import cv2

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    cv2.imshow("camera", frame)
    if cv2.waitKey(0.5) == 113:
        break
video.release()
cv2.destroyAllWindows()