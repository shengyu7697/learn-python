#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2

#img = cv2.imread('lena.jpg')
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
#img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow('image', img)
cv2.waitKey(0)

#cv2.imwrite('output.png', img)