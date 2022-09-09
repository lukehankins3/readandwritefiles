import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

outfile = open('customer_country.csv','w')
next(csvfile)
writer = csv.writer(outfile)
header = ['Full Name', 'Country']
writer.writerow(header)
count = 0

for record in csvfile:
    First_Name = record[1]
    Last_Name = record[2]
    Country = record[4]
    data = [
        [First_Name + ' ' + Last_Name , Country]
    ]
    writer.writerows(data)
    count = count + 1

print(count)
outfile.close()