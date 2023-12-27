import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.__version__)
print(cv2.__file__)

# 读取输入图像
img = cv2.imread('0.png', cv2.IMREAD_UNCHANGED)
# img = cv2.imread('00.png', cv2.IMREAD_UNCHANGED)

# 检查图像的形状
print(img.shape)

target_color=(150, 150, 150)
tolerance=10
# 定义目标颜色范围
lower_bound = np.array([target_color[0] - tolerance, target_color[1] - tolerance, target_color[2] - tolerance, 0], dtype=np.uint8)
upper_bound = np.array([target_color[0] + tolerance, target_color[1] + tolerance, target_color[2] + tolerance, 255], dtype=np.uint8)

# 创建掩码，选择目标颜色范围内的像素点
mask = cv2.inRange(img, lower_bound, upper_bound)

# 将满足条件的像素点变成透明
img[mask != 0] = [0, 0, 0, 0]

# 保存处理后的图片
cv2.imwrite('result-0.png', img)
# cv2.imwrite('result-00.png', img)


# # 将图片转换为灰度图
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # 设置阈值，将灰度值在指定范围内的像素置为透明
# lower_threshold = 100  # 设置灰度范围下限
# upper_threshold = 150  # 设置灰度范围上限
#
# # 创建一个二值化的掩码
# mask = cv2.inRange(gray, lower_threshold, upper_threshold)
#
# # 将满足条件的像素点变成透明
# img[mask != 0] = [0, 0, 0, 0]

