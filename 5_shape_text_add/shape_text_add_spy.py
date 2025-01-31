#sekil ve metın ekleme neden onemli: mesela bir nesne tespiti yaptıgımız zaman tespiti gerceklestirdigimize dair
#bir kutucuk cizecez ve nesneyi ifade edicez. yazı yazmak ise ilerleyen projelerde rakam sınıflandırmasında 
# % kac olasılıkla o rakam oldugunu yazdırıcaz ve metın olarak videomuza yansıtıcaz.


import cv2
import numpy as np


#resim üstünde oynamaktan ziyade simdi siyah bir resim olusturucaz.

#resim olusturuyoruz
img = np.zeros((512, 512, 3), np.uint8)  #512 512 ve 3 degerlerine sahip sıfırlardan olsuan int olan siyah bir resim bu.
#ne demistik onceden deger sıfıra yaklastıkca siyah oluyor 1 e yaklastıkca beyaz oluyoru burda da sıfırlardan olusturduk.
print(img.shape)



#resmimizi gorsellestiriyoruz.
cv2.imshow("Siyah", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#simdi bunun ustune belli baslı resim ve metin eklemeye baslayalım.
#ilk once bi line ekleyerek baslayalım.
cv2.line(img, (100,0), (400,512), (0,255,0), 3)   
#(resim, baslangıc noktası, bitis noktası, renk "= 0,255,0 yesile denk geliyor.", kalinlik)
#Ayrıca opencv bizim bilgigimiz RGB degerlerini de BGR olarak kullanıyor. yani ilk once mavi en son kırmızı geliyor.
cv2.imshow("Cizgi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#simdi dikdortgen cizelim
#dikdortgen bizim icin onemli cunku nesneleri tespit ettikten sonra tespit edilenin etrafına kutucuk cizicez.

#(resim, baslangic, bitis, renk)
cv2.rectangle(img, (0,0), (256,256), (255,0,0))    #eger buranın icine bir de ,cv2.FILLED  eklersek dikdortgenin icini doldurur.
cv2.imshow("Dikdortgen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#mavi bir dikdortgen olusturduk.



#cember olusturma

#(resim, merkez, yarıcap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#mesela ilerde nesne takibi yaparken nesnenin merkezine bir cember koyup nesnenin takibini yapabiliriz.



#yazı eklemeye gelelim simdi des

#metin ekleme
#(resim, baslangıc noktası, font tipi, kalınlık, renk)
cv2.putText(img, "Resim", (300,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Yazi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




































































