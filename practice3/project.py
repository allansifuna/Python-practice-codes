class employees:
    def rep(self,name,age,salary,incre):
        self.name = name
        self.age = age
        self.salary = salary
        self.incre = incre
        print('{}   {}   ${}'.format(self.name,self.age,self.salary*self.incre))
f= open("files.txt","r")
v=f.readlines()
for i in range(len(v)):

     name,age,salary=v[i].split(" ")
     age=int(age,10)
     salary=int(salary,10)
     if name=='Hilda':
         incre=4
     else:
        incre=1
     employee=employees()
     employee.rep(name,age,salary,incre)



