import operator

from extract_data import OUTPUT_FILENAME as INPUT_FILENAME
from service import DataLoader, filter_by_year

results = []
DATA_LOADER = DataLoader(INPUT_FILENAME)

results = DATA_LOADER.load(filter=filter_by_year(2018))
number_of_numbers = {}
for r in results:
    for n in r.results:
        if n in number_of_numbers:
            number_of_numbers[n] = number_of_numbers[n] + 1
        else:
            number_of_numbers[n] = 1

for key, value in sorted(number_of_numbers.items(), key=operator.itemgetter(1)):
    print("%s => %d" % (key, value))
