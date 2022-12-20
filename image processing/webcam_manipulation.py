import cv2

camera=cv2.VideoCapture(0)   # 0 means the frist webcame
while camera.isOpened():
    status,image=camera.read()
    if not status:
        print("Could not read image")
        break
    h,w,_=image.shape   # _ means how many layers in image
    image_bigger=cv2.resize(image,(2*w,2*h))     # also change width of screen
    image_bw=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("bigger window ",image_bigger)

    cv2.imshow('black and white image',image_bw)
    cv2.imshow("Webcam window",image)
    if cv2.waitKey(1)==27:   # 27 means the ESC key
        
        break

camera.release()
cv2.destroyAllWindows()
