from turtle import*

speed(0)
ht()

up()
backward(150)
down()
forward(350)
up()
goto(0,0)
down()

for k in range(2):
    forward(117)
    left(90)
    forward(125)
    left(90)

up()
forward(30)
down()
for k in range(2):
    color('brown')
    begin_fill()
    forward(30)
    left(90)
    forward(60)
    left(90)
    end_fill()

up()
goto(0,125)
down()

color('red')
begin_fill()
for k in range(3):
    forward(117)
    left(360/3)
end_fill()

up()
goto(-40,200)
down()

color('yellow')
begin_fill()
circle(30)
end_fill()

mainloop()