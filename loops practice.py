number=0
while number<7:
    print(number)
    number=number+1
print("bye bye")

a=["Ali","Arif",55,5.5]
while a:
    print(a.pop(0))    

n=int(input("Enter number:"))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i=i+1
print("The sum is",sum)

list1=['learning','is','fun']
ctr=0
while(ctr<len(list1)):
    print(list1[ctr])
    ctr+=1
    
print(list1)
number=int(input('enter a number:'))
total=0
while number!=0:
    total+=number
    number= int(input('Enter a number:'))
    
print('The sum is',total)

a=[1,2,3,4,5]
while(a):
    print("outer:",a.pop())
    b=['Arif','Rauf']
    while(b):
        print('\t Inner:',b.pop())
print("After both the loops end")
print("a=",a)
print("b=",b)

n=0
while(True):
    n=n+1
    if(n==5):
        break
    print(n)
print("outside loop")

n=10
while(n>0):
    n=n-1
    if(n==5):
        break
    print(n)
    