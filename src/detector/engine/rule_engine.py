"""
规则引擎核心
加载规则集并对告警进行快速匹配
"""


class RuleEngine:
    def __init__(self):
        pass

    def match(self, alert: dict) -> dict:
        raise NotImplementedError
