def f1(l):
    cnt = 0
    for n in l:
        if n % 2:
            cnt += 1
    return cnt


def f2(l):
    for n in l:
        if n % 2:
            print(n)


def f3(l):
    sum = 0
    for n in l:
        if n % 2:
            sum += n
    return sum


def f4(l):
    sum = 0
    for n in range(len(l)):
        if l[n] % 2:
            sum += n
    return sum


def f5(l):
    m = []
    for n in l:
        m.append(n * n)
    return m


def f6(l):
    if not l:
        return
    max_n = l[0]
    for n in l:
        if n > max_n:
            max_n = n
    return max_n


def f7(l):
    if not l :
        return
    sum = 0
    for n in l:
        sum += n
    return sum / len(l)


def f8(a, b, n):
    for i in range(a, b + 1):
        if i % n == 0:
            print(i)


def f9(width, height):
    for r in range(height):
        for c in range(width):
            print('*', end='')
        print('')


def f10(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        print('')


def f11(l):
    if len(l):
        i = l[0]
        for n in l[1:]:
            if i < n:
                return False
            i = n
    return True


def f12(l):
    if len(l):
        for n in l:
            if n >= 0:
                return False
    return True


def f13(l, t):
    index = 0
    for i in range(len(l)):
        if t == l[i]:
            index = i
    return index


def f14(l):
    index = 0
    for i in range(len(l)):
        if l[i] < 0:
            index = i
    return index


def f15(l):
    sum_var = 0
    for i in range(len(l)):
        if i % 2 == 0:
            sum_var += l[i]
    return sum_var


def f16(n):
    for i in range(n):
        print('*' * (n - i))


def f17(l):
    if len(l):
        for i in range(len(l) - 1, -1, -2):
            if i >= 0:
                print(l[i])


def f18(n):
    v = 1
    if n >= 2:
        for i in range(n):
            v *= (i + 1)
    return v


def f19(l):
    for n in l:
        v = 1
        if n >= 2:
            for i in range(n):
                v *= (i + 1)
        print(v)


def f20(l):
    for n in l:
        vl = []
        for i in range(n + 1):
            vl.append(n - i)
        print(*vl)


def f21(l1, l2):
    l = []
    for i in range(len(l1)):
        l.append(l1[i] + l2[i])
    return l


def f22(n):
    for i in range(1, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


def f23(l):
    mx = l[0][0]
    for i in l:
        for j in i:
            if j > mx:
                mx = j
    return mx


def f24(l):
    if l[0] > l[1]:
        mx_1, mx_2 = l[0], l[1]
    else:
        mx_1, mx_2 = l[1], l[0]
    for n in l[2:]:
        if n > mx_1:
            mx_1, mx_2 = n, mx_1
        elif n > mx_2:
            mx_2 = n
    return mx_2


def f25(n):
    while (n // 10):
        n //= 10
    return n


def f26(l):
    for i in l:
        mx = i[0]
        for j in i[1:]:
            if j > mx:
                mx = j
        print(mx)
