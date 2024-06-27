from turtle import *


#we want to paint a house

# step 1:  draw a square
speed(30)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(70, 110)
pendown()
color("yellow")
right(145)
forward(10)
color("green")

penup()
goto(70, 120)
pendown()

left(85)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

penup()
goto(45, 120)
pendown()

left(180)
forward(50)

penup()
goto(45, 145)
pendown()


left(90)
forward(25)

penup()
goto(45, 145)
pendown()

right(180)
forward(25)

penup()
goto(130, 120)
pendown()

forward(50)
left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
left(90)

penup()
goto(155, 120)
pendown()

left(90)
forward(50)

penup()
goto(155, 145)
pendown()

left(90)
forward(25)

right(180)
forward(50)



exitonclick()