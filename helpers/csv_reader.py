import csv

from model.gem import Gem


def read_gem_from_csv(file):
    gem = []
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            gem.append(Gem(row[0], int(row[1]), int(row[2])))
    return gem
