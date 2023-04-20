import sys
from student import Student
from teacher import Teacher
from grade import Grade
from load import Load

students = []
teachers = []

def addStudents():

    while True:

        print()
        print('T = Add Teacher')
        print('S = Add Student')
        print()

        add = input('What you want to add?:')
        add = add.upper()

        print()

        if add == 'S':
            id = input('Enter ID:')
            lastName = input('Enter LastName')
            firstName = input('Enter FirstName')
            middleName = input('MiddleName')
            type = input('Enter Type:')
            course = input('Enter Course:')
            year = input('Enter Year:')
            section = input('Enter Section:')

            print('------------------------------')

            english = int(input('Grade in English'))
            filipino = int(input('Grade in Filipino'))
            math = int(input('Grade in Math'))
            science = int(input('Grade in Science'))

            stud = Grade(filipino, math, science, english)
            stud.id = id
            stud.last_name = lastName
            stud.first_name = firstName
            stud.middle_name = middleName
            stud.type = type
            stud.course = course
            stud.year = year
            stud.section = section

            students.append(stud)

        elif add == 'T':

            id = input('Enter ID:')
            lastName = input('Enter LastName')
            firstName = input('Enter FirstName')
            middleNAme = input('MiddleName')
            type = input('Enter Type:')

            print('--------------------------------')

            position = input('Enter Position')
            department = input('Enter Your Department:')
            subject = input('Enter Subject:')

            tch = Load(subject)
            tch.position = position
            tch.department = department
            tch.id = id
            tch.lastName = lastName
            tch.firstName = firstName
            tch.middleName = middleNAme
            tch.type = type

            teachers.append(tch)

        else:
            menu()

        print()
        ans = input('Enter another? [y/n]')
        ans = ans.lower()

        if (ans !='y'):
            break
        menu()

def deleteRecord():

    print()
    print('T = Delete from Teacher')
    print('S = Delete from Student')
    print('DT = Delete Teachers')
    print('DS = Delete Students')
    print('DA = Delete All')

    delete = input('What do you want to delete?')
    delete = delete.upper()

    menu()

    if delete == 'S':
        i = int(input('Enter Index:'))
        students.pop(i)

    elif delete == 'T':
        i = int(input('Enter Index:'))
        teachers.pop(i)

    elif delete == 'DT':
        teachers.clear()

    elif delete == 'DS':
        students.clear()

    elif delete == 'DA':
        students.clear()
        teachers.clear()

    else:
        deleteRecord()
    menu()

def searchRecord():

    print()
    print('T = Search Teacher:')
    print('S = Search Student:')
    print()

    search = input('Type do you want to search?')
    search = search.upper()

    if search == 'S':

        i = int(input('Enter Index:'))

        print(f'{i} \t | {students[i].getType()} \t | {students[i].getName()} \t | {students[i].getID()} \t | {students[i].getYrCourseSec()} \t |{students[i].getAve()} ')

    elif search == 'T':
        i = int(input('Enter Index:'))
        print(f'{i} \t | {teachers[i].getID} \t | {teachers[i].getName} \t | {teachers[i].getType} \t | {teachers[i].getPosDep} \t | {teachers[i].getSub} \t')

    else:
        searchRecord()
    menu()

def displayRecord():

    print()
    print('T = Display Teacher:')
    print('S = Display Student:')
    print('A = Display All:')
    print()

    display = input('What do you want to display?')
    display = display.upper()

    if display == 'S':
        print()
        print('---------------------------------')
        i = 0
        for s in students:
            print(f'{i} \t | {students[i].getType()} \t | {students[i].getName()} \t | {students[i].getID()} \t | {students[i].getYrCourseSec()} \t |{students[i].getAve()}')
            i += 1
            print('-------------------------------')

    elif display == 'T':
        print()
        print('----------------------------------')

        i = 0
        for t in teachers:
            print(f'{i} \t {teachers[i].getID} \t | {teachers[i].getName} \t | {teachers[i].getType} \t | {teachers[i].getPosDep} \t | {teachers[i].getSub}')
            i += 1
        print('------------------------------')

    elif display == 'A':
        print()
        print('---------------------------------')
        i = 0
        for s in students:
            print(
                f'{i} \t | {s.getType()} \t | {s.getName()} \t | {s.getID()} \t | {s.getYrCourseSec()} \t')
            i += 1
            print('-------------------------------')

            i = 0
        for t in teachers:
            print(
                f'{i} \t {t.getType()} \t | {t.getName()} \t | {t.getID()} \t {t.getPosDep()} \t | {t.getSub()} \t |')
            i += 1
        print('------------------------------')

    else:
        displayRecord()
    menu()


def menu():

    print()
    print()
    print('::Menu::')
    print('D = Delete Record     S = Search Record')
    print('A = Add Record        M = Display All')
    print()

    choice = input('Enter a Function:')
    choice = choice.upper()

    if (choice == 'D'):
        deleteRecord()
    elif (choice == 'A'):
        addStudents()
    elif (choice == 'S'):
        searchRecord()
    elif (choice == 'M'):
        displayRecord()
    else:
        menu()

        print()
menu()




