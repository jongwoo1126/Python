# 부모 클래스
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

# 자식 클래스 : 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bounus):
        self.pay = base + bounus
        print('총 수령액 : ', format(self.pay, '3,d', '원'))

# 자식 클래스 : 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액 : ', format(self.pay, '3, d', '원'))