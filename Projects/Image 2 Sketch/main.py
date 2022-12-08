import cv2 as cv

img = cv.imread('joker.jpg')
height, width,  = img.shape[:2]

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
blur = cv.GaussianBlur(gray, (21, 21), 0, 0)
result = cv.divide(gray, blur, scale=256)

cv.imwrite("cartoon.jpg", result)
cv.imshow('Result', result)

cv.waitKey(0)
cv.destroyAllWindows()