class Fit:
    def __init__(self, buildings):
        self.buildings = buildings

    def fitness(self):
        value = []
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

            a1 = 0.3 * m1 + 0.3 * m2 + 0.2 * m3 + 0.2 * m4
            a2 = 0.4 * n1 + 0.4 * n2 + 0.2 * n3
            a3 = 0.35 * p1 + 0.3 * p2 + 0.35 * p3
            t1 = 0.4 * o1 + 0.4 * o2 + 0.2 * o3
            t2 = 0.4 * u1 + 0.4 * u2 + 0.2 * u3

            temp = a1 + a2 + a3 + t1 + t2
            value.append(temp)

        return value
