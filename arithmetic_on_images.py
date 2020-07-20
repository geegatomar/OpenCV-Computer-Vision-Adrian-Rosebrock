import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
#added = image + M
cv2.imshow("Added", added)

subtracted = cv2.subtract(image, M)
#cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
