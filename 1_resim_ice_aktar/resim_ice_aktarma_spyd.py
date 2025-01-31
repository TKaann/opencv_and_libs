import cv2

#ice aktarma
img = cv2.imread("messi.jpg", 0)     #buradaki sıfır resmi siyah beyaz yani gri olarak aktarmayı saglar

#gorsellestirme
cv2.imshow("Ilk Resim", img)


#esc ye basınca cikis yapan s ye basınca kaydeden kodumuz.
k = cv2.waitKey(0) &0xFF
if k == 27:       #27 klavyedeki esc tuşunun sayısal degeridir.
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.jpg", img)
    cv2.destroyAllWindows()






















































