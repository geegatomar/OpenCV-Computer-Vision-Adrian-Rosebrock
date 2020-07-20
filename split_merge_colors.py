import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(B, G, R) = cv2.split(image)

zero = np.zeros(image.shape[:2], dtype="uint8")
red = cv2.merge([zero, zero, R])          # merge arguments shall be like [ b, g, r]
cv2.imshow("Red", red)
cv2.waitKey(0)
