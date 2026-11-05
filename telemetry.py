import csv


def create():
    with open("data.csv", "w") as csvfile:
        fieldnames = ["first_name", "last_name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

def append(firstname, lastname):
    with open('data.csv', 'a') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({"first_name": firstname, "last_name": lastname})

