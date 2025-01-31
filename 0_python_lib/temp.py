# %% numpy
"""
- matrisler için hesaplama kolaylığı sağlar
"""

import numpy as np

#1*15 boyutunda bir array-dizi oluşturma
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape)

#2 üstteki diziyi  boyutluya cevirme

dizi2 = dizi.reshape(3, 5)

print("Sekil: ", dizi2.shape)
print("Boyut: ", dizi2.ndim)
print("Tipi: ", dizi2.dtype.name)
print("Boy: ", dizi2.size)


#array type
print("Type: ",type(dizi2))



#2 boyutlu array oluşturma
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)


#sıfırlardan oluşan bir array (2 boyutlu)
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)


#birlerden oluşan bir array
bir_dizi = np.ones((3,4))
print(bir_dizi)


#bos bir array olusturma
bos_dizi = np.empty((3,4))
print(bos_dizi)


#arange (x,y,basamak)  x ten başlıyor y ye kadar gidiyor basamak kadar artarak gidiyor ama.!
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)


#linspace. bu da aynı mantıkta çalışıyor gibi ama bu bölüyor. (x,y,basamak) x ye y dahil olarak basamak kadar bölüyor bunları.
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)              # 2.5 2.5 şeklinde 10 dan başlayıp 20 ye kadar sayı oluşturmuş arasını dolurmuş.


#float array oluşturma
float_array = np.float32([[1,2],[3,4]])
print(float_array)


#matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)


#dizi elemanı toplama
print(np.sum(a))

#max değer
print(np.max(a))

#min değer
print(np.min(a))

#ortalaması
print(np.mean(a))

#medyanı        yani bodoslama ortadaki sayı.
print(np.median(a))

#rastgele sayı üretme  [0,1] arasında olacak ve sürekli dağılım olacak uniform dağılım. 3*3 lük bir matris oluşturucaz.
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

#indeks işlemleri. numpy ile bir arrayin içindeki indexlere bakma
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk 4 elemanı
print(dizi[:4])

#dizinin tersinli alma
print(dizi[::-1])               # : : -1 bize dizinin tersini verir.. listelerdeki reverse nin karşılığı

#indeksleri ve dilimleri inceleyelim. bunun için 2 boyutlu dizi oluşturalım
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1. satır ve 1ç sütundaki elemanını yazdırma. ama burada 1. satır 1. sütun derken index cinsinden bahsediyorum.
print(dizi2D[1,1])

#dizinin 1. sütununun tüm satırlarını arlıcaz.
print(dizi2D[:,1])          # ilki satır olduğu için tüm satırları alacağımızdan : koyuyoruz sonrasında hangi sütunsa onu.

#1. satır 1,2,3. sütunları alma.
print(dizi2D[1,1:4])

#dizi son satır tüm sütunlar
print(dizi2D[-1, :])



#diziyi vektör haline getirme. yeni bir dizi oluşturuyoruz.     RAVEL
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

#vektor haline geitiriyoruz.
vektor = dizi2D.ravel()     #ravel komutu dizileri vektör haline getirmemizi sağlıyor..
print(vektor)


#bunun karşılığı, işe yaradığı nokta ise: neural networkde özellikleri çıkarttıktan sonra sınıflandırma yapıcaz,
#bu özellik katmanlarınının en sonunda sınıflandırma yapabilcek olan neural networke giriş yapmak için bir vektöre
#ihtiyacımız var bu nedenle en sondaki resmi vektör haline getirmemiz gerekiyor. resimler 2 boyutlu olduğu için
#bizim düzleştirmemiz gerekiyor. sonra sınıflandırmaya sokucaz. eğer renkliyse 3 boyutlu ama normalde 2 boyutlu


#maksimum sayının indexini bulma
maks_sayinin_index_bulma = vektor.argmax()
print(maks_sayinin_index_bulma)


#PANDASA GECİSS

# %% pandas

"""
-hızlı güçlü ve esnek
"""

import pandas as pd

#sozluk olusturuyoruz.

dictionary = {"isim": ["ali","veli","kenan","ayse"],
              "yas": [15,16,17,35],
               "maas": [244,452,637,835]}

#bu sozlugu simdi dataframe'e ceviricez

veri = pd.DataFrame(dictionary)

#ilk 2 satır
print(veri.head(2))

#sutunları yazdirma
print(veri.columns)

#veri bilgisi
print(veri.info())

#istatistiksel özellikler
print(veri.describe())

