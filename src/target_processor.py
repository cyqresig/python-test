import cv2
import numpy as np
import ddddocr

from src.pre_processor import WaterShedPreProcessor
from src.target_detect_algorithm import DddOCRTargetDetectAlgorithm

''' 
    目标图片处理器，目标图片这里指验证码识别中的大图，
    即需要用户手动点选的图
'''
class TargetProcessor:
    def __init__(self, target_pic_path ="../resource/target.png", output_target_pic_path = "../resource/output/", pre_processor=WaterShedPreProcessor(), target_detect_algorithm=DddOCRTargetDetectAlgorithm()):
        self.target_pic_path = target_pic_path
        self.output_target_pic_path = output_target_pic_path
        self.pre_processor = pre_processor
        self.target_detect_algorithm = target_detect_algorithm

    def process(self) -> list:
        raw_target_pic = cv2.imread(self.target_pic_path)
        raw_target_pic = self.pre_processor.pre_process(raw_target_pic)
        isSuccess = cv2.imwrite(self.output_target_pic_path + "target.png", raw_target_pic)
        if not isSuccess:
            print("cv2 write error")
            return list()
        results = self.target_detect_algorithm.detect_target(raw_target_pic)
        return results
            # im = cv2.rectangle(raw_target_pic, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)


if __name__ == '__main__':
    TargetProcessor().process()