n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    t=(a/b)+(a/c)
    if t>=d:
        print("Win")
    else:
        print("Lose")