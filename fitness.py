# 适应度函数直接使用5个位置基因的加权总分
class Fit:
    def __init__(self, buildings, rain, land, money, location, prefer):
        self.buildings = buildings
        self.rain = float(rain)
        self.land = float(land)
        self.money = float(money)
        self.location = float(location)
        self.prefer = float(prefer)

    def fitness(self):
        value = []
        # 设定不同位置基因的不同权重
        # 一号位基因即为self.buildings[i][0]：1代表A11，2代表A12....5代表A15，其余以此类推
        for i in range(len(self.buildings)):
            if self.buildings[i][0] == 1:
                m1, m2, m3, m4 = 2, 5, 5, 4
            if self.buildings[i][0] == 2:
                m1, m2, m3, m4 = 2, 4, 4, 5
            if self.buildings[i][0] == 3:
                m1, m2, m3, m4 = 4, 3, 3, 3
            if self.buildings[i][0] == 4:
                m1, m2, m3, m4 = 5, 1, 3, 2
            if self.buildings[i][0] == 5:
                m1, m2, m3, m4 = 5, 1, 5, 2

            if self.buildings[i][1] == 1:
                n1, n2, n3 = 4, 3, 5
            if self.buildings[i][1] == 2:
                n1, n2, n3 = 3, 3, 5
            if self.buildings[i][1] == 3:
                n1, n2, n3 = 5, 4, 4

            if self.buildings[i][2] == 1:
                p1, p2, p3 = 2, 4, 3
            if self.buildings[i][2] == 2:
                p1, p2, p3 = 3, 5, 3
            if self.buildings[i][2] == 3:
                p1, p2, p3 = 5, 3, 4

            if self.buildings[i][3] == 1:
                o1, o2, o3 = 5, 5, 3
            if self.buildings[i][3] == 2:
                o1, o2, o3 = 4, 4, 1
            if self.buildings[i][3] == 3:
                o1, o2, o3 = 1, 1, 5

            if self.buildings[i][4] == 1:
                u1, u2, u3 = 5, 5, 3
            if self.buildings[i][4] == 2:
                u1, u2, u3 = 4, 4, 1
            if self.buildings[i][4] == 3:
                u1, u2, u3 = 1, 1, 5
            # 包含既定条件的基因权值和计算：
            a1 = ((0.3 + 0.2 * self.rain) * m1 + (0.3 + 0.2 * self.prefer) * m2 +
                  (0.2 + 0.2 * self.land) * m3 + (0.2 + 0.2 * self.money) * m4) /\
                 (1 + 0.2 * self.rain + 0.2 * self.prefer + 0.2 * self.land + 0.2 * self.money)

            a2 = ((0.4 + 0.2 * self.land) * n1 + (0.4 + 0.2 * self.land) * n2 +
                  (0.2 + 0.2 * self.money) * n3) /\
                (1 + 2 * 0.2 * self.land + 0.2 * self.money)

            a3 = ((0.35 + 0.2 * self.land) * p1 + (0.3 + 0.2 * self.prefer) * p2 +
                  (0.35 + 0.2 * self.money + 0.2 * self.land) * p3) / \
                 (1 + 2 * 0.2 * self.land + 0.2 * self.prefer + 0.2 * self.money)

            t1 = ((0.4 + 0.2 * self.prefer) * o1 + (0.4 + 0.2 * self.prefer) * o2 +
                  (0.2 + 0.2 * self.money) * o3) /\
                 (1 + 2 * 0.2 * self.prefer + 0.2 * self.money)
            t2 = ((0.4 + 0.2 * self.prefer) * u1 + (0.4 + 0.2 * self.prefer) * u2 +
                  (0.2 + 0.2 * self.money) * u3) /\
                 (1 + 2 * 0.2 * self.prefer + 0.2 * self.money)

            temp = a1 + a2 + a3 + t1 + t2
            value.append(temp)
        # 返回种群中每个个体的基因型权值和，即适应度
        return value
