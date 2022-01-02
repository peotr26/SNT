import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((1000, 800, 3), dtype=np.uint8)

x=997
y=2

for k in range(150):
    img[x,y] = (23,147,209)
    y=y+1
    img[x,y] = (23,147,209)
    x=x-1
    y=y+1

x=997
y=797

for k in range(150):
    img[x,y] = (23,147,209)
    y=y-1
    img[x,y] = (23,147,209)
    x=x-1
    y=y-1

x=997
y=2

for k in range(398):
    img[x,y] = (23,147,209)
    x=x-1
    img[x,y] = (23,147,209)
    x=x-1
    y=y+1

x=997
y=797

for k in range(398):
    img[x,y] = (23,147,209)
    x=x-1
    img[x,y] = (23,147,209)
    x=x-1
    y=y-1

theta = np.linspace( 0 , 2 * np.pi , 150 )
 
radius = 100
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b )
axes.set_aspect( 1 )
 
plt.title( 'Parametric Equation Circle' )
plt.imshow(img)
plt.show()

