import argparse
import numpy as np
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
translated = imutils.translation(image, -40, 120)
cv2.imshow("Translated", translated)
cv2.waitKey(0)
