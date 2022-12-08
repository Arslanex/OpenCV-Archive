import cv2 as cv
import numpy as np # yaoay bir resim oluşturmak için kullanacağız

#%%# ÇİZGİ
img = np.zeros((512,512,3), np.uint8)

line = cv.line(img,(0,0),(511,511),(255,0,0),5)
"""
src :: 
x1 ::
x2 ::
color ::
thickness  ::
"""

cv.imhow("LINE", line)
cv.waitKey(0)

#%%# Rectangle
img = np.zeros((512,512,3), np.uint8)

rectangle = cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
"""
src :: 
x1 :: top left corner
x2 :: bot right corner
color ::
thickness  ::
"""

cv.imhow("LINE", rectangle)
cv.waitKey(0)

#%%# Circle
img = np.zeros((512,512,3), np.uint8)

circle = cv.circle(img,(447,63), 63, (0,0,255), -1)
"""
src :: 
center ::
radius ::
color ::
thickness  ::
"""

cv.imhow("LINE", circle)
cv.waitKey(0)

#%%# Ellipse
img = np.zeros((512,512,3), np.uint8)

ellipse = cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
"""
src :: 
center ::
axes lengths :: major axis length, minor axis length
angle :: 
startAngle ::
endAngle ::
color :: scaler value
thickness ::
"""

cv.imhow("LINE", ellipse)
cv.waitKey(0)

#%%# Put Text
text = np.zeros((512,512,3), np.uint8)

text = cv.putText(img,'OpenCV',(10,500), cv.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv.LINE_AA)
"""
src :: 
text ::
coor ::
font ::
fontScale ::
color :: 
thickness ::
lineType ::
"""

cv.imhow("LINE", text)
cv.waitKey(0)

#%%#
cv.DestroyAllWindows()