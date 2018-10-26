from turtle import *
space = Screen()
ryan = Turtle()
ryan.speed(10)
def black_line(turtle,size,direction,length,x,y):
	turtle.color('black')
	turtle.pensize(size)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.right(direction)
	turtle.forward(length)
def filled_rectangle(turtle,color,size,length1,length2,x,y):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length1)
        turtle.right(90)
        turtle.forward(length2)
        turtle.right(90)
    turtle.end_fill()
def octagon(turtle,color,size,length,x,y):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(8):
        turtle.forward(length)
        turtle.right(90)
def repeat_octagon(turtle,color,size,length,x,y):
	for i in range(5):
		octagon(turtle,color,size,length*i,x,y)
def triangle(turtle,color,size,length,x,y):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)
def repeat_triangle(turtle,color,size,length,x,y):
	for i in range(4):
		triangle(turtle,color,size,length,x,y)
		turtle.left(90)
	for i in range(8):
		triangle(turtle,color,size,length*2,x,y)
		turtle.left(45)
def turtle_loop(turtle,size,distance,x,y):
	color_list = ['blue','red','yellow','orange','green','pink','lime','turquoise','azure','black','purple']
	turtle.shape('turtle')
	turtle.pensize(size)
	turtle.penup()
	turtle.goto(x,y)
	distance = 30
	for i in range(11):
		turtle.color(color_list[i])
		turtle.stamp()
		distance = distance+5
		turtle.forward(distance)
		turtle.right(40)
def draw_mondrian(turtle):
	filled_rectangle(turtle,'red',6,215,405,150,40)
	filled_rectangle(turtle,'purple',6,300,405,-400,40)
	filled_rectangle(turtle,'yellow',6,300,320,-400,400)
	filled_rectangle(turtle,'green',6,215,50,150,175)
	black_line(turtle,10,0,800,-400,40)
	black_line(turtle,10,0,800,-400,80)
	black_line(turtle,10,0,230,-80,300)
	black_line(turtle,10,0,230,-80,200)
	black_line(turtle,10,0,230,-80,350)
	black_line(turtle,10,0,230,-80,250)
	black_line(turtle,10,0,230,-80,150)
	black_line(turtle,10,0,250,150,125)
	black_line(turtle,10,0,250,150,175)
	black_line(turtle,10,90,800,150,400)
	black_line(turtle,10,0,800,-80,400)
	black_line(ryan,10,0,800,-100,400)
def draw_shapes(turtle):
	repeat_octagon(turtle,'blue',6,10,-300,300)
	repeat_triangle(turtle,'orange',6,20,300,300)
def draw_turtles(turtle):
	turtle_loop(ryan,15,10,-200,-200)
def drawArt():
	draw_mondrian(ryan)
	draw_shapes(ryan)
	draw_turtles(ryan)
drawArt()
exitonclick()