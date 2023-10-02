import csv
#import csv_tracemalloc

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='-')

    with open("new_user.csv", 'w') as csv_new_file:
        csv_writer = csv.writer(csv_new_file)

        for line in csv_reader:
            csv_writer.writerow(line)
