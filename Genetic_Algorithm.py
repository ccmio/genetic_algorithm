# 主程序
# 因遗传算法特性，每次运行的进化图像不一致，收敛结果一致
# 可调整参数：初始种群个体数，基因交叉概率，基因变异概率，进化次数
# 需要自行安装的库：matplotlib, random
import matplotlib.pyplot as plt
import random
from fitness import Fit
from selection import Select
from crossover import Cross
from mutation import Mutate

# 初始化随机种群
buildings = []
temp = []
# 种群内个体数量16，可自行调整，越大收敛效果越好，建议10~18之间的偶数
for i in range(16):
    for j in range(5):
        if j == 0:
            # 分配一号位基因
            temp.append(random.randint(1, 5))
        else:
            # 分配二三四五号位基因
            temp.append(random.randint(1, 3))
    buildings.append(temp)
    temp = []

conditon = input('请选择既定条件：', '\n', '1、气候条件', '\n', '2、地形地貌', '3、建造成本', '4、地理区位', '5、传统设计')
if conditon == 1:
    rain = input('请输入降雨量：0为低，1为高：')
elif conditon == 2:
    land = input('请输入地形：0为平原')
elif conditon == 2:
# 进化次数250次，建议不超过500次
t = []
record = []
for i in range(250):
    value = Fit(buildings).fitness()
    temp_max = max(value)
    t.append(temp_max)
    index = value.index(temp_max)
    record.append(buildings[index])
    buildings_new = Select(buildings, value).selection()
    # 交叉概率0.7，变异概率0.02
    children = Cross(buildings_new, 0.7).crossover()
    buildings = Mutate(children, 0.02).mutation()

# 提取最优解的基因型，打印输出
value_max = Fit(record).fitness()
temp_max = max(value_max)
index = value_max.index(temp_max)
print(record[index])

# 输出收敛过程及最大值的函数图像
plt.plot(t)
plt.axhline(max(t), linewidth=1, color='r')
plt.show()
