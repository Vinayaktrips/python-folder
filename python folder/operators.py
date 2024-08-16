#arithemetic operator
'''print(5-3)
a=int(input("enter a number? "))
b=int(input("enter another one? "))
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
if a==2:
    print(True)
'''
'''#assign operator
x=-5


x+=2 #x=x+2
print(x)
x-=3
print(x)
x*=7
print(x)
x/=4
print(x)
x//=4
print(x)
x%=3
print(x)

#Comparison operators
if 6>3:
    print(True)
else :
    print(False)
if 5<10:
    print(True)
else :
    print(False)

e=int(input("enter a number ? "))
f=e%2
if f==0:
    print(e," is an even number ")
else :
    print(e," is an odd number ")'''

'''f=int(input("enter a number "))
g=f%2
h=f%3
i=f%5
j=f%7
if g !=0 and h !=0 and i !=0 and j !=0 :
    print(f," is a prime number")
elif f==2 or f==3 or f==5 or f==7 :
    print(f," is a prime number")
else :
    print(f," is a composite number ")'''

#logical operator 'and&& or not'

#write a programme to check the type of triangle
'''a=int(input("give angle 1 "))
b=int(input("give angle 2 "))
c=abs(180-(a+b))
if a+b+c<=180 :
    if a==b and c!=60 :
        print("its an isoceles triangle")
    elif a==b==60 :
        print(" its an equilateral triangle")
    else :
        print(" its a scalene triangle")

else :
    print("triangle is not possible ")

x=[15,30,45,60,75]
if 90 not in x :
    print(True)
else :
    print(False)'''
#write a programme to ask the user for a square or a cube 
"""print("FIND A SQUARE OR CUBE")
a=int(input("enter a number : "))
operation=input("Square or Cube ").lower()
if operation=="square" :
    print(a**2) 
else :
    print(a**3)"""

#find the area/perimeter of a suare/circle/rectangle
a=input("choose your shape from square,circle or a rectangle ").lower()

if a=="square" :
    b=int(input("side= "))
    f=input("do you want to know area or perimeter ")
    if f=="area" and a=="square" :
        print(b**2)
    elif f=="perimeter" and a=="square" :
        print(b*4)
elif a=="rectangle" :
    c=int(input("length= "))
    d=int(input("breadth= "))
    f=input("do you want to know area or perimeter ")
    if f=="area" and a=="rectangle" :
        print(c*d)
    elif f=="perimeter" and a=="rectangle" :
        print(2*(c+d))


elif a=="circle" :
    e=int(input("radius= "))
    f=input("do you want to know area or perimeter ")
    if f=="area" and a=="circle" :
        print(3.14*e**2)
    elif f=="perimeter" and a=="circle" :
        print(e*6.28,"cm")




