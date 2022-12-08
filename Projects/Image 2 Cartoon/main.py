import cv2 as cv

# Resimi ekle
img = cv.imread("mustang.jpg")

# Editing
for i in range(30):
    img = cv.bilateralFilter(img, 9, 9, 7)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 3)
threshold = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 2)
colored_threshold = cv.cvtColor(threshold, cv.COLOR_GRAY2RGB)
result = cv.bitwise_and(img, colored_threshold)

# Sonucu ekrana yazdır
cv.imshow("RESULT", result)
cv.imwrite("cartoon.jpg", result)
cv.waitKey(0)
cv.destroyAllWindows()