import ddddocr
import cv2

det = ddddocr.DdddOcr(det=False, ocr=False)

# with open('target.png', 'rb') as f:
with open('target-slider-tx-7.png', 'rb') as f:
    target_bytes = f.read()

with open('background-slider-tx-7.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)

im = cv2.imread("background-slider-tx-7.png")

x1, y1, x2, y2 = res['target']
im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

cv2.imwrite("result-background-slider-tx-7.png", im)