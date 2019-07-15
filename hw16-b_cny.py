# 16-B

example_print_flag = False

#1
def count_matches( lst, val ):
    if len( lst ) == 0 :
        return 0
    else :
        if val == lst[0] :
            return  1 + count_matches( lst[1:], val )
        else:
            return count_matches( lst[1:], val )

if example_print_flag :        
    print( "\n==[1번]==")       
    print( count_matches( [0,1,0,4,2,0], 0 ) )
    print( count_matches( ["a", "b", "c"], 1 ) )
    print( count_matches( [], "a" ) )

#2

nums = [1,2,3]
def double_each( lst ):
   if not lst:
       return []
   return  [ lst[0] ] * 2 + double_each( lst[1:] )

if example_print_flag :        
    print( "\n==[2번]==")    
    print( double_each( nums ) )
    print( nums )
    print( double_each( [] ) )
       

# 3
nums = [1,2,3]
def sums_to( nums, k ):
    if len( nums ) == 0 :
        if k == 0 :
            return True
        else :
            return False
    return sums_to( nums[1:], k-nums[0] )

if example_print_flag :        
    print( "\n==[3번]==")    
    print( sums_to(nums, 6) )
    print( sums_to(nums, 5) )
    print( sums_to([], 1) )

# 4
def is_reverse( str1, str2 ):
    if not str1 and not str2 :
        return True
    if ( not str1 and str2 ) or ( str1 and not str2 ) : 
        return False
    if str1[0] == str2[-1]:
        return is_reverse( str1[1:], str2[0:-1])
    else :
        return False

if example_print_flag :        
    print( "\n==[4번]==")    
    print( is_reverse( "abc", "cba" ) )
    print( is_reverse( "abc", "abc" ) )
    print( is_reverse( "abc", "dcba" ) )
    print( is_reverse( "abc", "cb" ) )
    print( is_reverse( "", "" ) )
    
# 5
def sort_repeated( L ):
        elm_set = set() 
        re_elm_set = set()
        for elm in L:
            if elm in elm_set:
                re_elm_set.add(elm)
            elm_set.add(elm)
        return sorted(re_elm_set)

if example_print_flag :
    print( "\n==[5번]==")        
    print( sort_repeated( [1,2,3,2,1] ) )
    print( sort_repeated( [1,2,3,2,2,4] ) )
    print( sort_repeated( list( range(100) ) ) )

    

# 6


# 7

def histogram(d):
    res_dict = {}
    for elm in d.values(): 
        if elm in res_dict:
            res_dict[elm] += 1
        else:
            res_dict[elm]  = 1
    return res_dict

if example_print_flag :
    print( "\n==[7번]==")      
    letters = { 1:"a", 2:"b", 3:"a" }
    print( histogram( letters ) )
    letters = { 1:"a", 2:"b", 3:"c" }
    print( histogram( letters ) )
    letters[4] = "a"
    letters[5] = "b"
    letters[6] = "a"
    print( histogram( letters ) ) 

        



        
        
