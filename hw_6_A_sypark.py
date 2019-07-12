def f1(n) :
    for line in range(1, n+1):
        st=list(range(1, line+1))
        print(*st)
    print()

def f2(n) :
    for i in range(n):
        st = []
        for j in range(1, i+2):st.append(int(j+(i*(i+1)/2)))
        print(*st)
    print()
    
def f3(n) :
    for i in range(2*n-1):
        if i<n : s_c = i+2
        else : s_c = 2*n-i
        st = []
        for j in range(1, s_c):st.append(int(j+((s_c-2)*(s_c-2+1)/2)))
        print(*st)

def f4(n) :
    for i in range(2*n-1):
        st = []
        if i<n :
            s_c = i+2
            for j in range(1, s_c):st.append(int(j+((s_c-2)*(s_c-2+1)/2)))
        else :
            s_c = 2*n-i
            for j in range(1, s_c):st.append(int(j+ (n**2)-((s_c-1)*(s_c))/2))
        print(*st)

def f5(mat):
    for r in mat :
        sum = 0
        for c in r :
            sum += c
        print(sum)

def f6(mat):
    for r_i in range(len(mat)) :
        for c_i in range(len(mat[r_i])) :
            if r_i == c_i : print(mat[r_i][c_i])

def f7(mat):
    for r in mat :
        sum = 0
        for c in r :
            sum += c
        print(sum)

def f8(mat):
    sum = 0
    for r in mat :
        for c in r :
            sum += c
    return sum

def f9(mat):
    sum = 1
    for r in mat :
        for c in r :
            sum = sum *c
    return sum

def f10(mat):
    for r in mat :
        st = []
        for c in r :
            if c%2 == 1 : st.append(c)
        print(*st)
    print()


def f11(mat1, mat2) :
    for r_i in range(len(mat1)):
        for c_i in range(len(mat1[r_i])):
            mat1[r_i][c_i] += mat2[r_i][c_i]
    return mat1
    

def f12(mat1, mat2) :
    prod_mat = []
    row = len(mat1)
    col = len(mat2[0])
    
    for r_i in range(row):
        prod_mat_sub = []
        for c_i in range(col):
            sum = 0
            for inner in range(len(mat1[r_i])) :
                sum += mat1[r_i][inner]*mat2[inner][c_i]
            prod_mat_sub.append(sum)
        if row==1 and col == 1 : prod_mat.append(prod_mat_sub)
        else : prod_mat.append(prod_mat_sub)
    return prod_mat

def f13(mat):
    for r_i in range(len(mat)) :
        for c_i in range(len(mat[r_i])) :
            if (r_i == c_i and mat[r_i][c_i] != 1) or (r_i != c_i and mat[r_i][c_i] != 0) : return False   
    return True

def f14(row, col):
    x = [1, -1]
    y = [1, -1]
    mat = []
    for r in range(row) :
        mat_sub = []
        for c in range(col) :
            sum = 0
            if r+x[0] >= 0 and r+x[0] <row : sum += 1
            if r+x[1] >= 0 and r+x[1] <row :sum += 1
            if c+y[0] >= 0 and c+y[0] <col :sum += 1
            if c+y[1] >= 0 and c+y[1] <col :sum += 1
            mat_sub.append(sum)
        mat.append(mat_sub)
    return mat
