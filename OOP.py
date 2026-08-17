class student:
    name="chandu"
    def detail(self):
        print(f"my name is {self.name}")
obj=student()
obj.detail()

#USINF __INIT__

class student:
    def __init__(self,name,course,section, rollnumber,):
        self.name = name
        self.course = course
        self.section = section
        self.rollnumber = rollnumber
    def detail(self):
        print(f"student : {self.name}\n{self.course}\n{self.section}\n{self.rollnumber}")
    def detail2(self,passingyear):
        print(f"passingyear{passingyear}")
obj= student ("chandu","mca","B",2222)
obj.detail()
obj.detail2(2025)


# CALCULATOR

class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        print(self.a / self.b)                            
obj = calculator(20,2)
obj.add()
obj.sub()
obj.mul()
obj.div()