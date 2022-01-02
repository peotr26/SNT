import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.patches import Ellipse

pts = np.array([[2,2], [400,998], [798,2]])
p = Polygon(pts, closed=False, color='royalblue')
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,800)
ax.set_ylim(1,1000)

ellipse = Ellipse(xy=(400,-150), width=1000, height=650, 
                        edgecolor='white', fc='white', lw=2)
ax.add_patch(ellipse)

ellipse = Ellipse(xy=(400,250), width=150, height=350, 
                        edgecolor='white', fc='white', lw=2)
ax.add_patch(ellipse)

plt.axis('scaled')
plt.show()