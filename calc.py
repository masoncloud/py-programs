def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b

print("What operation do you want to Perform - \n" 

"1. add\n" \
"2. sub\n" \
"3. multiply\n" \
"4. Divide\n")

select = input("Select operations from 1, 2, 3, 4 :") 
num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :")) 

if  (select == '1'):
    print(add(num1,num2))
elif (select == '2'):
    print(sub(num1,num2))
elif (select == '3'):
    print(mul(num1,num2))
elif (select == '4'):
    print(divide(num1,num2))
else: 
    print("Invalid operation")