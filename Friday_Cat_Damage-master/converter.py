import csv

# SIC code stands for Standard Industrial Identification code.
# Each six-digit SIC code corresponds to a business type, or SIC code name.
# (ex. SIC code 581203 corresponds to SIC code name Ice Cream Parlours)

# this function gets a SIC code name and returns the corresponding SIC code


def get_sic_code(sic_code_name):
    with open('static/sic_codes.csv') as csv_file:
        # delimiter in this csv is the tab character, or ASCII character 9
        tab = chr(9)
        csv_reader = csv.reader(csv_file, delimiter=tab)
        for row in csv_reader:
            # in this csv, element 1 gives business type
            if sic_code_name == row[1]:
                return row[0]


def return_sic_code_names():
    sic_code_names = []
    with open('static/sic_codes.csv') as csv_file:
        tab = chr(9)
        csv_reader = csv.reader(csv_file, delimiter=tab)
        for row in csv_reader:
            sic_code_names.append(row[1])
    return sic_code_names
