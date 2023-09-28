x1 , y1 = eval( input("Enter three points for a triangle: ") )
x2 , y2 = eval( input() )
x3 , y3 = eval( input() )
s = ( ( (y2-y1)**2 / (x2-x1)**2 )**.5 +
      ( (y3-y2)**2 / (x3-x2)**2 )**.5 +
      ( (y1-y3)**2 / (x1-x3)**2 )**.5 ) / 2
area =( s * (s -((y2-y1)**2 / (x2-x1)**2)) *
            (s -((y3-y2)**2 / (x3-x2)**2)) *
            (s -((y1-y3)**2 / (x1-x3)**2)) )**.5
print( "The area of the triangle is " , area )
