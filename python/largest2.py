def largest(a,b,c):
    if(a>b and a>c):
        print("Number 1 is the largest")
    elif(b>a and b>c):
        print("Number 2 is the greatest")
    else:
        print("Number 3 is the greatest")



num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
result=largest(num1,num2,num3)
print(result)