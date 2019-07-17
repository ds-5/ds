
def f1(l):
    if not l:
        return 0
    else:
        return l[0]+f1(l[1:])


def f2(n):
    if n == 1:
        return 1
    else :
        if n%2 :
            return f2(3*n+1)+1
        else:
            return f2(n//2)+1


def f3(l):
    if len(l) == 0:
        return
    else :
        f3(l[1:])
        print(l[0])


def f4(l):
    if l:
        if l[0] %2 :
            print(l[0]*3)
        f4(l[1:])

def f5(l):
    if l:
        f5(l[1:])
        if l[0] % 2 :
            print(l[0]*3)
        else:
            print(l[0])
        
def f6(l):
    if l :
        if type(l[0]) == list :
            return f6(l[0]) + f6(l[1:])
        else :
            return [l[0]] + f6(l[1:])
    return []


def f7(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return f7(n-2) + f7(n-1)


def f8(s):
    if len(s) > 1:
        if s[0] != s[-1] or not f8(s[1:-1]) :
            return False
    return True

def f9(n):
    if n < 2 :
        return 1
    else :
        return n * f9(n-1)


def f10(l):
    if l:
        return f10(l[1:]) + 1
    else :
        return 0

def f11(l):
    if l :
        if len(l)==1:
            return l[0]        
        else:
            return f11(l[1:])
    return

def f12(n):
    if n>0:
        print(n)
        f12(n-1)

def f13(n):
    if n < 10:
        return 1
    else:
        return f13(n//10) + 1


def f14(l):
    if l:
        if l[0] % 2:
            return l[0]
        return f14(l[1:])
    else :
        return 


def f15(l):
    if l:
        if l[0] % 2:
            return l[0] + f15(l[1:])
        else :
            return f15(l[1:])
    else:
        return 0

def f16(l):
    if l:
        if l[0] % 2:
            return [l[0]]+f16(l[1:])
        else:
            return f16(l[1:])
    else:
        return []

def f17(l):
    if len(l) == 2:
        return l[0]
    else :
        return f17(l[1:])

def f18(a,b):
    if b>a :
        a, b = b, a
    if a%b :
        return f18(b,a%b)
    else:
        return b


def f19(l1,l2):
    if l1 and l2:
        if l1[0] > l2[0]:
            return [l2[0]]+f19(l1, l2[1:])
        else:
            return [l1[0]]+f19(l1[1:], l2)
    else :
        return l1+l2

def f20(l):
    if len(l) < 2 :
        return l
    return f19(f20(l[:len(l)//2]),f20(l[len(l)//2:]))

    
