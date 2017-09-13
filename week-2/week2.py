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
        course = course.lower() #Convert to lower case to make case insensitive
        if (course in str(courses)):
            chooseCourse = 0
        else :
            print("{} is not an available course, please select another one".format(course))
            chooseCourse = 1

    grade = input("What was his/her grade? ")

    #Allow the user to check wether it's input was coorect
    saveInputString = input("Is it true that {0} had an {1} for {2}? [Y/N]".format(name, grade, course, format_spec='{2}'))
    saveInputString = saveInputString.lower() #Convert to lower case to make case insensitive
    if saveInputString == 'y':
        saveInput = True
    elif saveInputString == 'n':
        saveInput = False
    elif saveInputString == 'n':
        saveInput = False

    #Save input if desired
    if saveInput:
        for i in range(courses_amount):
            if course == courses[i]:
                grades[courses[i]][name] = grade
                students.append(name)

    #Display the grades which have been inserted in a nice way
    for courseName in grades:
        print(courseName)
        for student in grades[courseName]:
            print('-',student, ':', grades[courseName][student])

    #Ask the user if he/she want to continue and set flag acordingly
    continueInput = input("Do you want to continue? (Y/N)")
    if continueInput == 'Y' or continueInput == 'y':
       continueFlag = 1
    else:
       continueFlag = 0