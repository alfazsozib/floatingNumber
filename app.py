import re

t = int(input())
for i in range(t):
    b = input()
    pattern = re.compile(r'[+-]?[0-9]*\.[0-9]+$')
    a=pattern.match(b)
    if a == None:
        print(False)
    else:
        print(True)    
