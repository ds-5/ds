# 10-A-Recursion-Practice-26pp.pdf
example_print_flag = True

def f1( lst ):
    #슬라이싱 사용
    # lst[0] + f1(lst[1:])
    if len( lst ) == 0:
            return 0
    else:
            return lst[0] + f1( lst[1:] )

if example_print_flag :
        print( "\n==[1번]==")      
        print( f1( [1,2,3,4] ) )
        print( f1( [] ) )

def f2(n):
    if n == 1:
        return 1
    else :
        if n%2 :
            return f2( 3*n+1 )+1
        else:
            return f2( n//2 )+1
    
if example_print_flag:
        print( "\n==[2번]==")      
        print( f2( 1 ) )
        print( f2( 6 ) )
        print( f2( 11) )
        print( f2 ( 637228127 ) )

def f3(lst):
    if len( lst ) == 0:
        return
    else:
        f3( lst[1:] )
        print ( lst[0] )

if example_print_flag:
        print( "\n==[3번]==")    
        f3( [1,2,3] )
        f3( [] )
        f3( [3,2,1] )

def f4( lst ):
    if lst :
        if lst[0] %2 :
            print( lst[0] * 3 )
        f4( lst[1:] )

if example_print_flag:
        print( "\n==[4번]==")    
        f4( [1,2,3,4] )
        f4( [2,4] )
        f4( [11,42,63,15] )
        
def f5( lst ):
    if len( lst ) == 0:
        return
    else:
        f5( lst[1:] )
        if lst[0] % 2 == 1 :
            print( lst[0] * 3)
        else:
            print( lst[0] )
            
if example_print_flag:
        print( "\n==[5번]==")
        f5( [1,2,3,4] )
        f5( [2,4] )        
        f5( [11,42,64,15] )

def f6( lst ):
    if lst :
        if type( lst[0] ) == list :
            return f6( lst[0] ) + f6( lst[1:] )
        else :
            return [ lst[0] ] + f6( lst[1:] )
    return []

if example_print_flag:
        print( "\n==[6번]==")
        print( f6(['baa']) ) 
        print( f6(['baa', [4, True, [10, 5], [1, 2, ['moo']]], ["chirp"]]) )
        print( f6([]) )
        print( f6([[[[[[[[[[[[[[23]]]]]]]]]]]]]]) )
        
def f7( n ):
    if n ==0:
        return 2
    elif n == 1:
        return 1
    else: 
        return f7(n-1)+f7(n-2)

if example_print_flag:
        print( "\n==[7번]==")
        print( f7(3) )
        print( f7(14) )
        print( f7(0) )
        print( f7(22) )
        
def f8( str ):
    if len( str ) == 0 or len( str ) == 1:
        return True
    if len(str) > 1:
        if str[0] != str[-1] :
            return False
        return f8( str[1:-1] )

if example_print_flag:
          print( "\n==[8번]==")
          print( f8("") )
          print( f8("kayak") )
          print( f8("penguin") )
          print( f8("a") )

def f9( n ):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f9( n-1 )

if example_print_flag:
        print( "\n==[9번]==")
        print( f9(0) )
        print( f9(1) )
        print( f9(2) )
        print( f9(3) )

def f10( lst ):
    if lst :
        return f10( lst[1:] ) + 1
    else :
        return 0        

if example_print_flag:
        print( "\n==[10번]==")
        print( f10( [1,2,3] ) )
        print( f10( [] ) )
        print( f10( [2] ) )
        
def f11( lst ):
    if len(lst) > 0 :
        if len(lst) == 1:
            return lst[0]
        else:
            return f11(lst[1:])
    else: return ''
    
if example_print_flag:
        print( "\n==[11번]==")
        print( f11([1,2,3]) )
        print( f11([]) )
        print( f11([1]) )
        
def f12(n):
    if n>0 :
        print( n )
        f12( n-1 )

if example_print_flag:
        print( "\n==[12번]==")
        f12( 3 )
        f12( 0 )
        f12( 1 )
        
def f13( n ):
    if n // 10 == 0:
        return 1
    else:
        return f13(n//10) + 1
    
if example_print_flag:
        print( "\n==[13번]==")  
        print( f13(9175) )
        print( f13(34) )
        print( f13(268) )
        print( f13(0) )

def f14( lst ):
    if lst :
        if lst [0] % 2:
            return lst[0]
        return f14( lst[1:] )
    else :
        return ''
    
if example_print_flag:
        print( "\n==[14번]==")  
        print( f14( [1,2,3] ) )
        print( f14( [2,4] ) )
        print( f14( [2,4,6,810,3] ) )

def f15(lst):
    
    #if len(lst) == 0:
    if not lst:  # 리스트가 비어있다면,
        return 0
    
    else:
        if lst[0] % 2 == 1:
            return lst[0] + f15(lst[1:])
        else:
            return 0 + f15(lst[1:])
        
if example_print_flag:
        print( "\n==[15번]==")  
        print( f15( [1,2,3] ) )
        print( f15( [2,4] ) )
        print( f15( [1,3,6,9] ) )

def f16( lst ):
    if lst :
        if lst[0] % 2:
            return [ lst[ 0 ] ] + f16( lst[1:] )
        else:
            return f16( lst[1:] )
    else:
        return []
    
if example_print_flag:
        print( "\n==[16번]==")
        print( f16( [1,3,5,7] ) )
        print( f16( [2,4] ) )
        print( f16( [1,2,3,5] ) )
            
def f17(lst):
    if len(lst) == 2:
        return lst[0]
    else:
        return f17(lst[1:])

if example_print_flag:
        print( "\n==[17번]==")
        print( f17( [1,2] ) )
        print( f17( [1,2,3,4] ) )
        print( f17( [1,2,3] ) )

def f18( a, b ):
    if b > a :
        a, b = b, a
    if a % b :
        return f18( a, a % b )
    else:
        return b
    
if example_print_flag:
        print( "\n==[18번]==")
        print( f18( 5,4 ) )    
        print( f18( 40, 60 ) )
        print( f18( 9, 3 ) )
        
def f19(lst1, lst2):
    if not lst1 or not lst2 :
        if not lst1 :
            return lst2
        if not lst2 :
            return lst1
    else:
        if  lst1[0] < lst2[0] :
            # lst[0] 은 원소 값이 된다.
            # 따라서 리스트 0번째 값을 리스트로 받기 위해
            # lst[0:1] 로 지정해야 한다.
            # 또는 lst[0]의 원소를 포한한 리스트로 표한한다
            # *** [lst[0]] 
            return lst1[0:1] + f19( lst1[1:], lst2 )
        else:
            return [lst2[0]] + f19( lst1, lst2[1:] )

if example_print_flag:
        print( "\n==[19번]==")
        print( f19( [1,2,3], [4,5] ) )
        print( f19( [4,5], [1,2,3] ) )
        print( f19( [], [1,2,3] ) )
        print( f19( [1,2,3], [] ) )
        print( f19( [], [] ) )

def f20( lst ):
    if len(lst ) < 2 :
        return lst
    else:
        half = len(lst) // 2
    return f19( f20( lst[:half] ), f20( lst[half:] ) )

if example_print_flag:
        print( "\n==[20번]==")
        print( f20( [3,2,1] ) )
        print( f20( [] ) )
        print( f20( [5,3,1,2,4,6] ) )
               














    


