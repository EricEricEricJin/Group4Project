import csv

class writeFile:
    def __init__(self, fname):
        self.file = open(fname, "w")
        self.fcsv = csv.writer(self.file)

    def write(self, data_list):
        self.fcsv.writerow(data_list)

    def __del__(self):
        self.file.close()
