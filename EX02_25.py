import turtle
x,y = eval( input(" Enter the center of a rectangle, width, and height: ") )
width = eval(input())
height = eval(input())
turtle.speed(1)
turtle.showturtle()
turtle.penup()
turtle.goto(( x + (width / 2) ) , ( y + (height / 2) ))
turtle.pendown()
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
