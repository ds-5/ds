#17-4 Simple OOP Practice

#(1) : Animal and Dog

class Animal:
    def __init__( self ):
        print( 'Animal created' )
    def whoAmI( self ):
        print( 'Animal' )
    def eat( self ):
        print( 'Eating' )

class Dog( Animal ):
    def __init__( self ):
        super().__init__()
        print( 'Dog created' )
    def whoAmI( self ):
        print( 'Dog' )
    def bark( self ):
        print( 'Woof!' )

d = Dog()
d.whoAmI()
d.eat()
d.bark()

#정답
'''
   1. 부모 클래스 Animal 를 자식 클래스 Dog 이 상속 받음.
   2. Dog 클래스를 기반으로 d 인스턴스 객체 만듬.
   3. d 인스턴스 객체는 만들어지는 시점에 super 클래스(Animal 클래스)의 생성자를 실행함.
   4. d 인스턴스 객체 생성 후  whoAmI, eat, bark 멤버 함수를 실행함.
       . whoAmI, bark 멤버 함수는 Dog 클래스 멤버 함수를 실행.
       . eat 멤버 함수는 Animal 부모 클래스 멤버 함수를 실행.
'''

#(2) : Circle

class Circle():
    def __init__( self ):
        self.pi = 3.141592
        self.r = 0
    def area( self ):
        return self.pi * self.r * self.r
    def getRadius( self ):
        return self.r
    def setRadius( self, rad ):
        self.r = rad

c = Circle()
c.setRadius(5)
print( c.getRadius() )
print( c.area() )

# 정답
# 5
# 78.5398

#(3) : Shape and Others

class Shape:
    def __init__( self, x, y ):
        self.x = x
        self.y = y
        self.description = 'This shape has not been described yet'
        self.author = 'Nobody has claimed to make this shape yet'
    def area( self ):
        return self.x * self.y
    def perimeter( self ):
        return 2 * self.x + 2 * self.y
    def describe( self, text ):
        self.description = text
    def authorName( self, text ):
        self.author = text
    def scaleSize(self, scale):
        self.x = self.y * scale
        self.y = self.y * scale

#정답
'''
    1. Shape 클래스는 생성시, Shape 길이 x, y 멤버 변수를 가지고 있음.
    2. area 멤버 함수는Shape 면적 값을 리턴함. ( x, y 멤버 변수의 곱 )
    3. perimeter 멤버 함수는 Shape 테두리 길이 값을 리턴함
    4. describe, authorName 함수는 description, author 멤버 변수의 값을 변경시킴.
    5. scaleSize 멤버 함수는 주어진 scale argument를 이용해 x, y 멤버 변수 값을 변경 시킴.
'''

#(3) : Shape and Others [1/3]

rectangle = Shape( 100, 45 )
print( rectangle.area() )
print( rectangle.perimeter() )
rectangle.describe( "A wide rectangle, more than twice as wide as it is tall")
rectangle.scaleSize(0.5)
print( rectangle.area() )

# 정답
# 4500
# 290
# 506.25

#(3) : Shape and Others [2/3]

# 정답
# Squre 클래스는 한 변의 길이를 입력받아 해당 길이의 정사각형을 만든다.
class Square(Shape) :
    def __init__(self, x=0):      
        super().__init__(x, x)

c = Square( 10 )
print( c.area() )
print( c.perimeter() )

# Double 클래는 한 변의 길이를 입력 받아
# 해당 길이의 2배의 가로, 해당 길이의 세로를 가지는 직사각형을 만든다. 
class DoubleSquare(Shape):
    def __init__(self, x=0):
        super().__init__( 2 * x, x )

c = DoubleSquare( 10 )
print( c.area() )
print( c.perimeter() )
        
#(3) : Shape and Others [3/3]
# 정답
# InsideDoubleSquare 클래스는 한 변의 길이를 입력받아 해당 길이의 정사각형을 만든 후
# 내부에 1/4 면적을 가지는 정사각형을 만든다.

class InsideDoubleSquare(Square):
    def __init__( self, x = 0 ):
        self.outterSqure = Square( x  )
        self.innerSqure = Square( x / 2 )

c = InsideDoubleSquare(20)
print( c.outterSqure.area() )
print( c.innerSqure.area() )



