import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument("-k", "--k", type=int, default=3, help="size of kernel filter")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

k = args["k"]
gblur = cv2.GaussianBlur(image, (k, k), 0)               # GaussianBlur takes 3 arguments
cv2.imshow("Image - ({}, {})".format(k, k), gblur)
cv2.waitKey(0)
