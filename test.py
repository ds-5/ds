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
mb1, mb2 = getmembers(s1), getmembers(s2)
if len(mb1) != len(mb2):
    print('[ERROR] function count = %d, %d\n\n\n' % (len(mb1), len(mb2)))
    #sys.exit()
# 멤버 중 공통 함수 추출하기
func_list_a, func_list_b = set([e[0] for e in mb1]), set([e[0] for e in mb2])
common = func_list_a.intersection(func_list_b)
m1 = [e for e in mb1 if isfunction(e[1]) and e[0] in common]
m2 = [e for e in mb2 if isfunction(e[1]) and e[0] in common]

# def 결과 검사
HW = {
    # HW10 TEST

    # WARNING
        # f2 = 1보다 작은 경우 무한 루프(pbh, sypark)
        # f12 = 음수일 경우 무한 루프(sypark)
        # f13 = -1 일 경우 무한 루프(sypark)
    # ERROR
        # f8 = slice 틀림 (sypark)
        # f17 = 개수 세는 프로그램? (sypark)
    # EXCEPTION
        # f6 : 불규칙적인 list 형태

    # CASE
    #'dim1':['f1','f3','f4','f5','f10','f11','f14','f15','f16','f20'],
    #'dim1_len_over_1':['f17'],
    #'dim1_dim1_sorted':['f19'],
    #'num1_over_0':['f2'],
    #'num1_pos':['f9','f12','f13'],
    'num1_pos_max_25':['f7'],
    #'num2_pos':['f18'],
    #'str1':['f8'],
}

cnt = [0, 0, 0]
for f1, f2 in sorted(zip(m1, m2)):
    #print(f1[0],f2[0])
    if 1:
        cnt[0] += 1
        test_case = []
        for k, v in HW.items():
            if f1[0] in v and k == 'dim1':
                for i in range(1000): test_case.append([dim_1()])
            if f1[0] in v and k == 'dim1_len_over_1':
                for i in range(1000):
                    generated = dim_1()
                    if len(generated) > 1 : test_case.append([generated])
            elif f1[0] in v and k == 'dim1_num1':
                for i in range(1000): test_case.append([dim_1(size=(1,10)), random.randint(-100,100)])
            elif f1[0] in v and k == 'dim1_asm_var2':
                for i in range(1000): test_case.append([dim_1(size=(2,10))])
            elif f1[0] in v and k == 'dim1_asm_neg_var1':
                for i in range(1000): test_case.append([dim_1(asm_neg_var=1)])
            elif f1[0] in v and k == 'dim1_dim1_asm_same_length':
                length = random.randint(0,10)
                for i in range(1000): test_case.append([dim_1(size=(length,length)),dim_1(size=(length,length))])
            elif f1[0] in v and k == 'dim1_dim1_sorted':
                for i in range(1000):
                    test_case.append([sorted(dim_1()),sorted(dim_1())])
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
                for i in range(1000):
                    test_case.append([random.randint(-500, 500)])
            elif f1[0] in v and k == 'num1_over_0':
                for i in range(1000):
                    test_case.append([random.randint(1, 100_000)])
            elif f1[0] in v and k == 'num1_pos':
                for i in range(1000):
                        test_case.append([random.randint(0, 200)])
            elif f1[0] in v and k == 'num1_pos_max_25':
                for i in range(25):
                        test_case.append([i])
            elif f1[0] in v and k == 'str1':
                for i in range(1000): #test_case.append([random.randint(-100000, 100000)])
                    string = ''
                    for _ in range(random.randint(0,20)):
                        string += chr(random.randint(97,122)) # lower alphabet
                    test_case.append([string])
            elif f1[0] in v and k == 'num2':
                for i in range(1000): test_case.append([random.randint(-100, 100),random.randint(-100, 100)])
            elif f1[0] in v and k == 'num2_pos':
                for i in range(1000): test_case.append([random.randint(1, 100),random.randint(1, 100)])
            elif f1[0] in v and k == 'num3_asm_3rd_pos':
                for i in range(1000): test_case.append([random.randint(-100, 100),random.randint(-100, 100),random.randint(1, 100)])


        if not test_case :
            print('skip! ----------------> {}'.format(f1[0]))
            cnt[2] += 1
            continue

        for test_no, args in enumerate(test_case) :
            #  def 수행
            log1, log2 = 'tmp1.txt', 'tmp2.txt'
            try :
                r1, r2 = run(f1, args, log1), run(f2, args, log2)
            except :
                print('ERROR ARGS =', args, f1, f2)
                sys.exit()

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
