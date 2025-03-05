from pdf2image import convert_from_path
import pytesseract
import os
import cv2
from threading import Thread


import time
start_time = time.time()

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def ocr(images , prefix):
    pages = ""
    for i, image in enumerate(images):
        print(prefix+" ",i)
        fname = prefix + str(i) + ".jpg"
        image.save(fname, "JPEG")
        text = pytesseract.image_to_string(cv2.imread(fname))
        os.remove(fname)
        pages = pages + " " + text
    return pages

def getimages(path):
    images = convert_from_path(path, 500,poppler_path=r'C:/Users/Extentia/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin')
    return images

images = getimages("data.pdf")
result = ocr(images , "p1")

print(result)

print("--- %s seconds ---" % (time.time() - start_time))