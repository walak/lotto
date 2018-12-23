import operator

from extract_data import OUTPUT_FILENAME as INPUT_FILENAME
from service import DataLoader, filter_by_year

results = []
DATA_LOADER = DataLoader(INPUT_FILENAME)
YEARS = range(1957, 2018+1)
NUMBER_OF_TOP_NUMBERS = 6

for year in YEARS:
    results = DATA_LOADER.load(filter=filter_by_year(year))
    number_of_numbers = {}
    for r in results:
        for n in r.results:
            if n in number_of_numbers:
                number_of_numbers[n] = number_of_numbers[n] + 1
            else:
                number_of_numbers[n] = 1
    sorted_results = sorted(number_of_numbers.items(), key=operator.itemgetter(1), reverse=True)
    print("Year: %d" % year)
    for i in range(0, NUMBER_OF_TOP_NUMBERS):
        print("%d: number=%d hits=%d" % (i + 1, sorted_results[i][0], sorted_results[i][1]))
