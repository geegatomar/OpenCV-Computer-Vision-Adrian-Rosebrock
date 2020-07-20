import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped image", flipped)
cv2.waitKey(0)
