from PIL import Image
import numpy as np

def remove_background(input_path, output_path):
    # 打开图片
    image = Image.open(input_path)

    # 将图片转为 NumPy 数组
    img_array = np.array(image)

    # 获取底色（图像的第一个像素点的颜色值）
    background_color = tuple(img_array[0, 0, :3])

    # 创建一个透明的底色掩码
    mask = np.all(img_array[:, :, :3] == background_color, axis=-1)

    # 将底色变为透明
    img_array[mask] = [0, 0, 0, 0]  # 将透明部分的 RGB 值设为 0，透明度设为 0

    # 保存处理后的图片
    result_image = Image.fromarray(img_array)
    result_image.save(output_path, format="PNG")

# 示例使用：替换 'input.png' 和 'output.png' 为实际文件路径
remove_background('target.png', 'target-2.png')