import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (600, 400))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 180)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in the image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 4)
cv2.imshow("img", coins)
cv2.waitKey(0)



