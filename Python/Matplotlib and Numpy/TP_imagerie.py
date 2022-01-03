import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((20, 20, 3), dtype=np.uint8)

x = 0
y = 10

for k in range(20):
    img[x,y] = (0,0,255)
    x = x+1

x = 3
y = 0

plt.imshow(img)
plt.show()