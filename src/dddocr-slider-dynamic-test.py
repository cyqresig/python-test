import ddddocr
import cv2
import sys

# 获取命令行参数
# sys.argv[0] 是脚本的名称，后面的元素是传递的参数
args1 = sys.argv[1:]
args2 = sys.argv[2:]

# 打印参数
print("Received command line arguments:", args1, args2)

det = ddddocr.DdddOcr(det=False, ocr=False)

# with open('target.png', 'rb') as f:
with open('target-slider-tx.png', 'rb') as f:
    target_bytes = f.read()

with open('background-slider-tx.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)

im = cv2.imread("background-slider-tx.png")

x1, y1, x2, y2 = res['target']
im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

cv2.imwrite("result-background-slider-tx.png", im)