import cv2
img = cv2.imread('image.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(gray, None)
img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))
cv2.imshow("ORB Keypoints", img_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()