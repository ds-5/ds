import def_pbh as s1
import def_sypark as s2
import sys, filecmp, random
from inspect import getmembers, isfunction

def dim_1(_length=10, _from=-100, _to=100):
    l = []
    for _ in range(random.randint(0,_length)):
        l.append(random.randint(_from,_to))
    return l

def run(func, arg, log_file):
    org = sys.stdout
    sys.stdout = open(log_file, 'w')
    r = func[1](arg)
    sys.stdout.close()
    sys.stdout = org
    return r

# def 개수 검사
m1, m2 = getmembers(s1), getmembers(s2)
if len(m1) != len(m2):
    print('[ERROR] function count = %d, %d' % (len(m1), len(m2)))
    sys.exit()

# def 결과 검사
HW4 = {
    # ERROR
        # bool type string : f11, f12
        # 라인 별 마지막 공백 : f20
        # [] 입력하는 경우 IndexError : f6, f7
    'dim1': ['f1', 'f2', 'f3', 'f4', 'f5', 'f15', 'f17', 'f19'],  # test용!! error 제외
    #'dim1': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f11', 'f12', 'f15', 'f17', 'f19', 'f20', 'f26'],
    'dim1_asm_neg_var1' : 'f14',
    'dim1_asm_var2' : 'f24',
    'dim2': ['f23'],
    'dim2_asm_not_empty' : ['f26'],
    'dim1_dim1': ['f21'],  # same length
    'dim1_num1': ['f13'],
    'num1': ['f10', 'f16', 'f18', 'f22', 'f25'],
    'num2': ['f9'],
    'num3': ['f8'],
}

cnt = [0, 0]
for f1, f2 in sorted(zip(m1, m2)):
    if isfunction(f1[1]):
        cnt[0] += 1
        test_case = []
        for k, v in HW4.items():
            if f1[0] in v and k == 'dim1':
                for i in range(1000): test_case.append(dim_1())

        if not test_case :
            print('skip! {}'.format(f1[0]))
            continue

        for test_no, arg in enumerate(test_case) :
            #  def 수행
            log1, log2 = 'tmp1.txt', 'tmp2.txt'
            r1, r2 = run(f1, arg, log1), run(f2, arg, log2)

            # def 판정
            if r1 != r2:
                print('return fail {} #{}'.format(f1[0], test_no))
                print('{}\narg=<{}>\ndef1=<{}>\ndef2=<{}>'.format('-'*20,arg,r1,r2))
                sys.exit()
            elif open(log1).read() != open(log2).read():
                print('print fail {} #{}'.format(f1[0], test_no))
                print('{}\narg=<{}>\ndef1=<{}>\ndef2=<{}>'.format('-'*20,arg,open(log1).read(), open(log2).read()))
                sys.exit()
        print('pass! {}'.format(f1[0]))
        cnt[1] += 1
print('finish! (total={}, pass={})'.format(cnt[0],cnt[1]))
