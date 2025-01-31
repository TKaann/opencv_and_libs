#goruntuleri alt alta veya yan yana birlestirme yapabiliyoruz.
#aynı pandasta verilerimizi concat ilie yan yana veya ust uste birlestirme gibi.
#bunun onemi ise elimizdeki farklı verilerin cesitlendirilmesi acısından resimleri birlestirip nesne tespiti yapabiliriz.

import cv2
import numpy as np


img = cv2.imread("messi.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#simdi resimleri yan yana birlestirelim
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)
cv2.waitKey(0)
cv2.destroyAllWindows()

#simdi dikey sekilde ekleme yapalım
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)
cv2.waitKey(0)
cv2.destroyAllWindows()




























































































