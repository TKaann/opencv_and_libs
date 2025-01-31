#resimlerin boyutunu oynuyoruz cunku bazı resimler cok buyuk olabiliyor, ornek olarak 1080 e 1080 bir foto var
#bu fotografta calısmak hem memory hem performans acısından maliyetli olabilir bunun yerine bu fotoyu
#240 a 240 a cekeriz ve islemlerimizi onunla yaparız.
#ayrıa derin ogrenmedeki bazı kutuphanelerin ozel boyutlandırmaları oluyor, sadece onları kabul ediyor.
#biz de kabul edilen boyutlara gore yeniden boyutlandırma yapmalıyız.

import cv2

#resmi ice akratıyoruz.
img = cv2.imread("lenna.png")   #resmi ice aktardık ve 0 da bize resmi siyah beyaz olarak almamıza yaradı.

#resmi yeniden boyutlandırmak icin orijinal boyutunu bilmemiz gerekiyor, orijinal boyutuna bakalım.
print("Resim Boyutu: ", img.shape)

cv2.imshow("Original Photo", img)
#outputta 512 den sonra cikan 3 bize resmin r g b oldgunu ifade ediyor.


#yeniden boyutlandıralım.
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shapae: ", imgResized.shape)
cv2.imshow("Resized Photo", imgResized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#crop islemini yapalım simdi de
imgCropped = img[:200,:500]   #normalde ilk x ekseninden baslar ama opencv de once y ekseninden yan yukseklikten baslıyor.
                                #width - height yerine --> height width oluyor. resimde de gorurseniz x ekseni daha buyuk
#y ekseninin 0. indexinden basla 200. indexine kadar al
#x ekseninin 0. indexinden basla 500. indexine kadar al yaptık kısacası.
cv2.imshow("Kirpik Resim", imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()















































































