import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((20, 20, 3), dtype=np.uint8)

img[10,9.5]= (0,0,255)
img[0,0] = (255,0,0)
img[0,19] = (255,0,0)
img[19,0] = (255,0,0)
img[19,19] = (255,0,0)

plt.imshow(img)
plt.show()