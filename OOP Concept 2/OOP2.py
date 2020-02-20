print("20-05-2019")

from oop2operation import operation as op
while (True):

    num1 = input("Enter The First Number:")
    num2 = input("Enter The Second Number:")

    num1 = float(num1)
    num2 = float(num2)

    obj=op(num1,num2)

    re=obj.alloperation()
    for i in range(0,len(re)):
        if (i == 0):
            print("Addition is :",re[i])
        elif(i == 1):
            print("Subtraction is :",re[i])
        elif(i == 2):
            print("Multiplication is :", re[i])


    per = input("Do you want to run again?\nEnter Yes or No.")
    per = per.lower()
    if (per == "yes"):
        continue
    elif (per == 'no'):
        break

