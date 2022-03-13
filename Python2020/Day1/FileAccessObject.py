import csv

class FileAccessObject:
    def __init__(fileData):
        with open("data.txt", rt) as csvFile:
            csvReader = csv.reader(csvFile)