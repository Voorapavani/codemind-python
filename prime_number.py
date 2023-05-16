import math
n=int(input())
s=int(math.sqrt(n))
for i in range(2,s+1): 
    if n%i==0:
        print('not a prime')
        break
else:
    print('prime')