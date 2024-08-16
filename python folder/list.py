#list1=["violet","indigo","blue","green","yellow",23,34,53]
"""
print(list1)
print(len(list1))
print(type(list1))
print(list1[1])
"""
 #print(list1[::])
"""
print(list1[0:])
#list are changeble,ordered and also they allow dupplication of the value which is not possible in tupple 
print(list1[::-1])
print(list1[2:8])
"""
"""
y=list((75,65,95))
print(y)

if "indigo" in list1 :
    print("yes indigo is available")

y.append(343)
y.insert(4,45)
y.extend(list1)
y.remove("yellow")
y.pop(5)
print(y)

print(y[1:7])
print(y[1:8:2])
#forloop has starting,end,increment 
for z in y :
    print(z)
print()
for i in range(0,len(y)) :
    print("index",i)
    print(y[i])

print(len(y))
a=0
while a<len(y) :
    print(y[a])
    a+=1

"""

a=eval(input("enter a list of no. "))
print(a)

b=list((24,42,52,45))
print(b)

#to use for loop take a variable then extract it and add it then loop it
























