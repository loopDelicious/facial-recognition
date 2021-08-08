import cv2
import sys
import uuid

name = sys.argv[1] # name passed from command line argument

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/{}/image_{}.jpg".format(name, uuid.uuid4().hex)
        status = cv2.imwrite(img_name, frame)
        if status is True:
            print("{} written!".format(img_name))
        else:
            print("Image not written. Check person's folder created and passed as command line argument.")

cam.release()

cv2.destroyAllWindows()
