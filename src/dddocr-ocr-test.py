import ddddocr
import cv2
import time
from PIL import Image

ocr = ddddocr.DdddOcr()

# with open("temp/click-selection/background/selection-background.png", 'rb') as f:
with open("temp/click-selection/target/selection-target.png", 'rb') as f:
    image = f.read()

res = ocr.classification(image)

print(res)



