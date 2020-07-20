import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument("-k", "--k", type=int, default=3, help="size of kernel filter")
args = vars(ap.parse_args())

k = int(args["k"])
image = cv2.imread(args["image"])

blurred = cv2.blur(image, (k, k))
cv2.imshow("Blur-({}, {})".format(k, k), blurred)
cv2.waitKey(0)
