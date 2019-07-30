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

	elif cond == 'mosaico':
		img1 = frame[0:120, 0:160, :]
		img2 = frame[0:120, 160:320, :]
		img3 = frame[0:120, 320:480, :]
		img4 = frame[0:120, 480:640, :]
		img5 = frame[120:240, 0:160, :]
		img6 = frame[120:240, 160:320, :]
		img7 = frame[120:240, 320:480, :]
		img8 = frame[120:240, 480:640, :]
		img9 = frame[240:360, 0:160, :]
		img10 = frame[240:360, 160:320, :]
		img11 = frame[240:360, 320:480, :]
		img12 = frame[240:360, 480:640, :]
		img13 = frame[360:480, 0:160, :]
		img14 = frame[360:480, 160:320, :]
		img15 = frame[360:480, 320:480, :]
		img16 = frame[360:480, 480:640, :]
		
		coluna1 = np.concatenate((img6, img8, img12, img4))
		coluna2 = np.concatenate((img11, img16, img14, img15))
		coluna3 = np.concatenate((img13, img1, img2, img10))
		coluna4 = np.concatenate((img3, img9, img7, img5))

		return np.column_stack((coluna1, coluna2, coluna3, coluna4))

	else:
		return frame
