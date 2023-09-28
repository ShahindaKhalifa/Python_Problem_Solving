subtotal = eval( input( "Enter the subtotal and a gratuity rate: " ) )
gratuityrate = eval( input() )
gratuity = (gratuityrate / 100) * subtotal
total = subtotal + gratuity
print("The gratuity is " ,gratuity ,"and the total is " , total)
