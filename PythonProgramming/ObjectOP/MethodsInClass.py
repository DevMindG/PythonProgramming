class SoftwareDeveloper():

    def __init__(self, name, lastName, phone, salary, languages):
        self.name = name
        self.lastName = lastName
        self.phone = phone
        self.salary = salary
        self.languages = languages

    def showInfo(self):
        print("""
        
        Software Developer:
        
        Name: {}
        
        Last Name: {}
        
        Phone: {}
        
        Salary: {}
        
        Languages: {}
        
        """.format(self.name, self.lastName, self.phone, self.salary, self.languages))



    def promotionDev(self, promotion):
            print("Developer will get promotion")
            self.salary += promotion

    def addLang(self, newLang):
            print("Languages is added")
            self.languages.append(newLang)

developer = SoftwareDeveloper("Bob", "Larry", "2019176534", 3500, ["Python", "Java", "HTML"])
developer.showInfo()

developer.addLang("GoLang")

developer.showInfo()
