import cv2

img = cv2.imread("image.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("Global Threshold", binary)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)

cv2.destroyAllWindows()
