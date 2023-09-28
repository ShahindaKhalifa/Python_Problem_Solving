x = eval( input("Enter an integer: ") )
fourth_digit = x % 10
x_without_fourth = x // 10
#print(x_without_fourth)
third_digit = x_without_fourth % 10
x_without_third = x_without_fourth // 10
#print(x_without_third)
secound_digit = x_without_third % 10
first_digit = x_without_third // 10
print(first_digit)
print(secound_digit)
print(third_digit)
print(fourth_digit)
