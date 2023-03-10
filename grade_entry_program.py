n = int(input('How many students do you need to enter grades for? '))
student_grades = []
for i in range(n):
    name = input(f'Enter the name of student {i+1}: ')
    grade = input('Enter the student\'s final letter grade: ')
    student_grades.append([name, grade])
outfile = open('grades.txt', 'w')
for line in student_grades:
    lineout = '\'' + line[0] + '\', \'' + line[1] + '\'\n'
    outfile.write(lineout)
    
outfile.close()
