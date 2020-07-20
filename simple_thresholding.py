import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to img")
ap.add_argument("-t", "--threshold", type=int, default=127, help="threshold value")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
#cv2.imshow("image gray" ,image)

T, binimage = cv2.threshold(image, args["threshold"], 255, cv2.THRESH_BINARY)
T, invimage = cv2.threshold(image, args["threshold"], 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Img", cv2.bitwise_and(image, image, mask=invimage))
cv2.waitKey(0)
