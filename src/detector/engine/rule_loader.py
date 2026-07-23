"""
规则加载器
从配置文件加载安全检测规则
"""


class RuleLoader:
    def __init__(self):
        pass

    def load(self, path: str) -> list:
        raise NotImplementedError
