import cv2 as cv

cap = cv.VideoCapture(0)


def make_1080p():
    cap.set(3, 72)
    cap.set(4, 72)


# make_1080p()

def rescale_frame(frame, percent):
    width = int(frame.shape[1] * (percent / 100))
    height = int(frame.shape[0] * (percent / 100))
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


while True:
    rect, frame = cap.read()
    frame200 = rescale_frame(frame, 200)

    cv.imshow('frame', frame)
    cv.imshow('frame200', frame200)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
