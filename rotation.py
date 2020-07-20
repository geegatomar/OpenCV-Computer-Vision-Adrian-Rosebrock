import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(h, w) = image.shape[:2]
centre = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(centre, 45, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Rotated", rotated)
cv2.waitKey(300*1000)
