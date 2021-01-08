import csv
from urllib.parse import unquote
from collections import Counter

#with open('log.csv') as csvfile:
#    print('flag:')
#    [print(unquote(row[1]), unquote(row[3])) for row in csv.reader(csvfile, delimiter=';') if b'%E2%80%8B' in row[1].encode()]
    
with open('luke_5_log.csv') as csvfile:
    name_counts = Counter([(row[1]) for row in csv.reader(csvfile, delimiter=';')])
    
    print('unique name:', name_counts.most_common()[-1:][0][0].encode() )
        #, unquote(row[3]).split('PST')[0])

with open('luke_5_log.csv') as csvfile:
    print([[unquote(item) for item in row] for row in csv.reader(csvfile, delimiter=';') if "%E2%80%8B" in row[1] ])

