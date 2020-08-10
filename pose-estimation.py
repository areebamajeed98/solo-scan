import numpy as np
import cv2
#import matplotlib.pyplot as plt

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1, 2)

axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)


# Arrays to store object points and image points from all the images
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane

im = cv2.imread('/home/thor/Desktop/FYP/camera_calibration/data/5.jpg') #chess board image
# resizing images with ratio 0.25, image size is very large
img = cv2.resize(im, (0, 0), fx=0.35, fy=0.35)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #color to gray
	
# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

# If found, add object points, image points (after refining them)
if ret == True:
	print "in 1"
	objpoints.append(objp)
	corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
	imgpoints.append(corners2)

    # Draw and display the corners
	img = cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
    
    #CALIBRATION
	global cameraMatrix, distCoeffs, rotvecs, transvecs
	retval, cameraMatrix, distCoeffs, rotvecs, transvecs = cv2.calibrateCamera(objpoints,  imgpoints, gray.shape[::-1], None, None)

#Function to draw 3D axis
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

#---Pose Estimation---
	
# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

# If found, add object points, image points (after refining them)
if ret == True:
	print "in 2"
	corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

	#Rotation and translation vector
	ret, rvec, tvec = cv2.solvePnP(objp, corners2, cameraMatrix, distCoeffs)

	#project 3D image to an image plane
	imgpts, jac = cv2.projectPoints(axis, rvec, tvec, cameraMatrix, distCoeffs)
	image6 = cv2.imread('/home/thor/Desktop/FYP/camera_calibration/data/5.jpg')
	image69 = cv2.resize(image6, (0, 0), fx=0.35, fy=0.35)
	newImage = draw(image69, corners2, imgpts)
	#cv2.imshow('newImage', newImage)
	#cv2.waitKey(2000)

	cv2.imwrite('/home/thor/Desktop/FYP/camera_calibration/poseEst/pe.jpg', newImage)
