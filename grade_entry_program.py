def main():

    line = []
    student_grades = []
    count = int(input("How many students do you need to "
                      "enter grades for? "))
    for student in range(0, count):
        student_name = input("Enter students name: ")
        grade = input("Enter students final letter grade: ")
        line.append(student_name)
        line.append(grade)
        student_grades.append(line)
        line = []
    print(student_grades)

    outfile = open("grades.txt", "w")
    for line in student_grades:
        lineout = "'" + line[0] + "','" + line[1] + "'/n"
        outfile.writelines(lineout)
    outfile.close()

main()
