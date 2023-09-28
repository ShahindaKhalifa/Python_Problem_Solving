import turtle
redius = eval( input("Enter the radius: ") )
turtle.showturtle()
turtle.penup()
turtle.goto( 2*redius ,(redius / 2))
turtle.pendown()
turtle.circle(2 * redius)

turtle.penup()
turtle.goto( -2*redius ,(redius / 2))
turtle.pendown()
turtle.circle(2 * redius)

turtle.penup()
turtle.goto( -2*redius ,-7*(redius / 2))
turtle.pendown()
turtle.circle(2 * redius)

turtle.penup()
turtle.goto( 2*redius ,-7*(redius / 2))
turtle.pendown()
turtle.circle(2 * redius)

