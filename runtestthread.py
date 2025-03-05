from pdf2image import convert_from_path
import pytesseract
import os
import cv2
from threading import Thread


import time
start_time = time.time()

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"



class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, verbose=None):
        # Initializing the Thread class
        super().__init__(group, target, name, args, kwargs)
        self._return = None

    # Overriding the Thread.run function
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return




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
timeresult = {}
for numthread in range(1 , len(images)):
    start_time = time.time()
    chunks = []
    chunk = numthread
    chunk_size = int(len(images)/chunk)


    for i in range(0, len(images), chunk_size):
        chunks.append(images[i:i + chunk_size])


    print(len(chunks))

    threadarray = []
    prefix = 0
    for i in chunks:
        pre = "p"+str(prefix)
        thread = CustomThread(target=ocr, args=(i,pre))
        thread.start()
        threadarray.append(thread)
        prefix = prefix+1

    result = []

    for thread in threadarray:
        result.append(thread.join())


    timetaken = time.time() - start_time
    print(result)

    print("--- %s seconds ---" % timetaken)

    timeresult["numthread"] = timetaken


print(timeresult)