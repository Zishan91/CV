import cv2
img = cv2.imread('image.jpeg')
cv2.imshow('Image.jpg', img)
cv2.waitKey(0)
cv2.imwrite('output.jpg', img)
cv2.destroyAllWindows()