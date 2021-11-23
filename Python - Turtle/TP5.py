from turtle import*

speed(0)
ht()

up()
goto(0,-300)
down()
circle(300,360)

up()
goto(0,0)
down()
color('red','pink')
begin_fill()
circle(30,360)
end_fill()

up()
goto(-450,100)

for k in range(2):
    up()
    forward(300)
    down()
    color('blue')
    begin_fill()
    circle(35,360)
    end_fill()

up()
width(15)
color('black')
goto(0,-200)
down()
circle(150,90)
up()
circle(150,-90)
down()
circle(150,-90)

mainloop()