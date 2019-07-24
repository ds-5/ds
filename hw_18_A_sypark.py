#Advances OOP(1) : Point Class & Pythagoras Class
class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

class Pythagoras :
    def __init__(self):
        self.point_one = Point(None, None)
        self.point_two = Point(None, None)
    
    def setPointOne(self, P) :
        self.point_one.x = P.x
        self.point_one.y = P.y
    
    def setPointTwo(self, P) :
        self.point_two.x = P.x
        self.point_two.y = P.y
    
    def getSlope(self):
        return (self.point_two.y-self.point_one.y)/(self.point_two.x-self.point_one.x)
    
    def getDistance(self):
        return((self.point_two.y-self.point_one.y)**2+(self.point_two.x-self.point_one.x)**2)**0.5


'''
def main():
    PPP = Pythagoras()
    PPP.setPointOne(Point(1,1))
    PPP.setPointTwo(Point(4,5))
    print(PPP.getSlope())
    print(PPP.getDistance())
main()
'''

#dvances OOP(2) : Calculator Class
class Calculator:
    def __init__(self):
        self.result = 0
        self.history = ""
        self.history_final = []
    def add(self, x):
        self.result += x
        if self.history == "": self.history=self.history+str(x)
        else : self.history= self.history+" + "+str(x)
    def subtract(self, x):
        self.result -= x
        self.history=self.history + " - " + str(x)
    def multiply(self, x):
        self.result = self.result*x
        self.history=self.history + " * " + str(x)
    def equals(self, x=False):
        self.result = self.result
        if self.history != "" : self.history_final.append(self.history + " = " + str(self.result))
        if x == True : print(self.result)
        self.result = 0
        self.history = ""
    def show_history(self):
        if self.history_final == [] :
            print("No calculation done yet!")
            print("History:")
        else :
            print("History:")
            for line in self.history_final : print(line)

'''            
def main():
    test = Calculator()
    test.equals()
    test.show_history()

    test.add(2)
    test.subtract(1)
    test.equals()
    test.show_history()

    test.add(2)
    test.multiply(4)
    test.equals(True)

    test.add(10)
    test.subtract(5)
    test.multiply(2)
    test.equals()

    test.show_history()
main()
'''

#Advanced OOP(3) : Account Class
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance-amount
        self.transactions.append(('withdrawal', amount))

    def status(self):
        print(self.holder + ": ", end = "")
        print(self.transactions)
'''
def main():
    b_a = Account("Bob")
    b_a.deposit(1000000)
    b_a.withdrawal(100)
    b_a.deposit(440)
    b_a.status()

    t_a = Account("Tom")
    t_a.deposit(5000000)
    t_a.withdrawal(250)
    t_a.withdrawal(875)
    t_a.status()
main()
'''

#Advanced OOP(4) :
A_to_S = {1:"H", 2:"He", 3:"Li", 4:"Be", 5:"B", 6:"C", 7:"N", 8:"O"}
class atom:
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x, y, z)
    def symbol(self):
        return A_to_S[self.atno]
    def __repr__(self):
        return "%d %10.4f %10.4f %10.4f" %(self.atno, self.position[0], self.position[1], self.position[2])
'''
def main():
    at = atom(6, 0.0, 1.0, 2.0)
    print(at)
    at
    at.symbol()
main()
'''

class molecule:
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self,atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' %self.name
        str = str+'It has %d atoms\n' %len(self.atomlist)
        for atom in self.atomlist:
            str = str + "%s\n" %atom
        return st
