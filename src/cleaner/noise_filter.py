"""
噪声过滤器
规则+大模型双层降噪，过滤已知误报和冗余告警
"""


class NoiseFilter:
    def __init__(self):
        pass

    def filter(self, alerts: list) -> list:
        raise NotImplementedError
