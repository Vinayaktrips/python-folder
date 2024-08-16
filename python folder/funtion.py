#defining a function
"""def addition():
    a=int(input("no.1="))
    b=int(input("no.2="))
    sum=a+b
    print(sum)

addition()
"""
#create a function for finding the volume of a cube,rectangular prism,cylinder

print("what shapes volume do you want to know about ?")
a=input("1=cube 2=rectangular prism 3=cylinder ")

def volumeOfCube():
    b=int(input("side="))
    vol=b**3
    print(vol)

def volumeOfRectangularPrism():
    c=int(input("length="))   
    d=int(input("breadth="))
    e=int(input("height="))
    vol=c*d*e
    print(vol)

def volumeOfCylinder():
    f=int(input("height="))
    g=int(input("radius="))
    vol=3.14*(f*(g**2))
    print(vol)

if a=="1" :
    volumeOfCube()

if a=="2" :
    volumeOfRectangularPrism()

if a=="3" :
    volumeOfCylinder()
















