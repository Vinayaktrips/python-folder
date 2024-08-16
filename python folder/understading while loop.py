#understanding while and for loop
'''i=20
while i<=30 :
    print(i)
    if i%7==0 and i%4==0 :
        break
    
    i+=1

#continue
f=0
while f<10 :
    
    f+=1
    if f%3==0 :
        continue
    print(f)'''


#hw,can you write a programme to enter a number and display its table   

"""a=int(input("what number's table do you want to know ? ")) 
b=1
while b<=10 :
    print(a," x ",b ,"=",a*b)
    b+=1"""
 
#write a programe to display the body mass index and the health of the person 
'''a=float(input("what is your height in m ? "))
b=float(input("what is your weight in kilograms ? "))
if 1<=a<=2.5 and 0<=b<=150 :
    bmi=b/(a**a)
    print(bmi)
    if bmi<=14 :
        print("you are underweight")
    elif 14<bmi<=26 :
        print("you are healthy")
    elif 26<bmi<=30 :
        print("you are overweight")
    elif bmi>30 :
        print("you are obeese")

#armstrong number
a=int(input("give me a number ? "))
n=len(str(a))
c=a
sum=0
while c>0 :
    b=c%10
    sum=sum+b**n
    c=c//10

if a==sum :
    print("armstrong number")
else :
    print("normal number")

'''
#find factorial of any number 
#start a fibonacchi series
'''
a=int(input("give me a number of which you want the factorial ? "))
b=1
while a>=1 :
    b*=a
    a-=1'''
   