import os
import glob
import cv2
import ddddocr
from PIL import Image
from rembg.bg import remove

pwd = os.getcwd()
det = ddddocr.DdddOcr(det=False, ocr=False)

slider_background_directory_path = 'temp/slider-2/background'
slider_background_validation_directory_path = 'temp/slider-2/background-validation'
slider_sprite_directory_path = 'temp/slider-2/sprite-target'
slider_crop_directory_path = 'temp/slider-2/crop-target'
slider_removebg_directory_path = 'temp/slider-2/removebg-target'
slider_validation_directory_path = 'temp/slider-2/validation'

def crop_image(input_path, output_path, coordinates):
    # 打开原始图像
    original_image = Image.open(input_path)

    # 指定裁剪区域的坐标（左上角和右下角）
    left, top, right, bottom = coordinates

    # 裁剪图像
    cropped_image = original_image.crop((left, top, right, bottom))

    # 保存裁剪后的图像
    cropped_image.save(output_path)

def remove_image_bg(input_pic_path, output_pic_path):
    # 处理图片并保存
    with open(input_pic_path, 'rb') as f_input:
        with open(output_pic_path, 'wb') as f_output:
            input_pic = f_input.read()
            output_pic = remove(input_pic)
            f_output.write(output_pic)
            # 关闭
            f_output.close()
        f_input.close()

def dddocr_validate(target_file_path, background_file_path):
    with open(target_file_path, 'rb') as f:
        target_bytes = f.read()

    with open(background_file_path, 'rb') as f:
        background_bytes = f.read()

    res = det.slide_match(target_bytes, background_bytes)
    print(res)
    return res

def paint_validation_box(box, background_file_path, background_validation_file_path):
    im = cv2.imread(background_file_path)
    x1, y1, x2, y2 = box
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    cv2.imwrite(background_validation_file_path, im)


def ocr_slider(slider_background_file_path, slider_sprite_file_path):
    png_file = os.path.basename(slider_background_file_path)
    # slider_background_file_path = os.path.join(pwd, slider_background_directory_path, png_file)
    slider_background_validation_file_path = os.path.join(pwd, slider_background_validation_directory_path, png_file)
    # slider_sprite_file_path = os.path.join(pwd, slider_sprite_directory_path, png_file)
    slider_sprite_crop_file_path = os.path.join(pwd, slider_crop_directory_path, f"crop_{png_file}")
    slider_removebg_crop_file_path = os.path.join(pwd, slider_removebg_directory_path, f"removebg_{png_file}")

    print(slider_background_file_path)
    # print(slider_background_validation_file_path)
    print(slider_sprite_file_path)
    # print(slider_sprite_crop_file_path)
    # print(slider_removebg_crop_file_path)

    print('crop_image...')
    crop_image(slider_sprite_file_path, slider_sprite_crop_file_path, (143, 495, 255, 609))

    print('remove_image_bg...')
    remove_image_bg(slider_sprite_crop_file_path, slider_removebg_crop_file_path)

    print('detect box...')
    res = dddocr_validate(slider_removebg_crop_file_path, slider_background_file_path)

    print('paint validation mark...')
    paint_validation_box(res['target'], slider_background_file_path, slider_background_validation_file_path)

    return res['target']       # [111,222,333,444]