'''
def main():
    mol = molecule('Water')
    at = atom(8, 0., 0., 0.)
    mol.addatom(at)
    mol.addatom(atom(1, 0., 0., 1.))
    mol.addatom(atom(1, 0., 1., 0.))
    print(mol)
main()
'''
'''
=> code설명

atom이라는 class는 atno, x, y, z인 input을 받고 atno는 class의 instance변수인 atno에 들어가고 x,y,z는 class의 instance변수인 position에 tuple로 들어간다.
symbol() instance method는 class의 instance변수인 atno값을 키로 하여 Atno_to_Symbol의 dictionary를 통해 해당 value를 return한다.
__repr__()라는 특수 method를 선언하여 이 class안에 구현된 return값(# #.#### #.#### #.####)으로 반환된다. print문을 쓰면 __repr__()을 call한다.

molecule class는 name을 input으로 받을 수 있으나 초기값이 설정되어 있어 아무것도 넣어주지 않았을 때에는 'Generic'으로 들어 간다.
내부 instance value로는 name과 list로 설정된 atomlist가 있다.
addatom(atom) instance method는 atom class를 input variable로 받고 atomlist에 atom.__repr__()에서 return하는 결과가 요소로 append된다.
이 class의 __repr__() 특수 method를 통하여 이 class안에서 만들어지는 str이 return된다.
str은 'This is a molecule named self.name' + 'It has len(self.atomlist) atoms\n' 로 문자열이 생성된 후에 atomlist의 요소 갯수만큼 'atom\n'의 문자열이 더하여 생성된 후 str의 값을 반환한다. 역시 print문은 __repr__()을 call한다.

=> code결과
<atom class>
6 0.0000 1.0000 2.0000
'C'
<molecule class>
This is a molecule named Water
It has 3 atoms
8 0.0000 0.0000 0.0000
1 0.0000 0.0000 1.0000
1 0.0000 1.0000 0.0000

'''



#Advanced OOP(5) : Professor and Student
class Person :
    def __init__(self, N):
        self.Name = N

    def getName(self):
        return self.Name

class Professor(Person) :
    def __init__(self, N, C, S, D):
        super().__init__(N)
        self.Course = C
        self.Salary = S
        self.Depart = D

    def getCourse(self):
        return self.Course

    def getAnnualSalary(self):
        return self.Salary*12

    def raiseSalary(self, percent):
        self.Salary += self.Salary*(percent/100)
        return self.Salary

    def getDepart(self):
        return self.Depart

class Student(Person) :
    def __init__(self, N, Y, C, D):
        super().__init__(N)
        self.Year = Y
        self.Credit = C
        self.Depart = D

    def getCredit(self):
        return self.Credit

    def setCredit(self, cre):
        self.Credit = cre

    def increaseYear(self):
        self.Year += 1

    def getDepart(self):
        return self.Depart

'''def main():
    P1 = Professor("Tim Cook", "Soft Arch", 5500, "CSE")
    print(5*P1.Salary)

    tot = 0
    for i in range(5) :
        tot += P1.raiseSalary(15)
    print(tot)
main()
'''

#Advanced OOP(6) : Staff and Student
class Person:
    def __init__(self, N, A):
        self.name = N
        self.addr = A
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

class Staff(Person):
    def __init__(self, N, A, S, AP):
        super().__init__(N, A)
        self.school = S
        self.annual_pay =AP
    def getSchool(self):
        return self.school
    def getMonthlyPay(self):
        return (self.annual_pay/12)
    def getAnnualPay(self):
        return self.annual_pay
    def raiseAnnualPay(self, per):
        self.annual_pay += self.annual_pay*(per/100)
        return self.annual_pay

class Student(Person):
    def __init__(self, N, A, G, Y, F):
        Person.__init__(self, N, A)
        self.gpa = G
        self.year = Y
        self.fee = F
    def getGpa(self):
        return self.gpa
    def setGpa(self, G):
        self.gpa = G
    def hasMinimumGpa(self):
        if self.gpa > 3.5 : return True
        else : return False
    def willGraduateNextYear(self):
        if self.year == 4 : return True
'''
def main():
    Tom = Staff("Tom", "Gangnam", "Yonsei", 350000)
    Dane = Staff("Dane", "Shindorim", "Sogang", 20000)
    
    for i in range(7):
        Tom.raiseAnnualPay(7)
        Dane.raiseAnnualPay(15)
    
    print(Tom.annual_pay)
    print(Dane.getAnnualPay())
    
    if Tom.getMonthlyPay() > Dane.getMonthlyPay() :
        print("Tom has a larger monthly pay")
    else:
        print("Dane has a larger monthly pay")
main()
'''
