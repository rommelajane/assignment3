from teacher import Teacher

class Load(Teacher):
    def __init__(self, subject):
        self.subject = subject

    def getSub(self):
        return self.subject