from loadTool import *
import os
import cv2

fileDir = './localImage/'
fileName = 'IMG_2747.png'

with open(fileDir+ fileName, "rb") as f:
    simpleOCR(f)