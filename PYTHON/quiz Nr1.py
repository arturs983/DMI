import random
import numpy as np

def ranges(b_r,b,x):
    for i in range(len(x)):
        for j in range(len(b_r)-1):
            if x[i] > b_r[j] and x[i] < b_r[j+1]:
                b[j] = b[j] + 1
    return b

N = 100
x = []
a = 0
b = np.pi
delta = 0.5
for i in range(N):
    x.append(random.uniform(a,b))

bars_ranges = np.arange(a,b,delta)
bars = np.zeros(len(bars_ranges))

bars = ranges(bars_ranges,bars,x)
print bars
