import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

canvas = np.zeros((image.shape), dtype="uint8")
cv2.rectangle(canvas, (300, 75), (575, 300), (255, 255, 255), -1)

masked = cv2.bitwise_and(image, canvas)
cv2.imshow("Masked dog", masked)
cv2.waitKey(0)
