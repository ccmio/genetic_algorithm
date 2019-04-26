import numpy as np


class Mutate:
    def __init__(self, children, mp):
        self.children = children
        self.mp = mp

    def mutation(self):
        for i in range(len(self.children)):
            if self.mp >= np.random.uniform(0, 1):
                key = np.random.randint(0, len(self.children[i]))
                if key == 0:
                    self.children[i][key] = np.random.randint(1, 6)
                else:
                    self.children[i][key] = np.random.randint(1, 4)
        return self.children
