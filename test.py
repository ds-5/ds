import def_a as s1
import def_b as s2
import sys, filecmp
from inspect import getmembers, isfunction

def run(func, log_file):
    o = sys.stdout
    sys.stdout = open(log_file, 'w')
    r = func()
    sys.stdout = o
    return r
'''
m1, m2 = getmembers(s1), getmembers(s2)
if len(m1) != len(m2):
    print('[ERROR] function count = %d, %d' % (len(m1), len(m2)))
    sys.exit()

for f1, f2 in zip(m1, m2):
    if isfunction(f1[1]):
        log1, log2 = '{}_ans1.txt'.format(f1[0]), '{}_ans2.txt'.format(f2[0])
        r1 = run(f1[1], log1)
        r2 = run(f2[1], log2)
        if r1 != r2:
            print('[FAIL] {}'.format(f1[0]))
            print('>>>{}'.format(r1))
            print('>>>{}'.format(r2))
        print(r1,r2)
        
        if filecmp.cmp(log1, log2):
            print('cmp pass!', log1, log2)
            print('{}'.format(open(log1).read()))
            print('{}'.format(open(log2).read()))
        else:
            print('[FAIL] {}'.format(f1[0]))
            print('>>>{}'.format(open(log1).read()))
            print('>>>{}'.format(open(log2).read()))
'''


import random
def gen_list(nth, mx_r=1000, mx_c=1000, mx_var=100000):
    r, c = random.randint(0, mx_r), random.randint(0,mx_c)
    return [[random.randint(0, mx_var)]* for _ in range(mx_r)]            

print(gen_list(1,4,4))

            









