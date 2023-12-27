# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import ddddocr

from src.comparator import Comparator
from src.source_processor import SourceProcessor
from src.target_processor import TargetProcessor


# 入口函数
def process():
    # 处理source图
    source_processor = SourceProcessor(3)
    source_pics = source_processor.process()
    # 处理target图
    target_processor = TargetProcessor()
    target_pics = target_processor.process()
    series_num = 0

    # 无需关注，只是为了输出中间结果到图片方便比较
    for source_pic in source_pics:
        cv2.imwrite( "../resource/output/source_" + series_num.__str__() + ".png", source_pic)
        series_num = series_num + 1
    series_num = 0
    for target_pic in target_pics:
        cv2.imwrite("../resource/output/target_" + series_num.__str__() + ".png",target_pic)
        series_num = series_num + 1

    #  计算相似度进行排序
    series_num = 0
    for source_pic in source_pics:
        # 这里cos相似度越接近0，越相似
        candidates = sorted(target_pics, key= lambda x: abs(Comparator().compare(source_pic, x)))
        cv2.imwrite( "../resource/output/candidate_" + series_num.__str__() + ".png", candidates[0])
        target_pics = candidates[1:]
        series_num = series_num + 1


if __name__ == '__main__':
    process()
