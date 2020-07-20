import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")

red = (0, 0, 255)

for i in range(0, 400, 20):
    for j in range(0, 400, 20):
        left = (i, j)
        right = (i + 10, j + 10)
        cv2.rectangle(canvas, left, right, red, -1)

cv2.imshow("Board", canvas)
cv2.waitKey(0)
    
