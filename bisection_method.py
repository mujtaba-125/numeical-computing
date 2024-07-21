def bisect(a,b):
    p=(a+b)/2
    fa,fp,fb=f(a),f(p),f(b)

    print(a,'\t',p,'\t','\t',b)
    print(fa,'\t',fb,'\t',fp,'\t')

    return p
def f(x):
    return x**2-36

a=1
b=10
fa=f(a)
fb=f(b)
fa,fb

a,b=a,b
p=bisect(a,b)
print(p)