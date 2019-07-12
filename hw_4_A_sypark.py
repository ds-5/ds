def f1(i_list):
    cnt=0
    for i in i_list:
        if i%2 == 1 : cnt = cnt+1
    return cnt

def f2(i_list):
    for i in i_list:
        if i%2 == 1 : print(i)

def f3(i_list):
    sum=0
    for i in i_list:
        if i%2 == 1 : sum = sum+i
    return sum

def f4(i_list):
    sum = 0
    for i in range(len(i_list)):
        if i_list[i]%2 == 1 : sum = sum+i
    return sum

def f5(i_list):
    sqr = []
    for i in i_list : sqr.append(i**2)
    return sqr

def f6(i_list):
    if len(i_list) != 0:
        max = i_list[0]
        for i in i_list :
            if i > max : max = i
        return max
        
def f7(i_list):
    if len(i_list) != 0:
        sum=0
        for i in i_list:sum = sum+i
        return sum/len(i_list)

def f8(a,b,n):
    for i in list(range(a,b+1)):
        if i%n==0 : print(i)

def f9(w,h):
    line = "*"*w
    for i in range(h):print(line)

def f10(n):
    for i in range(n):
        line = "*"*(i+1)
        print(line)

def f11(i_list):
    desc=True
    for i in range(len(i_list)-1) :
        if i_list[i] <= i_list[i+1] : desc = False
    return desc

def f12(i_list):
    res = True
    for i in range(len(i_list)) :
        if i_list[i] >= 0 : res = False
    return res

def f13(i_list, i_tar):
    find = -1
    for i in range(len(i_list)) :
        if i_list[i] == i_tar : find = i
    return find

def f14(i_list):
    find = -1
    for i in range(len(i_list)) :
        if i_list[i] < 0 : find = i
    return find

def f15(i_list):
    sum = 0
    for i in range(len(i_list)):
        if i%2 == 0 : sum = sum+i_list[i]
    return sum

def f16(n):
    for i in range(n):
        line = "*"*(n-i)
        print(line)

def f17(i_list):
    for i in range(len(i_list)):
        if (len(i_list)%2==0 and i%2==1) :print(i_list[len(i_list)-i])
        if (len(i_list)%2==1 and i%2==0) :print(i_list[len(i_list)-1-i])
            

def f18(n):
    fac = 1
    for i in range(n): fac = fac*(i+1)
    return fac


def f19(i_list):
    for i in i_list :
        fac = 1
        for n in range(i) :fac = fac*(n+1)
        print (fac)

def f20(i_list): 
    for i in i_list :
        line = []
        for n in range(i+1) : line.append(n)
        print(*line) 
    print()

def f21(i1_l, i2_l):
    s_l = []
    for i1 in range(len(i1_l)):
        for i2 in range(len(i2_l)):
            if i1==i2 : s_l.append(i1_l[i1]+i2_l[i2])
    return s_l

def f22(n):
    for i in range(1, n+1):
        if i%2==0 or i%3==0 : print(i)


def f23(i_list):
    max = i_list[0][0]
    for i1 in i_list :
        for i2 in i1 :
            if max < i2 : max = i2
    return max
        
def f24(values):
    max_v = values[0]
    max_i = 0
    
    for i in range(len(values)):
        if max_v < values[i] :
            max_v = values[i]
            max_i = i
    new_values = values[:max_i]+values[max_i+1:]
    max_v = new_values[0]
        for i in range(len(new_values)):
        if max_v < new_values[i] : max_v = new_values[i]

    return max_v
        

def f25(n):
    return n//10**(len(str(n))-1)


def f26(i_list):
    for i1 in i_list :
        max = i1[0]
        for i2 in i1 :
            if max < i2 : max = i2
        print(max)






























































