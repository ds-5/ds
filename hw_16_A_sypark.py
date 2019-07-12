def first_perfect_square(numbers):
    f_p_s = -1 
    for i in range(len(numbers)):
        if numbers[i] >= 0 :
            if ((numbers[i] ** 0.5)%1 == 0) :
                f_p_s = i
                break
    return f_p_s

#####################################################################

def num_perfect_squares(numbers):
    n_p_s = 0 
    for i in range(len(numbers)):
        if numbers[i] >= 0 :
            if ((numbers[i] ** 0.5)%1 == 0) :
                n_p_s += 1
    return n_p_s

#####################################################################

def second_largest(values):
    max_v = values[0]
    max_i = 0
    for i in range(len(values)):
        if max_v < values[i] :
            max_v = values[i]
            max_i = i
    new_values = values[:max_i]+values[max_i+1:]
    max_v = new_values[0]    
    for i in range(len(new_values)):
        if max_v < new_values[i] : max_v = new_values[i]
    return max_v

#####################################################################
# print french for the numbers between lo and hi (inclusive) def print_french(lo, hi): return None

#Part 3
def print_french(l, h):
    for i in range(l, h+1):
        print (i, end = " ")
        print (num_in_french(i)) 

def digit(num, pos):
    return (num // 10**(pos-1)) % 10

def num_in_french(num): # assumes 0 <= num <= 100
    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix","onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    # Part 1: get the ones and tens digits of num
    ten_d = digit(num, 2)
    one_d = digit(num, 1)
    
    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    if num == 100 : return "cent"
    elif num >= 0 and num < 20 : return ones_list[num]

    # Part 4: case when the numbers are 70, 71, 72,...79, and 90, 91, 92,...99
    elif num == 60 : return tens_list[ten_d]
    elif num == 61 or num == 71 : return tens_list[ten_d]+" et "+ones_list[num%20]
    elif num > 61 and num < 80 : return tens_list[ten_d]+"-"+ones_list[num%20]
    elif num == 80 : return tens_list[ten_d]+"s"
    elif num > 80 and num < 100 : return tens_list[ten_d]+"-"+ones_list[num%20]

    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...
    elif one_d == 0 : return tens_list[ten_d]

    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...
    elif one_d == 1 : return tens_list[ten_d]+" et "+ones_list[one_d]

    # Part 7: everything else, the most general case for 22, 23, ... 29, 32, 33, ..., 39, 42, ...
    else : return tens_list[ten_d]+"-"+ones_list[one_d]










