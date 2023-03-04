# using_csv.py

import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
            line_count +=1
    print(f'Processed {line_count - 1} lines.')


"""
In C (and many other languages), you can insert hard-to-see/type characters using \ notation:

    \a is alert/bell
    \b is backspace/rubout
    \n is newline
    \r is carriage return (return to left margin)
    \t is tab
"""

