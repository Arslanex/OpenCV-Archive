import cv2 as cv
import numpy as np

img = np.zeros((100,500,3), np.uint8)

# Trackbarı yerleştirmek için bir pencere açıyrouz
cv.namedWindow('image')

# Trackbarın çalışması için bir fonksiyon gerekli, biz fonksiyon
# üzerinden bir işlem yapmayacağımız için boş bir fonskyon açıyoruz
def callback(x):
    pass

print("TEST 1")
# Daha önce açtığımız pencereye bir Trackbar oluşturuyoruz
cv.createTrackbar('Trackbar_1', 'image', 300, 500, callback)
"""
Trackbar Adı ::
Pencere Adı ::
Low Value ::
High Value ::
Fonksiyon ::
"""

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# Şimdi oluşturduğumuz trackbardan gelen verileri çekerek resimin üztüne yazdıralım
# Trackbardan gelen değeri getTrackbarPos('trackbar adı','pencere adı')

print("TEST 2")
while True:
    imgCopy = img.copy()
    text = cv.getTrackbarPos('Trackbar_1', 'image')
    cv.putText(imgCopy,str(text),(50,50), cv.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv.LINE_AA)
    cv.imshow('image', imgCopy)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break