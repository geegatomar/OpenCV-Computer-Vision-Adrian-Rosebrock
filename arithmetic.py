import cv2
import numpy as np


print("Max of 255:  {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min of 0:    {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("Wrap around: {}".format(np.uint8([100]) + np.uint8([200])))
print("Wrap around: {}".format(np.uint8([50]) - np.uint8([100])))
