import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

for record in csvfile:
    print("Employee ID: " + record[0])
    print("First Name: " + record[1])
    print("Last Name: " + record[2])
    print("Salary: " + record[3])
    print("Bonus: " + record[4])
    print("Total Pay: " + str((int(record[3]) + int(record[3])*float(record[4]))))

    input()
