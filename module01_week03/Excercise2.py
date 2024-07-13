class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_person = []

    def add_person(self, person):
        self.__list_person.append(person)
    
    def describe(self):
        print(self.__name)
        for person in self.__list_person:
            person.describe()
    
    def count_doctor(self):
        count = 0
        for person in self.__list_person:
            if(isinstance(person,Doctor)):
                count += 1
        return count
    
    def sort_age(self):
        self.__list_person.sort(key = lambda person: person._yob)

    def compute_average(self):
        result = 0
        count = 0
        for person in self.__list_person:
            if(isinstance(person, Teacher)):
                result += person._yob
                count += 1
        return result / count 
    
class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
    
    def get_yob(self):
        return self._yob
    
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name,yob)
        self.__grade = grade
    
    def describe(self):
        print(f'Student - Name : {self._name} - YoB : {self._yob} - Grade : {self.__grade}')
    
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name,yob)
        self.__specialist = specialist
    
    def describe(self):
        print(f'Doctor - Name : {self._name} - YoB : {self._yob} - Specialist : {self.__specialist}')
    
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name,yob)
        self.__subject = subject
    
    def describe(self):
        print(f'Teacher - Name : {self._name} - YoB : {self._yob} - Subject : {self.__subject}')

student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward ( name ="Ward1")
ward1.add_person ( student1 )
ward1.add_person ( teacher1 )
ward1.add_person ( teacher2 )
ward1.add_person ( doctor1 )
ward1.add_person ( doctor2 )
ward1.describe()

print ( f"Number of doctors : { ward1 . count_doctor ()}")

print ("After sorting Age of Ward1 people ")
ward1 . sort_age ()
ward1 . describe ()

print ( f"Average year of birth ( teachers ): { ward1 . compute_average ()}")