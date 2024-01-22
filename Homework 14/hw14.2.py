import csv

with open('names.csv', 'r') as csv_file:
    with open('names.txt', 'w') as txt_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            txt_file.write(','.join(row) + '\n')

print("Data copied from names.csv to names.txt.")