import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)


"""
Fonksiyonun ismini istediğiniz gibi koysanız bile parametreler OpenCV'nin standartlarına göre olamlıdır. Bunun sebebi bu
bizim fonksiyonumuzun, aşağıda olduğı gibi,  setMouseCallBack() methodu ile beraber kullanılacak olmasıdır. Arka planda
bu method bizim fonsksiyonumuzun parametrelerini zaten dolduruyor olacak.
"""
def drawCircle1(event, x, y, flags, param):
    # farenin hareket etmesi durumunda
    if event == cv2.EVENT_MOUSEMOVE:
        print('({}, {})'.format(x, y))
        # resimi kopyalayın
        imgCopy = img.copy()
        # kopya resime bir daire çizin
        cv2.circle(imgCopy, (x, y), 10, (255, 0, 0), -1)
        # Image isimli pencerede gösterin
        cv2.imshow('image', imgCopy)

"""
Program çalıştığında göreceğiniz şey farenizi siyah ekran üzerine getirdiğiniz zaman farenin işaretçisi konumunda oluşan
daire olacaktır. Ama herhangi bir çizim yapamıyorsunuz. Bunun sebebi fonksiyon içinde imgCopy isimli, resimin kopyası
olan bir resim üzerinde işlem yapıp onuda Image isimli pencerede gösteriyor oluşumuz. Fare her hareket ettiğinde orjinal
resim kopyalanıyor bu yüzden çizilen tüm şekiller siliniyor ve sonrasında yeniden çiziliyor.

Bu bilgiye göre eğer imgCopy = img.copy() satırında copy() methodunu siler isek fare ile çizim yapabilir olacağız. 
Şimdi bunu test etmek için yapmanız gereken tek şey 48.satırda drawCircle1 yerine drawCircle2 yazarak yeni fonksiyonu
çağırmaktır 
"""

def drawCircle2(event, x, y, flags, param):
    # farenin hareket etmesi durumunda
    if event == cv2.EVENT_MOUSEMOVE:
        print('({}, {})'.format(x, y))
        # resimi kopyalayın
        imgCopy = img
        # kopya resime bir daire çizin
        cv2.circle(imgCopy, (x, y), 10, (255, 0, 0), -1)
        # Image isimli pencerede gösterin
        cv2.imshow('image', imgCopy)


# Image isimli pencerede resimi gösterin
cv2.imshow('image', img)
# Fonskiyonu image isimli pencerede uygulamaya başlayın
cv2.setMouseCallback('image', drawCircle1) # drawCircle2

# Standart kapanış
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
ALL MOUSE EVENTS 
    EVENT_MOUSEMOVE     = 0     :: Farenin hareket etmesi
    EVENT_LBUTTONDOWN   = 1     :: Sol butona basma
    EVENT_RBUTTONDOWN   = 2     :: Sağ butona basma
    EVENT_MBUTTONDOWN   = 3     :: Orta butona basma
    EVENT_LBUTTONUP     = 4     :: Sol butonun kalkması
    EVENT_RBUTTONUP     = 5     :: Sağ butonun kalkması
    EVENT_MBUTTONUP     = 6     :: Orta butonun kalkması
    EVENT_LBUTTONDBLCLK = 7     :: Sol butona iki kez tıklama
    EVENT_RBUTTONDBLCLK = 8     :: Sağ butona iki kez tıklama
    EVENT_MBUTTONDBLCLK = 9     :: Orta butona iki kez tıklama
    EVENT_MOUSEWHEEL    = 10    :: Tekerleğin ileri dönüşü
    EVENT_MOUSEHWHEEL   = 11    :: Tekerleğin geri dönüşü
"""