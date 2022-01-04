import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((20, 30, 3), dtype=np.uint8)

#sol
for k in range(0,30):
    img[19, k] = (139,69,19)

#maison
for j in range(10,20):
    for k in range(3,13):
        img[j, k] = (255, 255, 255)

#porte
for j in range(13,20):
    for k in range(4,8):
        img[j,k] = (105,105,105)

#fenêtre
c=255
for j in range(13,16):
    for k in range(9,12):
        img[j,k] = (0,0,c)
    c=c-50

#toit
u=1
c=100
for j in range(5,10):
    for k in range(8-u,8):
        img[j, k] = (c,0,0)
    u=u+1
    c=c+20

u=1
c=100
for j in range(5,10):
    for k in range(8,8+u):
        img[j, k] = (c,0,0)
    u=u+1
    c=c+20

#tronc
for j in range(5,19):
    for k in range(22,24):
        img[j,k] = (109,29,0)

#feuillage
u=1
for j in range(1,5):
    for k in range(23-u,23):
        img[j, k] = (155, 0, 0)
    u=u+1

u=1
for j in range(1,5):
    for k in range(23,23+u):
        img[j, k] = (155, 0, 0)
    u=u+1

u=1
for j in range(2,9):
    for k in range(23,23-u):
        img[j, k] = (155, 0, 0)
    u=u-1

u=1
for j in range(2,9):
    for k in range(23+u,23):
        img[j, k] = (155, 0, 0)
    u=u-1

u=1
for j in range(5,13):
    for k in range(23,23-u):
        img[j, k] = (155, 0, 0)
    u=u-1

u=1
for j in range(5,13):
    for k in range(23+u,23):
        img[j, k] = (155, 0, 0)
    u=u-1

plt.imshow(img)
plt.show()

