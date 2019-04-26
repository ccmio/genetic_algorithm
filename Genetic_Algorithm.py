# 主程序
# 因遗传算法特性，每次运行的进化图像不一致，收敛结果一致
# 可调整参数：初始种群个体数，基因交叉概率，基因变异概率，进化次数
# 需要自行安装的库：matplotlib, random
import matplotlib.pyplot as plt
import random
from translation import translate
from fitness import Fit
from selection import Select
from crossover import Cross
from mutation import Mutate

# 初始化随机种群
buildings = []
temp = []
# 20为种群内个体数，可自行调整，越大收敛效果越好，建议不小于10
for i in range(20):
    for j in range(5):
        if j == 0:
            # 随机分配一号位基因，编码方式为A11：1，A12：2，具体可见translation.py文件内的字典
            temp.append(random.randint(1, 5))
        else:
            # 随机分配二三四五号位基因
            temp.append(random.randint(1, 3))
    buildings.append(temp)
    temp = []

# 获取既定条件
rain = input('请输入降雨量【0/1】：0为低，1为高： ')
land = input('请输入地形【0/1】：0为平原，1为山地： ')
money = input('请输入成本【0/1】：0为资金充沛，1为资金紧张： ')
location = input('请输入地理区位【0/1】：0为用地分散，1用地集中： ')
prefer = input('请输入设计的传统性【0/1】：0为现代性强，1为传统性强： ')


t = []
record = []
# 进化次数250次，建议不少于200次
for i in range(250):
    # 计算每个个体的适应度函数的值
    value = Fit(buildings, rain, land, money, location, prefer).fitness()
    temp_max = max(value)
    # t用于存储最优个体的适应度，用以绘制最后的进化图像
    t.append(temp_max)
    index = value.index(temp_max)
    # record用于存储每次进化最优的个体，方便最后打印最优基因型
    record.append(buildings[index])
    # Select函数决定本代哪些个体可以活到下一代
    buildings_new = Select(buildings, value).selection()
    # 活下来的个体以0.7的概率进行交配产生子代（交叉概率0.7）
    children = Cross(buildings_new, 0.7).crossover()
    # 子代以0.02的概率基因突变
    buildings = Mutate(children, 0.02).mutation()

# 提取最优解的基因型
value_max = Fit(record, rain, land, money, location, prefer).fitness()
temp_max = max(value_max)
index = value_max.index(temp_max)
# 把最优解的基因型从数字编码翻译成题设给的字母，打印输出
result = translate(record[index])
print('最优解的基因型为:', result)

# 输出收敛过程及最大值的函数图像
plt.plot(t)
plt.axhline(max(t), linewidth=1, color='r')
plt.show()
