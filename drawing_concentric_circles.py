import numpy as np
import cv2

canvas = np.zeros((400, 400, 3), dtype="uint8")

centre = (200, 200)

for i in range(50, 0, -1):
    r = i * 4
    color = np.random.randint(255, size=3).tolist()
    cv2.circle(canvas, centre, r, color, -1)

cv2.imshow("Img", canvas)
cv2.waitKey(0)

