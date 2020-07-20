import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(B, G, R) = cv2.split(image)

#cv2.imshow("Blue", B)
#cv2.imshow("Red", R)
#cv2.imshow("Green", G)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
