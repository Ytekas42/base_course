import numpy as np
from physics_constants import g

h = 100
a = 45
b = 35

v = np.sqrt((g * h * np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))

print(v)
