n=int(input())
s=0
a=n*n
while a>0:
    s=s+a%10
    a=a//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")