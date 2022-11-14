#this calculator is faulty
#you will get wrong answers on this calculations:
# 45*3=555 || 56+9=77 || 56/6=4
#on other calculation you will get the right answers😍

operator = input("enter a operator")
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
while(True):
    if operator=='*' and num1==45 and num2==3:
        print("your answer is:555")
        break
    elif operator=='+' and num1==56 and num2==9:
        print("your answer is:77")
        break
    elif operator=='/' and num1==56 and num2==6:
        print("your answer is:4")
        break
    elif(operator=='+'):
            print(num1+num2)
            break
    elif(operator=='-'):
            print(num1-num2)
            break
    elif(operator=='*'):
            print(num1*num2)
            break
    elif(operator=='/'):
            print(num1/num2)
            break
    elif(operator=='**'):
            print(num1**num2)
            break
print("Thank you for using our service.")
