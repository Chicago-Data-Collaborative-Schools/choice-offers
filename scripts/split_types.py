import csv
import sys

reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(sys.stdout, ['OfferStatus', 'Choice', 'Type', 'level', 'year', 'masked_ID'])

writer.writeheader()

for row in reader:
    raw_type = row['Type']
    if 'High School' in raw_type:
        row['level'] = 'High School'
        row['Type'] = raw_type.removesuffix(' High School')
    else:
        row['level'] = 'Elementary'
        row['Type'] = raw_type.removesuffix(' Elementary')

    writer.writerow(row)
