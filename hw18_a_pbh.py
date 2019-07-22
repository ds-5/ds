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

    def __init__(self, name):
        self.name = name
        self.transaction = []
        self.deposit_value = 0

    def deposit(self, value):
        self.deposit_value = value
        self.transaction_log('deposit', value)

    def transaction_log(self, keyword, value):
        self.transaction.append((keyword, value))

# 18-A-5. Professor and Student
'''
year 에 3(rd) 2(nd) 필요 없음. rd, nd...
'''
class Person:
    pass

class Student(Person):
    def __init__(self, name, depart, year, credit):
        super().__init__(name)
        self.depart = depart
        self.year = year
        self.credit = credit

    def setDepart(self, depart):
        self.depart = depart

    def getDepart(self):
        return self.depart

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year

    def setCredit(self, credit):
        self.credit = credit

    def getCredit(self):
        return self.credit

    def IncreseYear(self):
        self.year += 1

class Professor(Person):
    def __init__(self, name, course, depart, salary):
        super().__init__(name)
        self.course = course
        self.depart = depart
        self.salary = salary

    def setCourse(self, course):
        pass
    def getCourse(self):
        pass
    def setDepart(self, depart):
        pass
    def getDepart(self):
        pass
    def setSalary(self, salary):
        pass





