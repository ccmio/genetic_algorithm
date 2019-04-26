#选择算子
import random
import math


class Select:
    def __init__(self, buildings, value):
        self.buildings = buildings
        self.value = value

    def selection(self):

        fitness_sum = []
        buildings_new = []
        sumx = 0
        # softmax函数处理个人加权分值，可扩大化差异并获得较理想的收敛结果
        for values in self.value:
            sumx += math.exp(values)
        # 轮盘赌算法模拟优胜劣汰
        for i in range(len(self.value)):
            if i == 0:
                fitness_sum.append(math.exp(self.value[i])/sumx)
            else:
                fitness_sum.append(math.exp(self.value[i])/sumx + fitness_sum[i-1])

        for i in range(len(self.value)):
            rand = random.uniform(0, 1)
            for j in range(len(self.value)):
                if j == 0:
                    if 0 < rand <= fitness_sum[j]:
                        buildings_new.append(self.buildings[j])
                else:
                    if fitness_sum[j-1] < rand <= fitness_sum[j]:
                        buildings_new.append(self.buildings[j])

        return buildings_new





