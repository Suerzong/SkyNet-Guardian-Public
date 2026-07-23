"""
异常检测模型
基于机器学习的异常流量识别
"""


class AnomalyDetector:
    def __init__(self, model_path: str = None):
        self.model = None
        self.model_path = model_path

    def load_model(self):
        raise NotImplementedError

    def predict(self, features: list) -> dict:
        raise NotImplementedError
