def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        print("divided by zero not processed")
    else:
        return n1/n2

print("Select the operation ")
print("1. ADD ")
print("2. subtraction ")
print("3. Multiply ")
print("4. Divide ")
choice = input("Enter your choice :")
x=float(input("Enter the first number :"))
y=float(input("Enter the second number :"))
if choice == '1':
    print("Addition :",add(x,y))
elif choice == '2':
    print("Subtraction : ",sub(x,y))
elif choice == '3':
    print("multiplication : ",mul(x,y))
elif choice == '4':
    print("Division : " ,div(x,y))
else:
    print("Invalid choice ")
