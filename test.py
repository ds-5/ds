import def_pbh as s1
import def_sypark as s2
import sys, filecmp, random
from inspect import getmembers, isfunction

def dim_1(size=(0,10), val=(-100,100), asm_neg_var=0):
    l = []
    for _ in range(random.randint(size[0],size[1])):
        l.append(random.randint(val[0],val[1]))
    if asm_neg_var:
        l.insert(random.randint(0,len(l)), random.randint(val[0],-1))
    return l

def dim_2(n=2,rn=0,row=(0,10),col=(0,10),val=(-20,20),empty_start=1):
    if n == 0:
        return random.randint(0,9)
    l = []
    if n == 2 : var = list(row)
    else : var = list(col)
    if empty_start == 0 and n == 1 and rn == 0 :
        var[0] = 1
    for j in range(random.randint(var[0],var[1])) :
            l.append(dim_2(n=n - 1, rn=j, row=row, col=col, empty_start=empty_start))
    return l

def run(func, args, log_file):
    org = sys.stdout
    sys.stdout = open(log_file, 'w')
    if len(args) == 0:
        r = func[1]()
    elif len(args) == 1:
        r = func[1](args[0])
    elif len(args) == 2:
        r = func[1](args[0],args[1])
    elif len(args) == 3:
        r = func[1](args[0], args[1],args[2])
    sys.stdout.close()
    sys.stdout = org
    return r

# def 개수 검사
m1, m2 = getmembers(s1), getmembers(s2)
if len(m1) != len(m2):
    print('[ERROR] function count = %d, %d' % (len(m1), len(m2)))
    sys.exit()

# def 결과 검사
HW = {
    # HW4 TEST
    # ERROR
        # f11 : 같은 값일 때 내림 정렬인가? (True / False)
        # f20 : def2 line 마지막 공백?
        # f25 : def 문자 반환?
    #'dim1': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f12', 'f15', 'f17', 'f19'], #pass #'dim1': ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f11', 'f12', 'f15', 'f17', 'f19', 'f20'],
    #'dim1_asm_neg_var1' : ['f14'],             #pass
    #'dim1_asm_var2' : ['f24'],             #pass
    #'dim2_asm_not_empty': ['f26'],          #pass
    #'dim2_asm_not_empty_start' : ['f23'],   #pass
    #'dim1_dim1_asm_same_length': ['f21'],   #pass
    #'dim1_num1': ['f13'],                   #pass
    #'num1': ['f10', 'f16', 'f18', 'f22'], #pass #'num1': ['f10', 'f16', 'f18', 'f22', 'f25'],
    #'num2': ['f9'],                        #pass
    #'num3_asm_3rd_pos': ['f8'],            #pass

    #HW6 TEST
    #ERROR
        # f1 : def2 에서 newline 포함.
        # f2,f3,f4,f10 : def2 에서 line 마지막 space
    #'num1' : ['f1','f2','f3','f4'],
    #'num2' : ['f14'],   #pass
    'dim2' : ['f5','f7','f8','f9','f10'],
    #'dim2_square' : ['f6','f13'],   #pass
    #'dim2_dim_2_same' : ['f11'],   #pass
    #'dim2_c_eq_r' : ['f12'],       #pass
}

cnt = [0, 0, 0]
for f1, f2 in sorted(zip(m1, m2)):
    if isfunction(f1[1]):
        cnt[0] += 1
        test_case = []
        for k, v in HW.items():
            if f1[0] in v and k == 'dim1':
                for i in range(1000): test_case.append([dim_1()])
            elif f1[0] in v and k == 'dim1_num1':
                for i in range(1000): test_case.append([dim_1(size=(1,10)), random.randint(-100,100)])
            elif f1[0] in v and k == 'dim1_asm_var2':
                for i in range(1000): test_case.append([dim_1(size=(2,10))])
            elif f1[0] in v and k == 'dim1_asm_neg_var1':
                for i in range(1000): test_case.append([dim_1(asm_neg_var=1)])
            elif f1[0] in v and k == 'dim1_dim1_asm_same_length':
                length = random.randint(0,10)
                for i in range(1000): test_case.append([dim_1(size=(length,length)),dim_1(size=(length,length))])
            elif f1[0] in v and k == 'dim2_square':
                length = random.randint(0,10)
                for i in range(1000): test_case.append([dim_2(row=(length,length),col=(length,length))])
            elif f1[0] in v and k == 'dim2_dim2_same':
                dim_r = random.randint(0,10)
                dim_c = random.randint(0,10)
                for i in range(1000): test_case.append([dim_2(row=(dim_r,dim_r),col=(dim_c,dim_c)),dim_2(row=(dim_r,dim_r),col=(dim_c,dim_c))])
            elif f1[0] in v and k == 'dim2_c_eq_r':
                dim_r1 = random.randint(0,10)
                dim_c1 = random.randint(0,10)
                dim_c2 = random.randint(0, 10)
                for i in range(1000): test_case.append([dim_2(row=(dim_r1,dim_r1),col=(dim_c1,dim_c1)),dim_2(row=(dim_c1,dim_c1),col=(dim_c2,dim_c2))])
            elif f1[0] in v and k == 'dim2':
                for i in range(1000): test_case.append([dim_2()])
            elif f1[0] in v and k == 'dim2_asm_not_empty':
                for i in range(1000): test_case.append([dim_2(row=(1,10),col=(1,10))])
            elif f1[0] in v and k == 'dim2_asm_not_empty_start':
                for i in range(1000): test_case.append([dim_2(row=(1,10),col=(0,10),empty_start=0)])
            elif f1[0] in v and k == 'num1':
                for i in range(1000): test_case.append([random.randint(-100, 100)])
            elif f1[0] in v and k == 'num2':
                for i in range(1000): test_case.append([random.randint(-100, 100),random.randint(-100, 100)])
            elif f1[0] in v and k == 'num3_asm_3rd_pos':
                for i in range(1000): test_case.append([random.randint(-100, 100),random.randint(-100, 100),random.randint(1, 100)])


        if not test_case :
            print('skip! {}'.format(f1[0]))
            cnt[2] += 1
            continue

        for test_no, args in enumerate(test_case) :
            #  def 수행
            log1, log2 = 'tmp1.txt', 'tmp2.txt'
            r1, r2 = run(f1, args, log1), run(f2, args, log2)

            # def 판정
            if r1 != r2:
                print('return fail {} #{}'.format(f1[0], test_no))
                print('{}\narg=<{}>\ndef1=<{}>\ndef2=<{}>'.format('-'*20,args,r1,r2))
                sys.exit()
            elif open(log1).read() != open(log2).read():
                print('print fail {} #{}'.format(f1[0], test_no))
                print('{}\narg=<{}>\ndef1=<{}>\ndef2=<{}>'.format('-'*20,args,open(log1).read(), open(log2).read()))
                sys.exit()
        print('pass! {}'.format(f1[0]))
        cnt[1] += 1
print('finish! (total={}, pass={}, skip={})'.format(cnt[0],cnt[1],cnt[2]))
