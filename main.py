import os
import cv2

chars = ["█", "▓", "▒", "░", "▌", "@", "#", "$", "%", "▲", "▼", "►", "◄", "/", "\\", "?", ";", "+", ":", "^", "*", ",", ".", "\"", "'", "`"]

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    gray_frames_large = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frames_small = cv2.resize(gray_frames_large, (112, 40), interpolation = cv2.INTER_AREA)
    cv2.imshow("camera", frame)
    frame_char = ""
    for frame in gray_frames_small:
        counter = 0
        for pixel in frame//10:
            counter += 1
            frame_char += chars[pixel]
            if counter > 100:
                counter = 0
                frame_char += "\n"
    os.system("cls")
    print(frame_char)
    if cv2.waitKey(1) == 113:
        break
video.release()
cv2.destroyAllWindows()