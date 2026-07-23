"""
大模型决策模块
轻量化大模型对安全事件进行智能研判与自动处置
"""


class LLMJudge:
    def __init__(self):
        pass

    def judge(self, alert: dict) -> dict:
        raise NotImplementedError
