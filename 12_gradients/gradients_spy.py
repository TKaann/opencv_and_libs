#goruntu gradyanları goruntudeki yogunluk veya renkteki yonlu bir degisikliktir
#kenar algılamada kullanılır. laplacian gradyan kullanılır kenar tespitinde

#simdi ornek bir sudoki fotografındaki kenarları bulucaz
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original Img")

#simdi gradyanlarını bulucaz. X eksenindeki gradyanları bulalım.
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize = 5)
#ddepth parametremiz outputun derinligini gosteriyor, bunu cv2.CV_16S yapıyoruz. dx = 1 X yonunde oldugunu soyluyor.
#dy = 0 ise Y yonunde degıl yani false 0 degerini giriyoruz. Kernal size ımız ise 5 yani 5 e 5 bir kutucuk yapıyoruz.
plt.figure(), plt.imshow(sobelx, cmap="gray"), plt.axis("off"), plt.title("Sobel X")

#simdi Y eksenindeki gradyanları bulalım.
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize = 5)
plt.figure(), plt.imshow(sobely, cmap="gray"), plt.axis("off"), plt.title("Sobel Y")

#her ikisini de aynı anda tespit etmek için ise : laplacian gradients yapıyoruz.
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)    #buraya x ve y eksenleri eklemiyoruz cunku her  2 yone de yapıyoruz.
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("Laplacian Img")















































































































