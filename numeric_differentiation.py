h=2
x=8
x0=1
y0=24

dy0=96
d2y0=120
d3y0=48

p=(x-x0)/h
print(f'value of x is {x}\nvalue of h is {h}\nvalue of p is {p}')

def fact(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value

def interpolation_polynomial(x,x0,h,dy0,d2y0,d3y0):
    p=(x-x0)/h
    return                      y0+\
          p                    *dy0+\
          p*(p-1)/fact(2)      *d2y0+\
          p*(p-1)*(p-2)/fact(3) *d3y0
x=8
print_stat=interpolation_polynomial(x,x0,h,dy0,d2y0,d3y0)
print(print_stat)

x_m=7.5
y_m=interpolation_polynomial(x_m,x0,h,dy0,d2y0,d3y0)
print(y_m)

x_p=8.5
y_p=interpolation_polynomial(x_p,x0,h,dy0,d2y0,d3y0)
print(y_p)

print((y_p-y_m)/(x_p-x_m))

"""we can also calculate the numeric calculation in the more simplest way"""

def numberic_diff(x,x0,h,dy0,d2y0,d3y0):
    p=(x-x0)/h
    print(f'p={p}')
    return(                              dy0  +\
            ((2*p)-1)     /fact(2)      *d2y0 +\
            (3* p**2 - 6*p + 2) /fact(3)*d3y0  \
    )/h

numberic_diff(8,x0,h,dy0,d2y0,d3y0)
h=1
x0=1
y0=1

dy0=7
d2y0=12
d3y0=6

y1=numberic_diff(1,x0,h,dy0,d2y0,d3y0)
print(y1)