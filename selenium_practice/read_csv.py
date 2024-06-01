import csv
import codecs
from itertools import islice

with codecs.open('./data/data.csv','r', 'utf_8_sig') as csv_file:
    data = csv.reader(csv_file)
    users1 = []
    users2 = []
    for line in data:
        users1.append(line)
    print(users1)
    print(type(data))
    csv_file.seek(0)
    for line in islice(data, 1, None):
        users2.append(line)
    print(users2)