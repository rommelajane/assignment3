from student import Student

class Grade(Student):

    def __init__(self, english, filipino, math, science):

        self.english = english
        self.filipino = filipino
        self.math = math
        self.science = science

    def getAve(self):
        return (int(self.filipino) + int(self.math) + int(self.science) + int(self.english)) / 4
        # sum = self.english + self.filipino + self.math + self.science
        #
        # return sum / 4