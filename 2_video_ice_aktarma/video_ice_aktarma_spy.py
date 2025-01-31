import cv2
import time

#video ismi
video_name = "MOT17-04-DPM.mp4"

#video ice aktar: capture dir ve genelde cap diye kısaltılır.
cap = cv2.VideoCapture(video_name)

#videonun boyutları
print("Genislik: ", cap.get(3))      #get fonksiyonunun 3. idexi bize genisligi
print("Yukseklık: ", cap.get(4))     #4. inceksi bize yuksekligi verir

#opencv video aktarma esnasında, aktardığımız dosya video olsa da başka bir şey olsa da aktarmaya devam edecektir.
#o yüzden bunu kontrol etmemiz gerekli, bunu isOpened fonksiyonu ile kontrol ediyoruz. bunu atlamamamız gerekiyor.
if cap.isOpened() == False:
    print("Hata")
#simdi bir hata mesajı dondurmedi yani dosyamız acılabiliyor.

#videoyu aktardık, simdi videoyu okuyoruz.
#read fonksiyonu bize 2 tane veri döndürüyor, birincisi return ikincisi frame
#frame dedigimiz sey videonun icinde bulunan her bir resim oluyor
#return dedigimiz sey ise bu islemin basarılı olup olamadıgıdır. eger cap.read basarısız olursa bize false dondurecek.

ret, frame = cap.read()

#cap.read ın bize frame dondurme isleminin basarılı olup olmadıgını kontrol ediyoruz.

while True:     #burada aslında video dedigimiz sey cok fazla resmin ard arda oynaması oldugu icin while kullanıyoruz.
                #bu resimleri video haline getirmek için return true oldugu surece oynatıyoruz.
        
    ret, frame = cap.read()    #bunu while dongusununun icine alıyoruz ki surekli capture okuyabilsin.
    
    #frame = cv2.resize(frame, (960, 540))     #istersek burdak videonun boyutunu degistirebiliyoruz.
    
    if ret == True:

        time.sleep(0.01) #bunu yapmamızın sebebi ard arda resimleri cok hızlı oynatacagı icin her birinin arasında sleep koyduk.
                            #bunu kullanmazsak cok hızlı akacaktır.

        cv2.imshow("Video", frame)
        
    else: break      #videoda gosterilcek bisey kalmamıssa return etmiyorsa artık videonun sonuna gelcek ve cikacak
        
    if cv2.waitKey(1) & 0xFF == ord("q"):  #burada ise kendimiz q ya basarak cikiyoruz.
        break

cap.release()   #stop capture, artık video yakalamayı birakiyoruz.
cv2.destroyAllWindows()

# %% hocanın yaptıgı

import cv2
import time 

# video ismi
video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name) # capture video
print("Genişlik: ",cap.get(3)) 
print("Yükseklik: ", cap.get(4))

if cap.isOpened() == False:
    print("Error")
    
    
while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (960, 540))
    
    if ret == True:
        
        time.sleep(0.01) # bunu kullanmazsak video çok hızlı gider.
        
        cv2.imshow("Video",frame)
        
    else: break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release() # stop capture
cv2.destroyAllWindows() 























































