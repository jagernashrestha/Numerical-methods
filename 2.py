# N-R method of finding the root.
E = 0.001
x0 = 3  # initial value
i = 0

def fx_value(x):
    fx = (x**2) - (4*x)- 10
    return round(fx,4)
def dfx_value(x):           # 1st derivative 
    fx = (2*x) - 4
    return round(fx,4)

print('Using N-R method to find the root.')
while True:
    i+=1
    fx0 = fx_value(x0)
    dfx0 = dfx_value(x0)
    print(f'{i}th iteration fx0 is: {fx0} at x0 = {round(x0,3)}')
    if abs(fx0) < E:
        print(f"\nThe Expected root is :{round(x0,3)}")
        break
    else :
        x1 = x0 - (fx0/dfx0)
        x0 = x1