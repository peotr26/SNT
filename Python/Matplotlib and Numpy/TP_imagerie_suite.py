import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((20, 20, 3), dtype=np.uint8)

u = 0
for j in range(0,10):
    for k in range(0,20):
        img[j, k] = (0, u, 255-u)
    u = u + 24
for j in range(10,20):
    for k in range(0,20):
        img[j, k] = (255-u, u, 0)
    u = u -24

plt.imshow(img)
plt.show()