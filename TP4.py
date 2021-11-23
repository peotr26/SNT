from turtle import*

ht()
bgcolor('black')
speed(0)
color('black')

down()
color('red')
for k in range(3):
    for k in range(12):
        circle(100)
        up()
        forward(100)
        left(360/12)
        down()
    up()
    forward(1)
    down()

mainloop()