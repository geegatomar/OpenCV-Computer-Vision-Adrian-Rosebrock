import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of image")
ap.add_argument("-w", "--width", default=100, help="Width of resized img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
width = int(args["width"])

ratio = width / image.shape[1]

dim = (int(ratio * image.shape[0]), width)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized img", resized)
cv2.waitKey(0)
