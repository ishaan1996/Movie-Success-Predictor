import csv

'''with open('Final.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = map(tuple, reader)
    print your_list
    '''
my_file=open("Final.csv", "rb")
for line in my_file:
    l = [i.strip() for i in line.split(',')]
    p = l[0].split(' ')
    print p[0]

