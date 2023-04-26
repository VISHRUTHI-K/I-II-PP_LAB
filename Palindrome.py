n=int(input("Enter a number"))
temp=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
    
    
    
    
    OUTPUT:
    Enter a number767
    767 is a palindrome
