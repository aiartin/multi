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
    pages = []
    for i, image in enumerate(images):
        print(prefix+" ",i)
        fname = prefix + str(i) + ".jpg"
        image.save(fname, "JPEG")
        text = pytesseract.image_to_string(cv2.imread(fname))
        os.remove(fname)
        pages.append(text) 
    return pages


def getimages(path):
    images = convert_from_path(path, 500,poppler_path=r'C:/Users/Extentia/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin')
    print(len(images))
    return images

# def strt():
#     images = getimages("data.pdf")
#     timeresult = {}
#     start_time = time.time()
#     chunks = []
#     chunk = 9
#     chunk_size = int(len(images)/chunk)
#     for i in range(0, len(images), chunk_size):
#         chunks.append(images[i:i + chunk_size])
#     print(len(chunks))
#     threadarray = []
#     prefix = 0
#     for i in chunks:
#         pre = "p"+str(prefix)
#         thread = CustomThread(target=ocr, args=(i,pre))
#         thread.start()
#         threadarray.append(thread)
#         prefix = prefix+1
#     results = []
#     for thread in threadarray:
#         results.append(thread.join())
#     timetaken = time.time() - start_time
#     print(results)

#     singlearray = []

#     for result in results:
#         for res in result:
#             singlearray.append(res)

#     print("--- %s seconds ---" % timetaken)
#     timeresult["numthread"] = timetaken

#     print(timeresult)



#     print(singlearray)



def strt():
    images = getimages("data2.pdf")
    timeresult = {}
    chunks = []
    chunk = 9
    chunk_size = int(len(images)/chunk)
    print(chunk_size)
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
    results = []
    for thread in threadarray:
        results.append(thread.join())
    print(results)

    singlearray = []

    for result in results:
        for res in result:
            singlearray.append(res)

    print(timeresult)
    print(singlearray)

strt()