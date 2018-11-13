# class Students:
#     name="Arjun"
#     rollno=22
#
#     def getAge(self,myAge):
#         print("Age is "+str(myAge))
# s=Students()
# x=int(input("Enter the Age "))
# print(s.getAge(x))


class Students:

    def __init__(self,x,y):     #__init__ is a special character
        self.name=x
        self.rollno=y

    def printData(self):
        print("Name= "+str(self.name))
        print("RollNo= "+str(self.rollno))

    def getAge(self,myAge):
        print("Age is "+str(myAge))

s=Students("Arjun S",22)

x=int(input("Enter the Age "))

s.printData()
s.getAge(x)
