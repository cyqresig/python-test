import ddddocr
import cv2
import time
from PIL import Image

det = ddddocr.DdddOcr(det=True)

with open("background-click-selection-tx-process.png", 'rb') as f:
    image = f.read()

poses = det.detection(image)
print(poses)

im = cv2.imread("background-click-selection-tx-process.png")

for box in poses:
    x1, y1, x2, y2 = box
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

cv2.imwrite("result-background-click-selection-tx-process.png", im)


# ocr = ddddocr.DdddOcr()
#
# # 处理检测到的文本区域
# index = 0;
# for result in poses:
#     # 获取文本区域的坐标
#     x1, y1, x2, y2 = result
#     y = y1
#     x = x1
#     h = y2 - y1
#     w = x2 - x1
#     # 切割图像，传递给 OCR 进行文本识别
#     # text_image = image[y:y + h, x:x + w]
#     # 获取当前时间戳（整数形式）
#     timestamp_float = time.time()
#     timestamp_int = int(timestamp_float)
#     text_image = Image.open("background-click-selection-tx.png").crop((x, y, x + w, y + h))
#
#     # 保存切割后的图像
#     save_path = f'text_region_{index}.png'
#     text_image.save(save_path)
#     index = index + 1
#
#     # 使用 OCR 进行文本识别
#     res = ocr.classification(text_image)
#
#     print(res)



