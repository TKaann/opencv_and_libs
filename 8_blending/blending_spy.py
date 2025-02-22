import cv2
import matplotlib.pyplot as plt

#resimleri yukleme ve renklerini duzeltme
img1 = cv2.imread("ronaldo.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("messi.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#simdi bunların boylarına bakalım. boylarının aynı olması lazım cunku farklı boyutlardaki matrisler toplanamaz. aynı yapıcaz.
print(img1.shape)
print(img2.shape)

#yeniden boyutlandırıyoruz.
img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2, (600,600))
print(img2.shape)

#fotografları getirelim
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#simdi resimleri karıstırıyoruz bu ise söyle oluyor: alpha*img1 + beta*img2  seklinde
blended = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blended)













































































































