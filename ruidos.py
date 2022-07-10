
import cv2 
import numpy as np 
  
image = cv2.imread('/Users/macbook/pdi-cedulas/teste-images/2_teste1.jpg') 
  
cv2.imshow('Original Image', image) 
cv2.waitKey(5) 
Gaussian = cv2.GaussianBlur(image, (5, 5), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 
cv2.waitKey(0) 
median = cv2.medianBlur(image, 5) 
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0) 
  
  
