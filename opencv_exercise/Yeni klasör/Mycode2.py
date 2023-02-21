import cv2, time

video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.destroyAllWindows()

a=1

while True:
    a=a+1
    check, frame=video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",gray)

    cv2.waitKey(1)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
