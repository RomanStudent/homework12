import copy
import numpy as np

np.random.seed(123)
income = np.random.randint(70000, 100000, (3, 10))
print(income)

net_income = income * 0.7
print(net_income)

net_income_recalculated = copy.deepcopy(net_income)
net_income_recalculated[:, 4:7] = income[:, 4:7] * 0.6
print(net_income_recalculated)

print(net_income_recalculated[:, 3:6])

print(net_income - net_income_recalculated)
