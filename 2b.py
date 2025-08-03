# Secant method of finding the root.
E = 0.001
x1 = 4
x2 = 2
i = 0

def fx_value(x):
    fx3 = (x**2) - (4*x)- 10
    return round(fx3,4)

def x3_value(x1,x2):
    x3 = (x1*fx_value(x2)-x2*fx_value(x1))/(fx_value(x2)-fx_value(x1))
    return round(x3,4)

print('Using Secant method to find the root.')

while True:
    i+=1
    x3 = x3_value(x1,x2)
    fx3 = fx_value(x3)
    print(f'{i}th iteration fx0 is: {fx3} at x0 = {x3}')
    if abs(fx3) < E:
        print(f"\nThe Expected root is :{x3}")
        break
    else:
        x1 = x2 
        x2 = x3  