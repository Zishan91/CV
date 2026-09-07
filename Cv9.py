import cv2
img = cv2.imread('image3.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray [50:100,50:100] = 255

gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

equalized = cv2.equalizeHist(gray)

orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(gray, None)
img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
img =cv2.imread('CV/image3.png')

faces = face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('Image.jpg', img)
cv2.imshow('Gray',gray)
cv2.imshow('Modified',gray)
cv2.imshow("Gaussian",gaussian)
cv2.imshow("Median",median)
cv2.imshow("Bilateral",bilateral)
cv2.imshow("Equalized",equalized)
cv2.imshow('img_kp',img_kp)
cv2.waitKey(0)

