import cv2
import matplotlib.pyplot as plt

img = cv2.imread('odev1.jpg', 0)  #0 yapmamiz gri olmasina yariyor.
cv2.imshow('Example', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(img.shape)

#resmi 4/5 oraninda yeniden boyutlandiriyorum.
imgResized = cv2.resize(img, (int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
cv2.imshow("Yeniden Boyutlandirma", imgResized), cv2.waitKey(0), cv2.destroyAllWindows()

#simdi orijinal resme yazi ekleyelim
cv2.putText(img,"Kopek", (375,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
cv2.imshow("Kopek Text", img), cv2.waitKey(0), cv2.destroyAllWindows()



#simdi ise orijinal resme 100 treshold degeri uzerindekileri beyaz yapip altindakileri siyah yapalim.
#binary treshold yontemini kullanicam.
_, thresh_img = cv2.threshold(img, thresh = 100, maxval = 255, type = cv2.THRESH_BINARY)
cv2.imshow("Thresh Img", thresh_img), cv2.waitKey(0), cv2.destroyAllWindows()

#simdi orijinal haline gaussian bulaniklastirma uyguluycam
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
cv2.imshow("Gaussian Blur", gb), cv2.waitKey(0), cv2.destroyAllWindows()

#simdi oriijinal resme laplacian gradyan uygulayalim
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
cv2.imshow("Laplacian Img", laplacian), cv2.waitKey(0), cv2.destroyAllWindows()

#simdi ise son olarak orijinal resmin histogramini cizelim.
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)




























































































































































