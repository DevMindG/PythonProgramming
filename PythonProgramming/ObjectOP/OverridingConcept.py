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

    def __init__(self, name, salary, department, numOfPeople):
        print("Manager class init function")

        self.name = name
        self.salary = salary
        self.department = department
        self.numOfPeople = numOfPeople

    # if you dont want to create function you can use pass keyword
    #    pass

    def showInfo(self):
        print("Employee's info")

        print("Name : {}\nSalary : {}\nDepartment : {}\nNumber of People : {}\n".format(self.name,
                                                                                        self.salary,
                                                                                        self.department,
                                                                                        self.numOfPeople))

    def promotion(self, promotion):
        self.salary += promotion

manager = Manager("Jack", 5000, "IT", 10)

manager.showInfo()

