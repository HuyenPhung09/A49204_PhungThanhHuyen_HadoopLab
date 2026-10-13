import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if len(row) < 10:
        continue
    if row[0] == "transaction_id":
        continue
    if row[9] == "SUCCESS":
        category = row[4]
        amount = int(row[8])
        print(f"{category}\t{amount}")
#viết lại Mapper
