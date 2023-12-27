import random
import uuid
from abc import ABCMeta, abstractmethod

import cv2
import numpy as np


class BasePreProcessor(metaclass=ABCMeta):
    @abstractmethod
    def pre_process(self, raw_pic):
        pass


class NaivePreProcessor(BasePreProcessor):

    def pre_process(self, raw_pic):
        (height, width) = raw_pic.shape[0], raw_pic.shape[1]
        for row in range(height):
            for col in range(width):
                if self.is_close_to_black(raw_pic, row, col):
                    self.set_pixel_to_black(raw_pic, row, col)
                else:
                    self.set_pixel_to_white(raw_pic, row, col)
        return raw_pic

    # 像素点是否接近黑色
    def is_close_to_black(self, raw_pic, row, col):
        return all(0 <= channel <= 50 for channel in raw_pic[row, col])

    # 设置像素点为纯黑色
    def set_pixel_to_black(self, raw_pic, row, col):
        raw_pic[row, col] = [0, 0, 0]

    # 设置像素点为纯白色
    def set_pixel_to_white(self, raw_pic, row, col):
        raw_pic[row, col] = [255, 255, 255]


class WaterShedPreProcessor(BasePreProcessor):

    def pre_process(self, raw_pic):
        gray_pic = cv2.cvtColor(raw_pic, cv2.COLOR_BGR2GRAY)
        ret, im_inv = cv2.threshold(gray_pic, 20, 255,  cv2.THRESH_BINARY)
        # # 构建卷积核的数据集，实现模糊成像的效果
        # kernel = 1 / 16 * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        # # 使用高斯模糊对图片进行降噪
        # im_blur = cv2.filter2D(im_inv, -1, kernel)
        # im_blur = cv2.GaussianBlur(im_inv, (3, 3), 0)
        # 将图片做二值化处理，阈值设定为185，将像素值大于185的置为0，小于185的置为255
        # ret, im_res = cv2.threshold(im_blur, 20, 255, cv2.THRESH_BINARY)
        opening = cv2.morphologyEx(im_inv, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        # nums, labels, stats, centroids = cv2.connectedComponentsWithStats(im_inv)
        # contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # for contour in contours:
        #     # if cv2.contourArea(contour) < 100:
        #     mask = cv2.drawContours(opening, [contour], -1, (255, 255, 255), -1)
        #     cv2.imshow("temp", mask)
        #     cv2.waitKey(0)
        # mask = np.zeros(im_inv.shape, dtype='uint8')
        # for num in range(1, nums):
        #     area = stats[num][4]
        #     componentMask = (labels == num).astype('uint8') * 255
        #
        #     if area > 100:
        #         cv2.imshow("connected component", componentMask)
        #         cv2.waitKey(0)
        #         mask = cv2.bitwise_or(mask, componentMask)
        #         cv2.imshow("connected component", mask)
        #         cv2.waitKey(0)
                # im_inv[labels == num] = 0
        cv2.imwrite("temp" + str(random.randint(0, 100)) + ".png", opening)
        return opening


if __name__ == '__main__':
    WaterShedPreProcessor().pre_process(cv2.imread("../resource/WechatIMG94.jpg"))
    WaterShedPreProcessor().pre_process(cv2.imread("../resource/WechatIMG95.jpg"))



