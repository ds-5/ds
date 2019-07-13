## NO.1
def first_perfect_square(l):
    for i in range(len(l)):
        if l[i] >= 0:
            if l[i] ** 0.5 % 1 == 0:
                return i
    return -1

## NO.2
def num_perfect_squares(l):
    cnt = 0
    for i in l:
        if i >= 0:
            if i ** 0.5 % 1 == 0:
                cnt += 1
    return cnt

## NO.3
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

## NO.4
def print_french(lo, hi):
    for i in range(lo,hi+1):
        print(i, num_in_french(i))
    return None

def num_in_french(num): #assumes 0 <= num <= 100
    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six",
                 "sept", "huit", "neuf", "dix", "onze", "douze",
                 "treize", "quatorze", "quinze", "seize", "dix-sept",
                 "dix-huit", "dix-neuf"]    # 0~19
    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante",
                 "soixante", "soixante", "quatre-vingt","quatre-vingt"] # 00~90
# EXCEPTION
    if num == 100:
        return 'cent'
# INIT
    system, sep = 20, ''
    tens, ones = '', ''
    if 20 < num < 60:
        system = 10
# TENS
    if num >= system:
        tens = tens_list[num//10]
    if num == 80:
        tens += 's'
# ONES
    if num == 0 or num%system != 0:
        ones = ones_list[num%system]
# SEPERATOR
    if tens and num < 80 and num % 10 == 1:
        sep = ' et '
    elif tens and num % system:
        sep = '-'
    return tens + sep + ones
