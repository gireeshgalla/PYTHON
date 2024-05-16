'''
class Test:
    
    org_name="TCS"
    
    def __init__(self):
        pass
    def m1(self):
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m2():
        pass

t1=Test()

t2=Test()

print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)
'''

'''
class Employee:
    pass


e1=Employee()
e2=Employee()

print(Employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
'''



class Employee:
    org_name="TCS"

    def __init__(self):
        Employee.loc ="Bangalore"

    def m1(self):
        Employee.country="India"
    @classmethod
    def m2(cls):
        Employee.cc = 91
        cls.pincode = 560032
    @staticmethod
    def m3():
        Employee.avail=True


Employee.discount=10

e1=Employee()
e1.m1()
e1.m2()
e1.m3()

print(EMployee.__dict__)
print(e1.__dict__)

e2=Employee()
print(e2.__dict__)



