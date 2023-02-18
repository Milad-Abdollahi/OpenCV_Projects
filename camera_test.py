import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)
    cv.imshow('gray', gray)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# when everything is done release the capture
cap.release()
cv.destroyAllWindows()
