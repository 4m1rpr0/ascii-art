import cv2

chars = ["█", "▓", "▒", "░", "▌", "@", "#", "$", "%", "▲", "▼", "►", "◄", "/", "\\", "?", ";", "+", ":", "^", "*", ",", ".", "\"", "'", "`"]

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    gray_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera", frame)
    for frame in gray_frames:
        for pixel in frame//10:
            print(pixel)
    if cv2.waitKey(1) == 113:
        break
video.release()
cv2.destroyAllWindows()