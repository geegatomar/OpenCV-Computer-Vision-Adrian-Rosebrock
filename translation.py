import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to img")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#cv2.imshow("Original", image)
#cv2.waitKey(0)

M = np.float32([[1, 0, -90], [0, 1, -120]])       # warpAffine takes matrix of type float, hence we convert it here

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
