def reverse(r):
    rev=0
    a=0
    while(r>0):
        a=r%10
        rev=rev*10+a
        r=r//10


n=int(input("Enter the value of n: "))
result=reverse(n)

print(result)