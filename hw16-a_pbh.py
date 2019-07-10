
def first_perfect_square(l):
    for i in range(len(l)):
        if l[i] >= 0:
            if l[i] ** 0.5 % 1 == 0:
                return i
    return -1

def num_perfect_squares(l):
    cnt = 0
    for i in l:
        if i >= 0:
            if i ** 0.5 % 1 == 0:
                cnt += 1
    return cnt

def second_largest(l):
    mx_i = 0
    for i in range(len(l)):
        if l[mx_i] < l[i]:
            mx_i = i
    l2 = l[:mx_i]+l[mx_i+1:]
    mx_v = l2[0]
    for v in l2:
        if mx_v < v:
            mx_v = v
    return mx_v

