class Employee:
    def __init__ (self,w,x,y,z):
        self.code=w
        self.name=x
        self.age=y
        self.salary=z

    def initialData(self):
        print("Code is "+str(self.code))
        print("Name is "+str(self.name))
        print("Age is "+str(self.age))
        print("Salary is "+str(self.salary))

    def printCode(self, code):
        print("Code is "+str(code))

    def printName(self, name):
        print("Code is "+str(self.name))

    def printAge(self, age):
        print("Code is "+str(self.age))

    def printSalary(self, salary):
        print("Code is "+str(self.salary))

e=Employee(122,"Arjun",24,24763)

w=int(input("Enter the code: "))
x=input("Enter the name: ")
y=int(input("Enter the age: "))
z=int(input("Enter the salary: "))

e.printCode(w)
e.printName(x)
e.printAge(y)
e.printSalary(z)
