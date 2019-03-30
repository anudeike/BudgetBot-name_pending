import csv
import random


def Purchases():
    for x in range(600):
        transP = random.randint(5, 50)
        entertainP = random.randint(15, 100)
        grocP = random.randint(50, 100)

        T = 1
        E = 2
        G = 3
        
        emphasis = random.choice([T, E, G])
        chance = random.randint(0, 100)

        if emphasis == T:
            if chance < 25:
                filewriter.writerow(['','','',grocP])
            if chance >= 25 and chance > 50:
                filewriter.writerow(['','',entertainP,''])
            if chance >= 50:
                filewriter.writerow(['',transP,'','']) #emphasis
                
        if emphasis == E:
            if chance < 25:
                filewriter.writerow(['','','',grocP])
            if chance >= 25 and chance > 50:
                filewriter.writerow(['',transP,'',''])
            if chance >= 50:
                filewriter.writerow(['',entertainP,'']) #emphasis
                
        if emphasis == G:
            if chance < 25:
                filewriter.writerow([transP,'',''])
            if chance >= 25 and chance > 50:
                filewriter.writerow(['',entertainP,''])
            if chance >= 50:
                filewriter.writerow(['','',grocP]) #emphasis


with open('Person1.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Transportation','Entertainment','Groceries'])
    Purchases()

with open('Person2.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Transportation','Entertainment','Groceries'])

    Purchases()

with open('Person3.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Transportation','Entertainment','Groceries'])
    Purchases()

