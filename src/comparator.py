import cv2
import numpy as np
from scipy import spatial

'''
    相似度比较器
'''
class Comparator:

    def __init__(self):

        pass

    def compare(self, source, target):
        source_vectors = self.__extract_sift_feature(source, 30)
        target_vectors = self.__extract_sift_feature(target, 30)
        # 特征矩阵算相似度，-1-1之间的一个浮点数
        score = spatial.distance.cdist(source_vectors, target_vectors, 'cosine').sum()
        return score


    def __extract_sift_feature(self, source, vector_size):
        # 特征检测器
        sift = cv2.SIFT.create()
        # 拿到所有特征
        keypoints = sift.detect(source)
        # 排序所有特征并筛选前vector_size个
        keypoints = sorted(keypoints, key=lambda keypoint: -keypoint.response)
        keypoints = keypoints[:vector_size]
        # 计算特征
        keypoints, descriptors = sift.compute(source, keypoints)
        # 特征展开成矩阵
        # [1,2,3]
        vectors = descriptors.flatten()
        # 一个特征扩成128维，如果不够，直接补0
        vector_length = vector_size * 128
        if vectors.size < vector_length:
            vectors = np.concatenate((vectors, np.zeros(vector_length - vectors.size)))
        #
        return vectors.reshape(-1, 128 * vector_size)







