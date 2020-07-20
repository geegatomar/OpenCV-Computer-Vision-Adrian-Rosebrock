import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cropped = image[75 : 300, 300 : 575]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
