# 交叉算子
import numpy as np


class Cross:
    def __init__(self, buildings_new, cp):
        self.bn = buildings_new
        self.cp = cp

    # 单点交叉
    def crossover(self):
        children = []
        half = int(len(self.bn)/2)
        father = self.bn[:half]
        mother = self.bn[half:]
        np.random.shuffle(father)
        np.random.shuffle(mother)

        for i in range(half):
            if self.cp >= np.random.uniform(0, 1):
                key = np.random.randint(0, int(len(father[i])))
                son = father[i][: key] + (mother[i][key:])
                daughter = mother[i][: key] + (father[i][key:])
            else:
                son = father[i]
                daughter = mother[i]
            children.append(son)
            children.append(daughter)

        return children
