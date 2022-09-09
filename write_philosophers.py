def main():

    myfile = open('philosophers.txt','w')
    myfile.write('John Locke' + '\n')
    myfile.write('David Hume' + '\n')
    myfile.write('Edmund Burke' + '\n')

    myfile.close()


main()
