import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to img")
ap.add_argument("-k", "--k", type=int, default=3, help="size of kernel filter")
ap.add_argument("-s", "--sigma", type=int, default=21, help="value of sigma")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
k = args["k"]
s = args["sigma"]

bblur = cv2.bilateralFilter(image, k, s, s)
cv2.imshow("img", bblur)
cv2.waitKey(0)
