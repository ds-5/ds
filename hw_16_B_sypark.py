def count_matches(some_list, value):
    if some_list == [] : return 0
    else :
        if some_list[0] == value : return count_matches(some_list[1:], value) + 1
        else : return count_matches(some_list[1:], value)


def double_each(some_list):
    if some_list == [] : return some_list
    else : return  some_list[0:1]*2 + double_each(some_list[1:])


def sums_to(nums, k):
    if nums == [] :
        if k == 0 : return True
        else : return False
    else : return sums_to(nums[1:], k-nums[0])


def is_reverse(string1, string2):
    if string1 == "" or string2 == "" :
        if len(string1+string2) == 0 : return True
        else : return False
    elif string1[0] !=  string2[len(string2)-1] : return False
    else : return is_reverse(string1[1:], string2[:len(string2)-1])


def sort_repeated(L) :
    re_el = []
    new_el = []
    for el in L :
        if el not in new_el : new_el.append(el)
        else :
            if el not in re_el : re_el.append(el)
    for min in range(len(re_el)):
        min_index = min
        for i in range(min+1, len(re_el)):
            if re_el[min_index] > re_el[i] : min_index = i
        re_el[min_index], re_el[min] = re_el[min], re_el[min_index]
    return re_el


def make_Dict_number(lst) :
    make_dic = {}
    for i in lst:
        if i in make_dic.keys() : make_dic[i] += 1
        else : make_dic[i] = 1

    key_list = list(make_dic.keys())
    for min in range(len(key_list)):
        min_index = min
        for i in range(min+1, len(key_list)):
            if key_list[min_index] > key_list[i] : min_index = i
        key_list[min_index], key_list[min] = key_list[min], key_list[min_index]

    new_make_dic = {}
    for key in key_list : new_make_dic[key] = make_dic[key]

    return new_make_dic

#w/get
##def most_Frequent(lst) : 
##    #make_Dict_number
##    make_dic = {}
##    for i in lst:
##        if i in make_dic.keys() : make_dic[i] += 1
##        else : make_dic[i] = 1
##
##    max_key = list(make_dic.keys())[0]
##    max_freq = make_dic.get(max_key)
##    
##    for key in list(make_dic.keys()) :
##        if max_freq < make_dic.get(key) :
##            max_freq = make_dic.get(key)
##            max_key = key
##            
##    return max_key

#wo/get
def most_Frequent(lst) : 
    #make_Dict_number
    make_dic = {}
    for i in lst:
        if i in make_dic.keys() : make_dic[i] += 1
        else : make_dic[i] = 1

    max_key = list(make_dic.keys())[0]
    max_freq = make_dic[max_key]
    
    for key in list(make_dic.keys()) :
        if max_freq < make_dic[key] :
            max_freq = make_dic[key]
            max_key = key
            
    return max_key


def histogram(d) : 
    chg_dic = {}
    value_list = list(d.values())
    for v in value_list:
        chg_dic[v] = value_list.count(v)

    return chg_dic


