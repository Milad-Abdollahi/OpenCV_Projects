import cv2 as cv

img = cv.imread('photos/group1.jpg')
cv.imshow('group1', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)

print(f'# faces found: {len(face_rect)}')
for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
