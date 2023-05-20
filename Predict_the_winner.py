n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in l:
    if i%2==0:
        s=s+i
for j in l:
    if j%2!=0:
        s1=s1+j
if((abs(s-s1))%4==0):
    print("X")
else:
    print("Y")