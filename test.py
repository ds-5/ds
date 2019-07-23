
#22-A-1. Parenthesis Matching using Python
# Version-1. user define
def printMatchedPairs_self(s):
    stack = []
    result = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                result.append('(%d,%d)' % (stack.pop(), i))
            except IndexError:
                print('Stack was empty, no match exists')
    print(', '.join(result))
    while stack:
        print('No match for left parenthesis at', stack.pop())

# Version-2. import module
import queue
def printMatchedPairs_import(s):
    stack = queue.LifoQueue(len(s))
    result = []
    for i, c in enumerate(s):
        if c == '(':
            stack.put(i)
        elif c == ')':
            if stack.qsize():
                result.append('(%d,%d)' % (stack.get(), i))
            else:
                print('Stack was empty, no match exists')
    print(', '.join(result))
    while stack.qsize():
        print('No match for left parenthesis at', stack.get())

# TEST
'''
strings = ['(a*(b+c)+d)', '(a*(b+c+d)', '(a*b+c)+d)', '(a*(((b+c)+d)']
for s in strings:
    print('self:')
    printMatchedPairs_self(s)
    print('import:')
    printMatchedPairs_import(s)
    print()
'''

#22-A-2. Tower of Hanoi using Python
def printTower(x,y,z):
    height = sum(map(len, [x,y,z]))-1
    for i in range(height,-1,-1):
        for l in [x,y,z]:
            if len(l) > i:
                print('[%d]   '%l[i], end='')
            else:
                print('      ',end='')
        print()
    print('-----------------')

def towersOfHanoi(n, x, y, z):
    if n > 0:
        towersOfHanoi(n-1, x, z, y)
        y.append(x.pop())
        printTower(x0,y0,z0)
        towersOfHanoi(n-1, z, y, x)

x0 = list(range(4,0,-1))
y0 = []
z0 = []
printTower(x0,y0,z0)
towersOfHanoi(4, x0, y0, z0)

