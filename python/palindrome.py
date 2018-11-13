num=int(input("Enter a number: "))
temp=num
i=0
rev=0
while(num>0):
    a=num%10
    rev=rev*10+a
    num=num//10
if(num==temp):
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
