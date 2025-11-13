import numpy as np

N, M = 4, 5
i, j = np.ogrid[:N, :M]
trig_array = np.sin(i + j + 1)
trig_array[trig_array < 0] = 0
print("Массив после замены отрицательных на 0:")
print(trig_array)


