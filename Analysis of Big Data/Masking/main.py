import cv2
import numpy as np

#_Original Picture fig.1.0
img = cv2.imread("img/dog.jpg")
cv2.imshow("Original Photo", img)

#_Converting to Gray Scale fig.1.1
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Photo",gray)

#_Masking the Original fig.1.2
_, mask = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
cv2.imshow("Mask Original", mask)

#_Masking the GrayScale fg.1.3
_, graymask = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
cv2.imshow("Gray Mask", graymask)

cv2.waitKey(0)
cv2.destroyAllWindows()
