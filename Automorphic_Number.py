n=int(input())
s=n*n
if str(s).endswith(str(n)):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')