"""
特征提取器
从告警数据中提取多维特征向量，用于后续检测分析
"""


class FeatureExtractor:
    def __init__(self):
        pass

    def extract(self, alert: dict) -> list:
        raise NotImplementedError
