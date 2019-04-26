import matplotlib.pyplot as plt
import numpy as np
import random
from fitness import Fit
from selection import Select
from crossover import Cross
from mutation import Mutate

buildings = []
temp = []
for i in range(8):
    for j in range(5):
        if j == 0:
            temp.append(random.randint(1, 5))
        else:
            temp.append(random.randint(1, 3))
    buildings.append(temp)
    temp = []

t = []
record = []
for i in range(500):
    value = Fit(buildings).fitness()
    temp_max = max(value)
    t.append(temp_max)
    index = value.index(temp_max)
    record.append(buildings[index])
    buildings_new = Select(buildings, value).selection()
    children = Cross(buildings_new, 0.8).crossover()
    buildings = Mutate(children, 0.02).mutation()

value_max = Fit(record).fitness()
temp_max = max(value_max)
index = value_max.index(temp_max)
print(value_max[index])

plt.plot(t)
plt.axhline(max(t), linewidth=1, color='r')
plt.show()
