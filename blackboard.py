import numpy as np
import cv2

# print all the events
#events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)
# using event EVENT_MOUSEMOVE

# call back function


def click_event(event, x, y, flags, params):
    global state, erase
    print(event)
    events.append(event)
    if events[-1]==4 and events[-2]==1:
        if state == True:
            state = False
        else:
            state = True
    elif events[-1]==5 and events[-2]==2:
        if erase == True:
            state = True
            erase = False
        else:
            erase = True
            state = False

    if state == True:
        # print(x,y)
        img[y, x-1, 0], img[y-1, x, 0], img[y-1, x-1, 0], img[y,
                                                              x, 0], img[y+1, x+1, 0] = 255, 255, 255, 255, 255
        img[y, x-1, 1], img[y-1, x, 1], img[y-1, x-1, 1], img[y,
                                                              x, 1], img[y+1, x+1, 1] = 255, 255, 255, 255, 255
        img[y, x-1, 2], img[y-1, x, 2], img[y-1, x-1, 2], img[y,
                                                              x, 2], img[y+1, x+1, 2] = 255, 255, 255, 255, 255
        cv2.imshow("frame", img)
    elif erase == True:
        cv2.circle(img,(x,y),10,(0,0,0),3,-1)
        cv2.imshow("frame",img)
    else:
        cv2.imshow("frame", img)

    # if event == cv2.EVENT_MBUTTONDOWN and event == cv2.EVENT_MOUSEMOVE:
        # cv2.imshow("frame",img)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("frame", img)
events = []
state = False
erase = False

cv2.setMouseCallback("frame", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
