import numpy as np
import matplotlib.pyplot as plt
import random

img = np.zeros((50, 50, 3), dtype=np.uint8)

x = 0
y = 25

for k in range(50):
    img[x,y] = (255,255,255)
    x = x+1

x = random.randrange(0, 35)
y = 0

for k in range(2):
    for k in range(15):
        img[x,y] = (255,255,255)
        x = x+1
    x = x-15
    y = y+1

x = random.randrange(0, 35)
y = 49

for k in range(2):
    for k in range(15):
        img[x,y] = (255,255,255)
        x = x+1
    x = x-15
    y = y-1

x = random.randrange(3, 47)
y = random.randrange(3, 47)

for k in range(2):
    img[x,y] = (255,255,255)
    x = x+1
    img[x,y] = (255,255,255)
    y = y+1
    x = x-1

plt.imshow(img)
plt.show()