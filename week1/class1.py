
"""
ideal_gas.py

本模块提供理想气体相关的热力学计算函数。
"""

class IdealGas:
    """表示一个理想气体系统，封装状态变量与热力学计算方法。"""

    def __init__(self, v, t, n):
        """初始化理想气体实例。

        Args:
            v: 体积，单位立方米
            t: 绝对温度，单位开尔文
            n: 粒子数
        """
        self.v = v
        self.t = t
        self.n = n

    def pressure(self):
        """计算当前状态下的气体压强，单位帕斯卡。"""
        k = 1.38e-23  # 玻尔兹曼常数
        return self.n * k * self.t / self.v


