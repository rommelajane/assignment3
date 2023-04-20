from person import Person

class Student(Person):

    def __init__(self, id, last_name, first_name, middle_name, type, section, year, course):
        super().__init__(id, last_name, first_name, middle_name, type)
        self.section = section
        self.year = year
        self.course = course

    def getYrCourseSec(self):
        return (f'{self.section}/{self.year}/{self.course}')


# class Grade(Student):
#
#     def __init__(self, english, filipino, math, science):
#
#         self.english = english
#         self.filipino = filipino
#         self.math =math
#         self.science = science
#
#     def getAve(self):
#         sum = self.english + self.filipino + self.math + self.science
#
#         return sum / 4