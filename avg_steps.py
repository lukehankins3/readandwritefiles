import csv
import calendar

infile = open('steps.csv','r')

csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

outfile = open('avg_steps.csv','w', newline = '')
writer = csv.writer(outfile, delimiter = ',')
header = ['Month', 'Avg Steps in Month']
writer.writerow(header)

steps = 0
current_month = 1
day = 0

for record in csvfile:
    if int(record[0]) == current_month:
        day += 1
        steps += int(record[1])
    else:
        average = round((steps / day), 2)
        month_name = calendar.month_name[int(record[0])]
        data = [month_name , average]
        writer.writerow(data)
        current_month = int(record[0])
        steps = int(record[1])
        day = 1



outfile.close()
