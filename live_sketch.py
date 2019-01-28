import numpy as np
import cv2
def doodle(f, b):
    r = f*255/(255-b)
    r[np.logical_or(r>255, b == 255)] = 255
    return r

def sketch(img):
    #inverted_img = 255 - img;#1
    #return inverted_img
    #img_blur = cv2.GaussianBlur(inverted_img, (3,3), 0)
    #dimage = doodle(inverted_img, img)#2
    #canny_edges = cv2.Canny(dimage, 10 , 70)
    #dimage = cv2.GaussianBlur(dimage, (3,3), 0)
    #ret, mask = cv2.threshold(dimage, 70, 255, cv2.THRESH_BINARY)
    #return dimage#3
    #ret, thresh = cv2.threshold(img, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im2, contours, -1, (0, 255, 0), 3)
    #c, h = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(img, c, -1, (0,255,0), 3)
    return im2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', sketch(gray))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()