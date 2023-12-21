import ddddocr
import cv2
import time
from PIL import Image

ocr = ddddocr.DdddOcr()

with open("target-click-selection-tx.png", 'rb') as f:
    image = f.read()

res = ocr.classification(image)

print(res)



