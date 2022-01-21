#클래스의 상속
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name : %s, age : %d' % (self.name, self. age))

sup = Super('부모', 55)
sup.display()

class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print('name : %s, age : %d, gender : %s' % (self.name, self.age, self.gender))

sub = Sub('자식', 25, '여자')
sub.display()

#Super 클래스
class Parent:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

p = Parent('홍길동', '회사원')
p.display()

class Children(Parent):
    gender = None

    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender

    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))

chil = Children('이순신', '해군 장군', '남자')
chil.display()

