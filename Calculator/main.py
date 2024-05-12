# Simple Calculator

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(round(a/b,1))

while(True):
    operand1=int(input("Enter first number: "))
    operand2=int(input("Enter second number: "))

    print("<---Select an Operation to Perform--->")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")

    op=int(input("Enter the Operation 1 or 2 or 3 or 4 :"))
    if op in range(0,5):
        if op==1:
            print(f"The Sum of {operand1} and {operand2} is {add(operand1,operand2)}")
        elif op==2:
            print(f"The Differnce of {operand1} and {operand2} is {sub(operand1,operand2)}")
        elif op==3:
            print(f"The Product of {operand1} and {operand2} is {mul(operand1,operand2)}")
        elif op==4:
            print(f"The Result of {operand1} / {operand2} is {div(operand1,operand2)}")
    else:
        print("Invalid Operation! Try Again")
    choice=input("Do you Wish to Countinue? : yes/no ").lower()      
    if choice!="yes":
        break
       