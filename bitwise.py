import cv2
import argparse
import numpy as np

rectangle = np.zeros((300, 300, 3), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

circle = np.zeros((300, 300, 3), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)

bitwiseOr = cv2.bitwise_or(rectangle, circle)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)

#cv2.imshow("Bitwise And", bitwiseAnd)
#cv2.imshow("Bitwise or", bitwiseOr)
cv2.imshow("Bitwise xor", bitwiseXor)
cv2.waitKey(0)
