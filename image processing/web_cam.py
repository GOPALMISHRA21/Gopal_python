import cv2

camera=cv2.VideoCapture(0)   # 0 means the frist webcame
while camera.isOpened():
    status,image=camera.read()
    if not status:
        print("Could not read image")
        break


    cv2.imshow("Webcam window",image)
    if cv2.waitKey(1)==27:   # 27 means the ESC key
        break

camera.release()
cv2.destroyAllWindows()

