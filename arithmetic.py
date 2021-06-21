num1 = int(input("enter the starting num="))
num2 = int(input("enter the ending num="))

print("Prime numbers between", num1, "and", num2, "are:")
for num in range(num1, num1 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)