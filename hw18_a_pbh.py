# 18-A-1
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pythagoras():
    def __init__(self, x1, y1, x2, y2):
        self.point_one = Point(x1, y1)
        self.point_two = Point(x2, y2)

    def setPointOne(self, p):
        self.point_one = p

    def setPointTwo(self, p):
        self.point_one = p

    def getSlope(self):
        return (self.point_two.y - self.point_one.y) / (self.point_two.x - self.point_one.x)

    def getDistance(self):
        return ((self.point_two.x - self.point_one.x)**2 + (self.point_two.y - self.point_one.y)**2)**0.5

'''
# TEST
p1 = Pythagoras(1,1,2,2)
print(p1.getSlope())
print(p1.getDistance())
p1.setPointTwo(Point(-1,-1))
print(p1.getSlope())
print(p1.getDistance())
'''

#18-A-2. Calculator Class
class Calculator():

    def __init__(self):
        self.result = 0
        self.equation = ''
        self.history = []

    def add(self, i):
        if self.result :
            self.equation += ' + ' + str(i)
        else :
            self.equation += str(i)
        self.result += i

    def subtract(self, i):
        if self.result:
            self.equation += ' - ' + str(i)
        else:
            self.equation += '- ' + str(i)
        self.result -= i

    def multiply(self, i):
        if self.result :
            self.equation += ' * ' + str(i)
        else :
            self.equation += str(i)
        self.result *= i

    def equals(self, b=False):
        if self.equation:
            self.equation += ' = ' + str(self.result)
            if b:
                print(self.result)
            self.history.append(self.equation)
            self.equation = ''
            self.result = 0

    def show_history(self):
        if not self.history:
            print('No Calculation done yet!')
        print('History:')
        if self.history:
            for line in self.history:
                print(line)

'''
# TEST
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
'''

# 18-A-3. Account Class
class Account :

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        self.transactions.append(('withdrwal', amount))
        return self.balance

    def status(self):
        print(self.holder + ': ', end='')
        print(self.transactions)

'''
# TEST
bob_account = Account('Bob')
bob_account.deposit(1000000)
bob_account.withdrawal(100)
bob_account.deposit(440)
bob_account.status()

tom_account = Account('Tom')
tom_account.deposit(5000000)
tom_account.withdrawal(250)
tom_account.withdrawal(875)
tom_account.status()
'''

# 18-A-4. Atom and Molecule
Atno_to_Symbol = {1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O'}

class atom(object):
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.position = (x,y,z)
    def symbol(self):
        return Atno_to_Symbol[self.atno]
    def __repr__(self):
        return '%d %10.4f %10.4f %10.4f' % (self.atno, self.position[0], self.position[1], self.position[2])

class molecule:
    def __init__(self, name='Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' % (self.name)
        str = str+'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            str = str + " %s \n" % atom
        return str
'''
<설명>
atom 클래스는 생성자를 통하여 원자번호와 x,y,z 를 받음.
symbol 메소드 호출시, 미리 정의된 Atno_to_Symbol 의 원자번호에 맞는 기호 반환.
class 호출 시, __repr__ 메소드를 통해 원자번호와 x,y,z 를 포맷에 맞게 리턴.

molecule 클래스는 생성자를 통하여
    분자이름을 입력받거나, 입력되지 않는 경우 'Generic' 으로 초기화하고, atomlist 를 빈 list로 초기화.
addatom 메소드는 atomlist 에 입력받은 atom 클래스를 추가.
molecule 호출 시, __repr__ 메소드에 의해서,
    분자이름 을 출력하고, atomlist 에 존재하는 클래스들의 리턴 값 (atom 클래스 내의 __repr__) 을
    순차적으로 결합하여 리턴한다.

<결과>
>>> at = atom(6, 0.0, 1.0, 2.0)
>> print(at)
6     0.0000     1.0000     2.0000
>>> at.symbol()
'C'
>>> mol = molecule('Water')
>>> at = atom(8, 0., 0., 0.)
>>> mol.addatom(at)
>>> mol.addatom(atom(1,0.,0.,1.))
>>> mol.addatom(atom(1,0.,1.,0.))
>>> print(mol)
#This is a molecule named Water
#It has 3 atoms
# 8     0.0000     0.0000     0.0000
# 1     0.0000     0.0000     1.0000
# 1     0.0000     1.0000     0.0000
'''

# 18-A-5. Professor and Student
class Person:
    def __init__(self, name, depart):
        self.name = name
        self.depart = depart
    def getName(self):
        return self.getName
    def getDepart(self):
        return self.getDepart

class Student(Person):
    def __init__(self, name, depart, year, credit):
        super().__init__(name, depart)
        self.year = year
        self.credit = credit
    def getCredit(self):
        return self.credit
    def setCredit(self, credit):
        self.credit = credit
    def increaseYear(self):
        self.year += 1

class Professor(Person):
    def __init__(self, name, course, depart, salary):
        super().__init__(name, depart)
        self.course = course
        self.salary = salary
    def getCourse(self):
        return self.course
    def getAnnualSalary(self):
        return self.salary * 12
    def get_5month_salary(self):
        return self.salary * 5
    def get_5year_salary(self):
        salary = 0
        for i in range(1,6):
            salary += self.salary * (1.15 ** i)
        return salary

# TEST
tim_cook = Professor('Tim Cook', 'Soft Arch.', 'CSE', 5500)
print('5 year salary:', tim_cook.get_5month_salary())
print('5 year salary 15% raise:', tim_cook.get_5year_salary())

# 18-A-6. Staff and Student
class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
class Staff(Person):
    def __init__(self, name, address, school, annual_pay):
        super().__init__(name, address)
        self.school = school
        self.annual_pay = annual_pay
    def getSchool(self):
        return self.school
    def getMonthlyPay(self):
        return self.annual_pay / 12
    def raiseAnnualPay(self, percent):
        self.annual_pay += self.annual_pay * (percent/100)
class Student(Person):
    def __init__(self, name, address, gpa, year, fee):
        super().__init__(name, address)
        self.gpa = gpa
        self.year = year
        self.fee = fee
    def getGpa(self):
        return self.gpa
    def setGpa(self, gpa):
        self.gpa = gpa
    def hasMinimumGpa(self):
        if self.gpa >= 3.5:
            return True
        return False
    def willGraduateNextYear(self):
        if self.year == 4:
            return True
        return False

# TEST
tom = Staff('Tom', 'Gangnam', 'Yonsei', 35000)
dane = Staff('Dane', 'Shindorim', 'Sogang', 20000)
# The seven year:
for i in range(7):
    tom.raiseAnnualPay(7)
    dane.raiseAnnualPay(15)
if tom.annual_pay > dane.annual_pay:
    print("Tom has a larger monthly pay")
else:
    print("dane has a larger monthly pay")
