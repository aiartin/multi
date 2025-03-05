#! /bin/bash

apt-get install -y libopencv-dev libgl1-mesa-glx ffmpeg libsm6 libxext6 poppler-utils tesseract-ocr 

fastapi run main.py