import numpy as np
import cv2
import dlib
from math import hypot
import sys
from models import *

capture = cv2.VideoCapture(0)

cond = sys.argv[1]

while(True):

	ret, frame = capture.read()
	cv2.imshow('original', frame)
	result = aplica_filtro(frame, cond)
	cv2.imshow('filtro', result)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
