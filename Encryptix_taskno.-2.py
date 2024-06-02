
#Taking input from the user
num1=eval(input("enter the first number"))
num2=eval(input("enter the second number"))
# choices
print("-------Hey! Welcome to your calculator-------")
print("Please select from  the following choices about the operation you  want to perform")
print("1. Addition")
print("1. Subtraction")
print("1. Multiplication")
print("1. Division")
choice=int(input("enter the choice between 1-4"))
#conditions  
if choice==1:
    print("The sum of two numbers is",(num1+num2))
elif choice==2:
    print("The difference of two numbers is",(num1,num2))
elif choice==3:
    print("The product of two numbers is",(num1*num2))
elif choice==4:
    print("The quotient of two numbers is",(num1/num2))
else:
    print("Sorry ! No task can be performed")
print("Good Bye wave :)")
