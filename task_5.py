import numpy as np

N, M = 4, 5
i, j = np.ogrid[:N, :M]
trig_array = np.sin(i + j + 1)
a, b = 1, 3
trig_array[:, [a, b]] = trig_array[:, [a, b]]
print(f"После обмена столбцов {a} и {b}:")
print(trig_array)