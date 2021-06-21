a=int(input("side of a="))
b=int(input("side of b="))
c=int(input("side of c="))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f' %area)