import cv2

img = cv2.imread('/home/thor/Desktop/FYP/test_data/fan1.jpg')
#img2 = cv2.imread('/home/thor/Desktop/FYP/img1.jpg')
img1 = cv2.resize(img, (0, 0), fx=0.2, fy=0.20)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp1 = sift.detect(gray, None)
#kp2 = sift.detect(img2, None)

#img1 = cv2.drawKeypoints(img, kp1, img)
img1=cv2.drawKeypoints(gray, kp1, img)
cv2.imshow("img", img1)
cv2.waitKey(8000)
#img2 = cv2.drawKeypoints(img2, kp2, img2)

#cv2.imwrite('/home/thor/Desktop/FYP/1.1.jpg', img1)
#cv2.imwrite('/home/thor/Desktop/FYP/1.2.jpg', img2)
