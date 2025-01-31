#goruntu esikleme sudur: bizim normalde esik degerlerimiz 0-255 arası. biz bunu 125 den ustunu alma dersek bir esik
#degeri koymus oluruz.
#bu da mesela bizim on planda duran nesnelerimizi daha once cıkarmamıza arka planı daha da yok etmemize yarayabilir
#burda threshold ve adaptive threshold esikleme yontemleri vardır.

import cv2
import matplotlib.pyplot as plt

#simdi resmi ice aktarıyoruz ve siyah beyaza yani gri scale ile boyuyoruz
img = cv2.imread("ronaldo.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#resmi gorsele dokuyoruz.
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#esik degerlerini girme.
_, thresh_img = cv2.threshold(img, thresh = 80, maxval = 255, type = cv2.THRESH_BINARY)

#burada simdi ilk deger onemsiz oldugu icin _ koyup gectik ikinci degere thresh_img verdik.
#threshold keywordumuz img alıyor, thresh degeri alıyor, bunu 60 olarak ayarladık. 60 ın ustunde olanları beyaza cevırıcek.
#max degerimiz de 255 oldugu icin 255 olarak ayarladık. type ımız ise thresh_binary ve thresh_binary_inverse olarak 2 adet var.
#thresh_binary bizim 60 ile 255 arasını beyaza ceviriyorken inverse ise tam tersini yapıyor.

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

#simdi adaptive threshold yapalım peki nedir bu: normal thresholdlarda mesela bir nesnenin butunlugu aldıgı ısık mıktarına
#gore degısıyor, normalde nesne bir butun olsa bile belirli bir kısmına az ısık vurursa bir tarafı belli oluyor diger tarfı
#belli olmuyor. adaptive threshold ise komsu pikselleri alarak bir butunluk saglamaya yarıyor.

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
#simdi burada ilk olark (adaptiveThreshold yontemi kullanıyoruz, resmi koyuyoruz, max degerimizi giriyoruz, 
#ADAPTIVE_THRESH_MEAN_C ise bizim kullanacagımız yontem, thresh binary acıkladık zaten, en sondaki 8 ise bizim c sabitimiz
#ortalamadan cıkartılan deger, normalde pıozitif olur, c sabitine gore ortalama alınır ve ona gore threshold uygulanıyor,
#11 ise bloksize ımız, bu bloksize ise demistik ya ustte komsu pikseller diye onu temsil ediyor.)

plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()

#simdi resmi ice aktarıyoruz ve siyah beyaza yani gri scale ile boyuyoruz
img = cv2.imread("messi.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#resmi gorsele dokuyoruz.
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#esik degerlerini girme.
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

#burada simdi ilk deger onemsiz oldugu icin _ koyup gectik ikinci degere thresh_img verdik.
#threshold keywordumuz img alıyor, thresh degeri alıyor, bunu 60 olarak ayarladık. 60 ın ustunde olanları beyaza cevırıcek.
#max degerimiz de 255 oldugu icin 255 olarak ayarladık. type ımız ise thresh_binary ve thresh_binary_inverse olarak 2 adet var.
#thresh_binary bizim 60 ile 255 arasını beyaza ceviriyorken inverse ise tam tersini yapıyor.

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

#simdi adaptive threshold yapalım peki nedir bu: normal thresholdlarda mesela bir nesnenin butunlugu aldıgı ısık mıktarına
#gore degısıyor, normalde nesne bir butun olsa bile belirli bir kısmına az ısık vurursa bir tarafı belli oluyor diger tarfı
#belli olmuyor. adaptive threshold ise komsu pikselleri alarak bir butunluk saglamaya yarıyor.

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
#simdi burada ilk olark (adaptiveThreshold yontemi kullanıyoruz, resmi koyuyoruz, max degerimizi giriyoruz, 
#ADAPTIVE_THRESH_MEAN_C ise bizim kullanacagımız yontem, thresh binary acıkladık zaten, en sondaki 8 ise bizim c sabitimiz
#ortalamadan cıkartılan deger, normalde pıozitif olur, c sabitine gore ortalama alınır ve ona gore threshold uygulanıyor,
#11 ise bloksize ımız, bu bloksize ise demistik ya ustte komsu pikseller diye onu temsil ediyor.)

plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()

























































































































