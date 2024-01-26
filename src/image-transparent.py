from PIL import Image
import numpy as np
from rembg.bg import remove
#
# def remove_background(input_path, output_path):
#     # 打开图片
#     image = Image.open(input_path)
#
#     # 将图片转为 NumPy 数组
#     img_array = np.array(image)
#
#     # 获取底色（图像的第一个像素点的颜色值）
#     background_color = tuple(img_array[0, 0, :3])
#
#     # 创建一个透明的底色掩码
#     mask = np.all(img_array[:, :, :3] == background_color, axis=-1)
#
#     # 将底色变为透明
#     img_array[mask] = [0, 0, 0, 0]  # 将透明部分的 RGB 值设为 0，透明度设为 0
#
#     # 保存处理后的图片
#     result_image = Image.fromarray(img_array)
#     result_image.save(output_path, format="PNG")
#
# # 示例使用：替换 'input.png' 和 'output.png' 为实际文件路径
# remove_background('target.png', 'target-2.png')


#待处理图片路径
input_pic_path = "target-slider-tx-1.png"

#处理后图片保存路径
output_pic_path = "target-slider-tx-1-rgb.png"

print("1")

#处理图片并保存
with open(input_pic_path,'rb') as f_input:
    with open(output_pic_path,'wb') as f_output:
        input_pic = f_input.read()
        output_pic = remove(input_pic)
        f_output.write(output_pic)
        #关闭
        f_output.close()
    f_input.close()

print("2")


# def crop_image(input_path, output_path, coordinates):
#     # 打开原始图像
#     original_image = Image.open(input_path)
#
#     # 指定裁剪区域的坐标（左上角和右下角）
#     left, top, right, bottom = coordinates
#
#     # 裁剪图像
#     cropped_image = original_image.crop((left, top, right, bottom))
#
#     # 保存裁剪后的图像
#     cropped_image.save(output_path)
#
# crop_image('sprite-target-slider-tx-1.png', 'target-slider-tx-1.png', (143, 495, 255, 609))