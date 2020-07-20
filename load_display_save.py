import argparse
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

print("ap: ", ap)
print("ap.parse_args() : ", ap.parse_args())
print("args: ", args)

image = cv2.imread(args["image"])

print("Height: {}, Width: {}, Channels: {} ".format(image.shape[0], image.shape[1], image.shape[2]))

cv2.imshow("DogImage", image)
cv2.waitKey(0)


