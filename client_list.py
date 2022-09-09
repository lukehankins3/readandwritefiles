def main():
    file = open('clients.txt')
    n=1
    for line in file:
        print(str(n) + '. ' + line.rstrip())
        n = n + 1

main()