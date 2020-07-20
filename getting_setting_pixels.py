import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("OriginalImage", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(image.shape, image[0].shape, image[0][0].shape)

(g, b, r) = image[0][0]
print("Pixel at [0][0] - Red: {},   Green: {},   Blue: {}".format(r, g, b))

(g, b, r) = (0, 0, 255)
image[0][0] = (g, b, r)
print("Pixel at [0][0] - Red: {},   Green: {},  Blue: {}".format(r, g, b))


corner = image[0:250, 0:100]
#cv2.imshow("Corner", corner)
#cv2.waitKey(0)

image[0:250, 0:100] = (0, 255, 0)
#cv2.imshow("Updated", image)
#cv2.waitKey(0)

