from person import Person

class Teacher(Person):
    def __init__(self, id, last_name, first_name, middle_name, type, position, department):

        super().__init__(id, last_name, first_name, middle_name, type)
        self.position = position
        self.department = department

    def getPosDep(self):
        return (f'{self.position},{self.department}')


# class Load(Teacher):
#     def __init__(self, subject):
#         self.subject = subject
#
#     def getSbu(self):
#         return self.subject