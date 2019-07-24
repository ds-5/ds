#(1) Parenthesis Matching using Python
#(Version 1) Using Stack class

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, a):
        self.stack.append(a)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        if self.stack == [] : return True
        else : return False
    def peek(self):
        return self.stack[-1]
    
def main(pare):
    myS = Stack()
    mat_list = []
    mis_mat = []

    for i in range(len(pare)):
        if pare[i] == "(" : myS.push(i)
        elif pare[i] == ")" :
            if myS.isEmpty() : mis_mat.append(i)
            else : mat_list.append((myS.pop(), i))

    if mat_list != []:
        print("Output : ", end = "")
        for mat in mat_list :
            if mat == mat_list[-1] : print(mat, end = " ")
            else : print(mat, end = ", ")
        print("match")

    mis_mat += myS.stack

    if mis_mat != [] :
        print("Output : ", end = "")
        for mat in mis_mat :
            if mat == mis_mat[-1] : print(mat, end = " ")
            else : print(mat, end = ", ")
        print("have no matching parentheses")

'''
main("(a*(b+c)+d)")
main("(b+c))(")
'''
#(Version 2) Using Queue module

import queue

def main(pare):
    myS = queue.LifoQueue()
    mat_list = []
    mis_mat = []

    for i in range(len(pare)):
        if pare[i] == "(" : myS.put(i)
        elif pare[i] == ")" :
            if myS.empty() : mis_mat.append(i)
            else : mat_list.append((myS.get(), i))

    if mat_list != []:
        print("Output : ", end = "")
        for mat in mat_list :
            if mat == mat_list[-1] : print(mat, end = " ")
            else : print(mat, end = ", ")
        print("match")


    while myS.qsize() > 0 : mis_mat.append(myS.get())

    if mis_mat != [] :
        print("Output : ", end = "")
        for mat in mis_mat :
            if mat == mis_mat[-1] : print(mat, end = " ")
            else : print(mat, end = ", ")
        print("have no matching parentheses")
        
'''
main("(a*(b+c)+d)")
main("(b+c))(")
'''

#(2)Tower of Hanoi using Python
def towerofHanoi(n,x,y,z):
    if (n>0):
        towerofHanoi(n-1,x,z,y)
        print("Move the top Dish from tower "+x+" to top of tower " +y)
        towerofHanoi(n-1,z,y,x)

towerofHanoi(4,"x","y","z")
