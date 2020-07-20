import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

(centreX, centreY) = (canvas.shape[1]//2, canvas.shape[0]//2)
r = 50
white = (255, 255, 255)

cv2.circle(canvas, (centreX, centreY), r, white, 4)

red = (100, 0, 255)
for r in range(0, min(centreX, centreY), 25):
    cv2.circle(canvas, (centreX, centreY), r, red, 3)

cv2.imshow("MyCirclesCanvas", canvas)
cv2.waitKey(0)
