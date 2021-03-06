import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('/home/thor/Desktop/FYP/camera_calibration/?.jpg')

for fname in images:
	print "in loop"
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#image show
	window_name = 'img'
	cv2.imshow(window_name, gray)
	# Find the chess board corners
	ret, corners = cv2.findCirclesGrid(gray, (8, 8),None)

	# If found, add object points, image points (after refining them)
	if ret == True:
		print "in if"
	        objpoints.append(objp)
	
	        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
	        imgpoints.append(corners2)
	
	        # Draw and display the corners
	        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
		plt.imshow(img3)
		plt.savefig('/home/thor/Desktop/FYP/cali_result/img.jpg')
	        #cv2.imshow('/home/thor/Desktop/FYP/cali_result/img.jpg',img)
	        #cv2.waitKey(500)

cv2.destroyAllWindows()
