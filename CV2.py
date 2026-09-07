import cv2
img = cv2.imread('image.jpeg',0)
small = cv2.resize(img,(200,200))
img[50:100,50:100] = 255
cv2.imshow('Modified Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()