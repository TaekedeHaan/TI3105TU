#Initialize progrom
courses_string = ""
students = []
courses = ['english', 'math','history']
grades_english = {}.fromkeys(students,) #Create a dict
grades_math = {}.fromkeys(students,)
grades_history = {}.fromkeys(students,)

#Combine al grades in another dictionary
grades = {courses[0] : grades_english , courses[1] : grades_math, courses[2] : grades_history}

continueFlag = 1
courses_amount = len(courses)

#We want to transform the list containing the cources into a proper string so it can be printed.
for i in range(courses_amount):
    courses_string += courses[i].capitalize()
    if  i < (courses_amount - 2):
        courses_string += ", "
    elif i == (courses_amount - 2):
        courses_string += " and "


while continueFlag:

    #Ask for name
    name = input("What is the student's name? ")

    #Ask for course and determine whether it exists
    chooseCourse = 1
    while chooseCourse:
        course = input("What is the course? Choose from: {} ".format(courses_string))
        if (course in str(courses)):
            chooseCourse = 0
        else :
            print("{} is not an available course, please select another one".format(course))
            chooseCourse = 1

    grade = input("What was his/her grade? ")

    saveInput = 0
    while saveInput == 0:
        saveInput = input("Is it true that {0} had an {1} for {2}".format(name, grade, course, format_spec='{2}'))

    #Save input
    for i in range(courses_amount):
        if course == courses[i]:
            grades[courses[i]][name] = grade


    print(grades)
    students.append(name)

    continueInput = input("Do you want to continue? (Y/N)")
    if continueInput == 'Y' or continueInput == 'y':
       continueFlag = 1
    else:
       continueFlag = 0