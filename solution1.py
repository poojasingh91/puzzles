# From Pooja Singh

import csv
file = open("csv-sample.csv")
data = csv.reader(file) 
lines= len(list(data))

print("The count of lines becomes: ", lines)
