class Employee():

    def __init__(self, name, salary, department):
        print("Employee class init function")

        self.name = name
        self.salary = salary
        self.department = department

    def showInfo(self):
        print("Employee's info")

        print("Name : {}\nSalary : {}\nDepartment : {}\n".format(self.name, self.salary, self.department))

    def changeDepartment(self, newDepertment):
        self.department = newDepertment

class Manager(Employee):

# if you dont want to create function you can use pass keyword
#    pass

   def promotion(self, promotion):
       self.salary += promotion


manager = Manager("Robert", 3000, "IT")

manager.showInfo()

manager.changeDepartment("HR")

manager.showInfo()

manager = Manager("Bob", 4000, "DevOps")

manager.promotion(500)

manager.showInfo()