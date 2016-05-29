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

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: studenmt is of type Student
            Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrades(self, student, grade):
        """Assumes: grade is a float
            Add grade to the list of grades for students"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mappling')
        def getGrades(self,student):
            """return a list of grades for student"""
            try:#return copy of student's grades
                return self.grades[student.getIdNum()][:]
            except:
                raise ValueError('student not in mapping')

        def getStudents(self):
            """return a list of students in the grade book"""
            if not self.isSorted:
                  self.students.sort()
                  self.isSorted = True
                  return self.students[:]#return copy of list of students
