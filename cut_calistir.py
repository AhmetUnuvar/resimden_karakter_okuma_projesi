import pytesseract.pytesseract
from PIL import Image
import cv2
import numpy as np
import tkinter as tk
pytesseract.pytesseract.tesseract_cmd="C:\\Users\\unuva\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


img = cv2.imread("hastaMonitor.PNG")
rows , cols ,_ = img.shape
print("Rows", rows)
print("Cols",cols)

#seksendort cutting
cut_image_seksendort = img[12:60 , 217:270]
cv2.imshow("hastaMonitorKirpilmis.PNG",cut_image_seksendort)
cv2.imshow("image",img)
cv2.waitKey(0)

# seksendort yeni resim kaydetme

yeni_kayit_seksendort = cv2.imread("seksendort.PNG")
cv2.imwrite("seksendort.PNG",cut_image_seksendort)

# ekrana yazdır 84

def image_to_text_seksendort(image_path_seksendort):
    image_seksendort=Image.open(image_path_seksendort)
    text_seksendort = pytesseract.image_to_string(image_seksendort)
    return text_seksendort
image_path_seksendort = "seksendort.PNG"
text1="EKG :" + image_to_text_seksendort(image_path_seksendort)
print(text1)

# doksandort - seksenbes cutting
cut_image_doksandort_seksenbes = img[60:150 , 215:255]
cv2.imshow("doksandort_seksenbesKirpilmis.PNG",cut_image_doksandort_seksenbes)
cv2.waitKey(0)

# doksandort_seksenbes yeni kayıt
yeni_kayit_doksandort_seksenbes = cv2.imread("doksandort_seksenbes.PNG")
cv2.imwrite("doksandort_seksenbes.PNG",cut_image_doksandort_seksenbes)

# 9485 ekrana yazdır
def image_to_text_doksandort_seksenbes(image_path_doksandort_seksenbes):
    image_doksandort_seksenbes = Image.open(image_path_doksandort_seksenbes)
    text_doksandort_seksenbes = pytesseract.image_to_string(image_doksandort_seksenbes)
    return text_doksandort_seksenbes
image_path_doksandort_seksenbes = "doksandort_seksenbes.PNG"
text2 = "SPO2A : "+ image_to_text_doksandort_seksenbes(image_path_doksandort_seksenbes)
print(text2)

# onüc cutting

cut_image_onuc = img[100:230 , 210:290]
cv2.imshow("onuc.PNG",cut_image_onuc)
cv2.waitKey(0)

# onuc yeni resim kaydetme
yeni_kayit_onuc = cv2.imread("onuckirpilmis.PNG")
cv2.imwrite("onuckirpilmis.PNG",cut_image_onuc)

# ekrana yazdır onuc

def image_to_text_onuc(image_path_onuc):
    image_onuc = Image.open(image_path_onuc)
    text_onuc = pytesseract.image_to_string(image_onuc)
    return text_onuc
image_path_onuc = "onuckirpilmis.PNG"
text3 = "Resp ECG :" + image_to_text_onuc(image_path_onuc)
print(text3)

# yuzyirmibir cutting

cut_image_yuzyirmibir = img[230:315 , 170:300]
cv2.imshow("yuzyirmibir.PNG",cut_image_yuzyirmibir)
cv2.waitKey(0)

# yuzyirmibir yeni resim kaydetme
yeni_kayit_yuzyirmibir = cv2.imread("yuzyirmibirkirpilmis.PNG")
cv2.imwrite("yuzyirmibirkirpilmis.PNG",cut_image_yuzyirmibir)

# ekran yazdırma 121
def image_to_text_yuzyirmibir(image_path_yuzyirmibir):
    image_yuzyirmibir = Image.open(image_path_yuzyirmibir)
    text_yuzyirmibir = pytesseract.image_to_string(image_yuzyirmibir)
    return text_yuzyirmibir
image_path_yuzyirmibir = "yuzyirmibirkirpilmis.PNG"
text4 = image_to_text_yuzyirmibir(image_path_yuzyirmibir)
print(text4)

def tk_yazdir():
    cikti = text1 , text2 , text3 , text4
    output_label.config(text=cikti)

root = tk.Tk()
root.title("Arayüz")

output_label = tk.Label(root, text="",font=("Arial",12))
output_label.pack(pady=20)

show_button = tk.Button(root,command=tk_yazdir())
show_button.pack()
root.mainloop()


