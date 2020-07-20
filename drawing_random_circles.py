import cv2
import numpy as np



# drawing 25 random circles

canvas = np.zeros((400, 400, 3), dtype="uint8")

for i in range(25):
    radius = np.random.randint(180)             # will generate random radius value between 0 and 100
    
    centre = np.random.randint(0, 400, size=(2, )) 
    color = np.random.randint(0, 255, size=(3, ))
    color = (int(color[0]), int(color[1]), int(color[2]))
    cv2.circle(canvas, tuple(centre), radius, tuple(color), 2)

cv2.imshow("MyCanvas", canvas)
cv2.waitKey(0)