#sadece yas sutununu yazdırma
print(veri["yas"])

#yeni bir sutun eklemek
veri["sehir"] = ["istanbul", "bartin", "denizli","london"]
print(veri)

#yas sutunu yazdırma
print(veri.loc[:,"yas"])

#yas sutununun icindeki 3 satır alma
print(veri.loc[:2,"yas"])            #buradaki girilen index dahil oluyor, numpydan farklı olarak.

#yas ve sehir arası sutununun icindeki 3 satır alma
print(veri.loc[:2,"yas":"sehir"])  

#simdi de sadece isim ve yas ı alma
print(veri.loc[:2,["isim","yas"]])  

#satırları tersten yazdirma
print(veri.loc[::-1,:])

#yas sutununu iloc ile yazdırma.    iloc yani index location demek
print(veri.iloc[:,1])

#iloc ile ilk 3 satır yazdırma yas ve isim.         burada farklı olarak yazdığımız sayınin indexi sahil değil.
print(veri.iloc[:3,[0,1]])


#filtreleme

dictionary = {"isim": ["ali","veli","kenan","ayse"],
              "yas": [15,16,17,35],
               "sehir": ["istanbul", "bartin", "denizli","london"]}

veri = pd.DataFrame(dictionary)
print(veri)

#ilk olarak yasa gore filtre olusturalım. bu filtre yas > 20 olsun
filtre1 = veri.yas > 20
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

#ortalama yas bulma
ortalama_yas = veri.yas.mean()

#yeni bir kolon olusturuyoruz yas_grubu adında. yası ortalamadan kucuk olanlara kucuk buyuk olanlara buyuk yazdırdık.
veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

#verileri birlestirme, yatay ve dikeyde birlestirme

sozluk1 = {"isim": ["ali","veli","kenan"],
              "yas": [15,16,17],
               "sehir": ["istanbul", "bartin", "denizli"]}

veri1 = pd.DataFrame(sozluk1)

#veriseti 2 yi olusturalım 

sozluk2 = {"isim": ["kaan","ayse","deniz"],
              "yas": [23,22,21],
               "sehir": ["london", "izmir", "konya"]}

veri2 = pd.DataFrame(sozluk2)

#simdi bu verileri dieyde birlestirelim.
veri_dikey = pd.concat([veri1,veri2], axis = 0)     #dikeyde oldugu için axis = 0 yaptık.

#yatay birlestirme
veri_yatay = pd.concat([veri1,veri2], axis = 1)     #yatayda birlestirmek istediğimiz için axis = 1 yaptık.



# %% matplotlib
"""
- verileri görsellestirmemize yarıyor.
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()
plt.plot(x,y, color = "red", alpha = 0.5, label = "Line")
plt.scatter(x,y, color = "blue", alpha = 0.4, label = "Scatter")
plt.title("Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend()        #labeli ekledikten sonra görmek için legendi kullanmamız gerek.
plt.show()


fig, axes = plt.subplots(2,1, figsize=(9,7))
fig.subplots_adjust(hspace = 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]


axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(x,y)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")  
axes[1].set_xlabel("sub-2 x")





#random sayılardan resim olusturma
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray")      # 0 (Siyah)  1 (Beyaz) ->  0.5 (Gri)
#plt.imshow(img)    #random yapıyoruz gri veya baika bişey demiyoruz. ama genelde gri kullanırız.
#plt.axis("off")        #figurun etrafındaki kordinatları gosterir
plt.show()

#burada kordinat sistemi normalden farklıdır. sol üst 0 a 0 iken sağ alt max a max dır.




# %% OS kütüphanesi

import os

print(os.name)

currentDir = os.getcwd()
print(currentDir)

#new folder 
folder_name = "new_folder"
os.mkdir(folder_name)

#rename yapma
new_folder_name = "new_folder_2"
os.rename(folder_name, new_folder_name)

#folder içine gitme
os.chdir(currentDir)
print(os.getcwd())

#file isimlerini cagirma
files = os.listdir()

#sonu bununla bitenler..
for f in files:
    if f.endswith("2"):
        print(f)
        

#bir dosyayı silme
os.rmdir(new_folder_name)


#verdiğimiz bir klasorun altındaki dizinleri ve dosyaları goruntuleyecegimiz ornek kod..
for i in os.walk(currentDir):
    print(i)
    

#aradıgımız dosya var mı yok mu kontrol etme.
os.path.exists("temp.py")




























































