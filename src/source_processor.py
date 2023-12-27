import copy

import cv2

from src.pre_processor import WaterShedPreProcessor, NaivePreProcessor

''' 
    源图片处理器，源图片这里指验证码识别中的小图，
    即需要用户根据该小图来进行大图的点选
'''
class SourceProcessor:
    def __init__(self, width_split_nums, source_pic_path = "../resource/source.png", pre_processor=NaivePreProcessor()):
        self.width_split_nums = width_split_nums
        self.source_pic_path = source_pic_path
        self.pre_processor = pre_processor



    def process(self) -> list():
        raw_source_pic = cv2.imread(self.source_pic_path)
        raw_source_pic = self.pre_processor.pre_process(raw_source_pic)

        cv2.imwrite("../resource/output/source.png", raw_source_pic)
        (height, width) = raw_source_pic.shape[0], raw_source_pic.shape[1]
        split_width = width // self.width_split_nums
        results = list()
        for cur_width_split_num in range(self.width_split_nums):
            start_width = cur_width_split_num * split_width
            end_width = (cur_width_split_num + 1) * split_width
            sub_pic = raw_source_pic[0:height, start_width:end_width]
            results.append(sub_pic)
            cur_width_split_num += cur_width_split_num + 1
        return results
