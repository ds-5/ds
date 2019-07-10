def f1(i_list):
    if i_list == [] : return 0
    else : return i_list[0] + f1(i_list[1:])
    
def f2(n):
    if n == 1: return 1
    else:
        if n%2==0 : return f2(n//2)+1
        else : return f2(3*n+1)+1

def f3(i_list):
    if i_list != [] :
        f3(i_list[1:])
        print(i_list[0])

def f4(i_list):
    if i_list != []:
        if ((i_list[0]*3)%2 == 1) : print(i_list[0]*3)
        f4(i_list[1:])
        
def f5(i_list):
    if i_list != []:
        f5(i_list[1:])
        if ((i_list[0]*3)%2 == 1) : print(i_list[0]*3)
        else : print(i_list[0])

def f6(i_list):
    if i_list == []: return i_list
    else :
        if (type(i_list[0]) == list) : return f6(i_list[0])+f6(i_list[1:])
        else : return [i_list[0]] + f6(i_list[1:])

def f7(n):
    if n == 0 : return 2
    elif n == 1 : return 1 
    else : return f7(n-1)+f7(n-2)

def f8(s):
    chk = "True"
    if s != "" :
        if len(s) != 1 :
            if s[0] != s[-1] : chk = "False"
            else : f8(s[1:-2])
    return chk

def f9(n):
    if n == 0 : return 1
    else : return n*f9(n-1)

def f10(i_list):
    if i_list==[] : return 0
    else : return f10(i_list[1:])+1

def f11(i_list):
    if len(i_list) == 1 : return i_list[0]
    elif len(i_list) == 0 :return
    else : return f11(i_list[1:])

def f12(n):
    if n == 0 : return
    else :
        print(n)
        return f12(n-1)
    
def f13(n):
    if n//10 == 0 : return 1
    else : return f13(n//10) + 1

def f14(i_list):
    if i_list == [] :return
    else :
        if i_list[0]%2==1 : return i_list[0]
        else : return(f14(i_list[1:]))

def f15(i_list):
    if i_list == [] :return 0
    else :
        if i_list[0]%2==1 : return f15(i_list[1:]) + i_list[0]
        else : return (f15(i_list[1:]))

def f16(i_list):
    if i_list == [] :return []
    else :
        if i_list[0]%2==1 : return [i_list[0]] + f16(i_list[1:])
        else : return (f16(i_list[1:]))

def f17(i_list):
    if len(i_list) == 0 : return -1
    else : return f17(i_list[1:])+1
    
def f18(a,b):
    if a>b :
        if a%b==0 : return b
        else : return f18(b, a%b)
    else :
        if b%a==0 : return a
        else : return f18(a, b%a)

def f19(lst1, lst2):
    index1 = 0
    index2 = 0
    tot = []
    while index1 < len(lst1) and index2 < len(lst2) :
        if lst1[index1] > lst2[index2] :
            tot.append(lst2[index2])
            index2 += 1
        else :
            tot.append(lst1[index1])
            index1 += 1
    tot.extend(lst1[index1:])
    tot.extend(lst2[index2:])
    return tot

def f20(list) :
    if len(list) == 0 or len(list) == 1 : return list[:len(list)]
    mid = len(list)//2
    t_list1 = list[0:mid]
    t_list2 = list[mid:len(list)]
    list1 = f20(t_list1)
    list2 = f20(t_list2)
    new_list = f19(list1, list2)
    return new_list
        














        

