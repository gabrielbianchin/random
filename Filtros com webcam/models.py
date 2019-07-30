import numpy as np
import cv2
import dlib
from math import hypot

def hisEqulColor(img):
	ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
	channels=cv2.split(ycrcb)
	cv2.equalizeHist(channels[0],channels[0])
	cv2.merge(channels,ycrcb)
	cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
	return img

def aplica_filtro(frame, cond):
	if cond == 'cinza':
		return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	    
	elif cond == 'negativo':
		return (255 - frame)

	elif cond == 'blur':
		kernel = np.ones((10,10),np.float32)/50
		return cv2.filter2D(frame, -1, kernel)

	elif cond == 'y':
		kernel = np.asarray([[-1, 0, 1], [-2, 0, 2], [-1, 0, -1]])
		return cv2.filter2D(frame, -1, kernel)

	elif cond == 'x':
		kernel = np.asarray([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
		return cv2.filter2D(frame, -1, kernel)

	elif cond == 'realce':
		kernel = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
		return cv2.filter2D(frame, -1, kernel)

#	elif cond == 'binario':
#		result = 0

	elif cond == 'equalizado':
		return hisEqulColor(frame)

	elif cond == 'cartoon':
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.medianBlur(gray, 5)
		edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
		color = cv2.bilateralFilter(frame, 9, 300, 300)
		return cv2.bitwise_and(color, color, mask=edges)

	else:
		return frame
