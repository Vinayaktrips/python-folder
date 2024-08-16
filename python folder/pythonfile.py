#write a forloop foor checking if a number is divisible by 7 or9 and display the table of that number

a=int(input("type the number that you want to know the table of , as well as to check whether it is divisible by either 7 or 9 ? "))

for c in range(1,11) :
   
    print(a ,"x", c ,"=", a*c)

if a%7==0 and a%9==0 :
    print(a," is divisible by both 7 and 9")
elif a%7==0 :
    print(a,"is only divisible by 7 ")
elif a%9==0 :
    print(a,"is only divisible by 9 ")
else :
    print(a,"is neither divisble by 7 nor 9")

