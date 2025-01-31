#perspektifi degistirmek neden onemli: biz yamuk olan nesnelerin tespitini yapabilyoruz ama goruntu ıslemede oyle degıl
#duz olanı ogrenırse yamuk olanı bilemeyebilir. o yuzden nesneleri cevire cevire anlamlandırmasını saglıyoruz.

import cv2
import pandas as pd
import numpy as np

#resmi ice aktarıyoruz
img = cv2.imread("ronaldo.jpg")
cv2.imshow("Original Ronaldo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resim boyutlarına bakalım
width = 550
height =450

pts1 = np.float32([[0,0],[0,height],[width,0],[width,height]])
pts2 = np.float32([[230,1],[1,472],[540,150],[338,617]])
#buraya ilk once yamuk olan & duz olup da yamultmak istedigimiz nesnemizin onceki ve olmasını istedigimiz sonraki kordinatlarını
#giriyoruz.

matrix = cv2.getPerspectiveTransform(pts1, pts2)
#1. perspektiften 2. perspektife cevirttiriyoruz.
print(matrix)

#cevirme islemini gerceklestiriyoruz.
imgOutput = cv2.warpPerspective(img, matrix, (width,height))     #burada en sondaki resmimizin olmasını istedigimiz boyudur.
cv2.imshow("Donusturulmus Resim", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()








































































































