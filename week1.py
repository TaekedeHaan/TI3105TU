students = []
courses = ['English', 'Math','History']
continueFlag = 1

grades_english = {}.fromkeys(students,) #Create a dict
grades_math = {}.fromkeys(students,)
grades_history = {}.fromkeys(students,)

grades = {courses[0] : grades_english , courses[1] : grades_math, courses[2] : grades_history}

while continueFlag == 1:
   name = input("What is the student's name?")
   course = input("What is the subject? Choose from: {}".format(courses))
   grade = input("What was his/her grade? :")


   if course == courses[0]:
       grades[courses[0]][name] = grade
   elif course ==courses[1]:
       grades[courses[1]][name] = grade
   elif course == courses[2]:
       grades[courses[2]][name] = grade
   else:
       print("Something went wrong")

   print(grades)
   students.append(name)

   continueInput = input("Do you want to continue? (Y/N)")
   if continueInput == 'Y' or continueInput == 'y':
       continueFlag = 1
   else:
       continueFlag = 0