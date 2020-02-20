from mul import multiplication
from div import divition
from sub import subtraction
from add import addition

print("Omar helped a girl")

while(True):

    num1=input("Enter the first number:")
    num2=input("Enter the second number:")

    num1=float(num1)
    num2=float(num2)

    op=input("Enter your operation:")

    mulobj=multiplication(num1,num2)
    subobj=subtraction(num1,num2)
    addobj=addition(num1,num2)
    divobj=divition(num1,num2)

    if (op == '*'):
        result=mulobj.mulfunction()
        print("your result is :",result)
    elif (op == '-'):
        result=subobj.subfunction()
        print("Subtraction is:", result)
    elif(op == '+'):
        result=addobj.addfunction()
        print("Addition is:", result)
    elif(op == '/'):
        result=divobj.divfunction()

    per=input("Do you want to run again?\nEnter Yes or No.")
    per=per.lower()
    if (per == "yes"):
        continue
    elif(per == 'no'):
        break

