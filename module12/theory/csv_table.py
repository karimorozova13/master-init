import csv


with open('table.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked beans'])
    spam_writer.writerow(['Spam', 'Lovely spam', 'Amazing spam', 'Spam is wonderful'])
    
with open('table.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    print(spam_reader)
    for row in spam_reader:
        print(', '.join(row))
        
with open('eggs.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    csv_dict = csv.DictWriter(fh, fieldnames=field_names)
    csv_dict.writeheader()
    csv_dict.writerow({'first_name': 'Kari', 'last_name': 'Mo'})
    csv_dict.writerow({'first_name': 'Platon', 'last_name': 'Mo'})
    csv_dict.writerow({'first_name': 'Iana', 'last_name': 'Lenser'})
    
with open('eggs.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(f"{row['first_name']} {row['last_name']}")
    