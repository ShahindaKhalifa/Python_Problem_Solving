import turtle
x,y = eval( input("enter the center and radius of a circle: ") )
radius = eval( input() )
area = radius **2 *3.14
turtle.showturtle()
turtle.penup()
turtle.goto( x,y  )
turtle.write(area)
turtle.right(90)
turtle.forward(radius)
turtle.right(-90)
turtle.pendown()
turtle.circle(radius)
