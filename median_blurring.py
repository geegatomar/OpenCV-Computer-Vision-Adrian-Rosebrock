import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument("-k", "--k", type=int, default=3, help="size of  kenrel filter")
args = vars(ap.parse_args())

k = args["k"]
image = cv2.imread(args["image"])

mblur = cv2.medianBlur(image, k)
cv2.imshow("img", mblur)
cv2.waitKey(0)
