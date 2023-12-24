import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.__version__)
print(cv2.__file__)

# # 读取输入图像
# img = cv2.imread('0.png', cv2.IMREAD_UNCHANGED)
#
# # 检查图像的形状
# print(img.shape)
#
# # 保存处理后的图片
# cv2.imwrite('result-0-x.png', img)

# 截取区域的坐标和大小
x, y, width, height = 142, 492, 118, 118
# 读取图像
image = cv2.imread('0_4.png', cv2.IMREAD_UNCHANGED)

# 提取 alpha 通道
alpha_channel = image[:, :, 3]

# 截取指定区域
cropped_image = image[y:y + height, x:x + width]

# 创建新图像，设置截取区域的透明通道
new_image = np.zeros((height, width, 4), dtype=np.uint8)
new_image[:, :, :3] = cropped_image[:, :, :3]
new_image[:, :, 3] = alpha_channel[y:y + height, x:x + width]

# 保存结果
cv2.imwrite('target-slider-tx-4.png', new_image)
