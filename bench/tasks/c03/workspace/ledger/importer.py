import csv
from datetime import datetime

FMT = '%m/%d/%Y'


def load(path):
    out = []
    with open(path) as fh:
        for row in csv.DictReader(fh):
            out.append(datetime.strptime(row['date'], FMT))
    return out
