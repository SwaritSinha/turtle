import turtle
house = turtle.Turtle()

turtle.bgcolor("blue")

#wall
house.begin_fill()
house.color("black")


for i in range(4):
    house.forward(100)
    house.left(90)

house.left(90)
house.forward(100)

    #roof
house.right(30)
house.forward(100)
house.right(120)
house.forward(100)
house.begin_fill()
house.color("black")
 
turtle.done()