#1
def count_matches(l,v):
    if not l:
        return 0
    if l[0] == v:
        return 1 + count_matches(l[1:],v)
    else:
        return count_matches(l[1:], v)

#2
def double_each(l):
    if not l:
        return []
    return [l[0]]*2 + double_each(l[1:])

#3
def sums_to(l, k):
    if not l:
        if k == 0: return True
        else: return False
    return sums_to( l[1:] , k-l[0])

#4
def is_reverse(s1,s2):
    if (not s1 and s2) or (s1 and not s2):
        return False
    if not s1 and not s2:
        return True
    if s1[0] == s2[-1]:
        return is_reverse(s1[1:],s2[0:-1])
    else :
        return False

#5
def sort_repeated(l):
    l2 = []
    # sort
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] > l[j] :
                l[i], l[j] = l[j], l[i]
    # compare
    buf = None
    for i in range(1,len(l)):
        if l[i-1] == l[i] and buf != l[i]:
            l2.append(l[i])
            buf = l[i]
    return l2
#def sort_repeated_short(l):
#    return sorted([x for x in set(l) if l.count(x) > 1])

#6-a
def make_Dict_number(l):
    d = {}
    k = []
    for n in l:
        exist = 0
        for e in k:
            if e == n :
                exist = 1
        if exist:
            d[n] += 1
        else:
            d[n] = 1
            k.append(n)
    return d

#6-b
def make_Dict_number(l):
    d = {}
    for n in l:
        if d.get(n):
            d[n] += 1
        else:
            d[n] = 1
    return d

def mostFrequent(l):
    d = make_Dict_number(l)
    mx_v, mx_cnt = 0, 0
    for k, v in d.items():
        if mx_cnt < v :
            mx_v, mx_cnt = k, v
    return mx_v

#7
def histogram(d):
    d2 = {}
    for e in d.values():
        d2[e] = list(d.values()).count(e)
    return d2
#def histogram_short(d):
#    return {v:list(d.values()).count(v) for v in d.values()}

