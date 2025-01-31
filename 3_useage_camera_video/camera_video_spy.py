import cv2

#capture
cap = cv2.VideoCapture(0)    #0 bizim default kameramızdır.

#kameramızın yukseklık ve genislik degerlerine bakalım
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)


#frameleri tek tek okumadan once video kaydedicimizi baslatıcaz.
#frameler okundukca ve bilgisayarmızda gorsellestirildikce paralelden bu video kaydediciye kaydedilecek.

#video kaydetme
writer = cv2.VideoWriter("video_kaydi_2.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))
#buradaki VideoWriter videoyu kaydetmemize yarıyor. fourcc ise windowsta geçerli kılıyor. 20 fps degerimiz oluyor.
#width ve height ise zaten kameramızın boyunu atıyor.
#forcc: cerveceveleri sıkıstırmak icin dort karakterlı codec kodudur.


#Sımdı videomuzu okumaya geldik.
while True:
    
    ret, frame = cap.read()     #framelerimizin gelip gelmedigini ret icine aktarıyoruz. geldigi surece True kalıyor.
    cv2.imshow("Video",frame)
    
    #kayıt etme, yukarda ayarladıgımız writer ile kayıt islemini paralelde yapıcaz.
    writer.write(frame)   #frame leri kaydediyoruz.
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break     #q tusuna basarsak cıkıs yapıyoruz.
        
cap.release()   #capture i serbest bırakıyoruz.
writer.release()   #writer i serbest bırakıyoruz. yani writera yazma islemini bitirttiriyoruz.
cv2.destroyAllWindows()  #acık kalan butun pencerelerı kapattırıyoruz en sonunda.































































































