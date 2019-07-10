def f1(n):
    for i in range(1,n+1):
        jl = []
        for j in range(1,i+1):
            jl.append(j)
        print(*jl)

        
def f2(n):
    s = 1
    for i in range(n):
        jl = []
        for j in range(i+1):
            jl.append(s)
            s += 1
        print(*jl)


def f3(n):
    s = 1
    for i in range(1,n+1):
        jl = []
        for j in range(i):
            jl.append(s)
            s += 1
        print(*jl)
    for i in range(n-1,0,-1):
        s -= 2*i+1
        jl = []
        for j in range(i):
            jl.append(s)
            s += 1
        print(*jl)


def f4(n):
    s = 1
    for i in range(1,2*n+1):
        sl = []
        if i>n: i = 2*n-i
        for j in range(i):
            sl.append(s)
            s+=1
        print(*sl)

def f5(m):
    for i in m:
        var = 0
        for j in i:
            var += j
        print(var)

def f6(m):
    for i in range(len(m)):
        print(m[i][i])

def f7(m):
    for i in m:
        var = 0
        for j in i:
            var += j
        print(var)

def f8(m):
    v = 0
    for i in m:
        for j in i:
            v += j
    return v

def f9(m):
    v = 1
    for i in m:
        for j in i:
            v*= j
    return v
    
def f10(m):
    for i in m:
        jl = []
        for j in i:
            if j %2:
                jl.append(j)
        print(*jl)

def f11(m1,m2):
    m = []
    for i in range(len(m1)):
        m.append([])
        for j in range(len(m1[0])):
            m[i].append(m1[i][j] + m2[i][j])
    return m


def f12(m1,m2):
    r1,c1,r2,c2 = len(m1),len(m1[0]),len(m2),len(m2[0])
    m=[[0]*c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                m[i][j] += m1[i][k] * m2[k][j]
    return m

    
def f13(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j:
                if not m[i][j] == 1:
                    return False
            else:
                if not m[i][j] == 0:
                    return False
    return True


def f14(r,c):
    m = [[] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            v = 4
            if i == 0   : v -= 1
            if i == r-1 : v -= 1
            if j == 0   : v -= 1
            if j == c-1 : v -= 1
            m[i].append(v)
    return m








    

