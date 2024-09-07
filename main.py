import cv2
from PIL import Image
from util import get_limits

# colors in BGR
yellow = [0, 255, 255]
red = [0, 0, 255]
blue = [255, 0, 0]

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # location of pixels containing the info
    mask_ = Image.fromarray(mask)
    boundingBox = mask_.getbbox()

    if boundingBox is not None:
        x1, y1, x2, y2 = boundingBox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)
    #print(boundingBox)

    cv2.imshow('frame', frame) #can replace frame with mask for testing

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()