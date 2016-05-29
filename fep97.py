import datetime

class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lasrName = name
        self.birthday = None

    def getName(self):
         """Returns self's full name"""
         return self.name
    
    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthday):
        """Assumes birthday is of type fatetime.days
            Sets self's birthday to birthdate"""
        self.birthday = birthday

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self's name is lexicographically less
            than other's name, and False otherwise"""
        if self.lastName == other.Lastname:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name 

class NIEPerson(Person):

    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = NIEPerson.nextIdNum
        NIEPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(NIEPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        NIEPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass 
