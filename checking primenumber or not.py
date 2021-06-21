num=int(input("enter a number="))
for i in range(2,num):
    if num%i==0:
        print("this is not a prime")
        break
else:
    print("this is a prime")