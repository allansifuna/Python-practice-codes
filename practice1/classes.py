class students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get(self):
        print("My name is %s and am %d years old and got a %s grade\n"%(self.name,self.age,self.grade))
class teachers(students):
    def __init__(self,name,age,grade,salary):
        super().__init__(name,age,grade)
        self.salary= salary
    def get(self):
        print("My name is %s and am %d years old and earning %d per month\n"%(self.name,self.age,self.salary))
allan=teachers("Allan",18,"A-",200000)
cornelius=students("Cornelius",20,"B+")
allan.get()
cornelius.get()