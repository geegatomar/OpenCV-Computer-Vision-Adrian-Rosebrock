import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)

red = (0, 0, 255)
cv2.line(canvas, (0, 100), (300, 250), red, 3)

blue = (255, 0, 0)
cv2.rectangle(canvas, (10, 10), (80, 120), blue, 2)

pink = (255, 0, 255)
cv2.rectangle(canvas, (200, 20), (220, 80), pink, -1)     # -1 for solid fill in rectangle


cv2.imshow("MyCanvas", canvas)
cv2.waitKey(0)
