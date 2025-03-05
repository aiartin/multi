from pdf2image import convert_from_path
import pytesseract
import os
import cv2

def ocr(path):
    pages = ""
    images = convert_from_path(path, 500)
    for i, image in enumerate(images):
        fname = "image" + str(i) + ".jpg"
        image.save(fname, "JPEG")
        text = pytesseract.image_to_string(cv2.imread(fname))
        os.remove(fname)
        pages = pages + " " + text
    return pages


print(ocr("data.pdf"))