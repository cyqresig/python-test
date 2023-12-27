from abc import ABCMeta

import cv2
import ddddocr

from src.pre_processor import WaterShedPreProcessor

'''
    算法模型处理器基类
'''
class BaseTargetDetectAlgorithm(metaclass=ABCMeta):
    def __init__(self):
        pass

    def detect_target(self, raw_pic: cv2.UMat, file_path: str = ""):
        pass


class NaiveTargetDetectAlgorithm(BaseTargetDetectAlgorithm):

    def detect_target(self, raw_pic: cv2.UMat, file_path: str = ""):
        nums, labels, stats, centroids = cv2.connectedComponentsWithStats(raw_pic)
        filtered_stats = list(filter(lambda stat: self.__filter_small_area(stat), stats))
        targets =  list(map(lambda stat: self.__compute_vertex_coordinates(stat, raw_pic), filtered_stats))

        for target in targets:
            cv2.imshow("target", target)
            cv2.waitKey(0)

        cv2.imwrite("../resource/output/target.png", raw_pic)
        return targets

    def __compute_vertex_coordinates(self, stat, raw_pic):
         left_most_x, top_most_y, width, height = stat[0], stat[1], stat[2], stat[3]
         raw_pic = cv2.rectangle(raw_pic, (left_most_x, top_most_y), (left_most_x + width, top_most_y + height), color=(0, 0, 255), thickness=2)
         return raw_pic[top_most_y:top_most_y+height, left_most_x:left_most_x+width]

    def __filter_small_area(self, stat):
        area = stat[4]
        return area > 50


class DddOCRTargetDetectAlgorithm(BaseTargetDetectAlgorithm):
    def detect_target(self, raw_pic: cv2.UMat = None, file_path: str = "../resource/output/target.png"):
        with open(file_path, 'rb') as f:
            image = f.read()
        det = ddddocr.DdddOcr(det=True)
        poses = det.detection(image)
        results = list()
        for box in poses:
            x1, y1, x2, y2 = box
            # 上到下，左到右
            sub_pic = raw_pic[y1:y2, x1:x2]
            results.append(sub_pic)
            im = cv2.rectangle(raw_pic, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
        cv2.imwrite("../resource/output/target.png", im)
        return results


if __name__ == '__main__':
    raw_target_pic = cv2.imread("../resource/WechatIMG94.jpg")
    WaterShedPreProcessor().pre_process(raw_target_pic)
    gray_pic = cv2.cvtColor(raw_target_pic, cv2.COLOR_BGR2GRAY)
    ret, im_inv = cv2.threshold(gray_pic, 20, 255, cv2.THRESH_BINARY)
    NaiveTargetDetectAlgorithm().detect_target(im_inv)