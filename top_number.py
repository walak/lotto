import operator

from model import LottoResult
from extract_data import OUTPUT_FILENAME as INPUT_FILENAME

results = []
with open(INPUT_FILENAME) as file:
    results = [LottoResult.from_csv_entry(l) for l in file.readlines() if "2018" in l]
    # results = [LottoResult.from_csv_entry(l) for l in file.readlines()]
    number_of_numbers = {}
    for r in results:
        for n in r.results:
            if n in number_of_numbers:
                number_of_numbers[n] = number_of_numbers[n] + 1
            else:
                number_of_numbers[n] = 1

    for key, value in sorted(number_of_numbers.items(), key=operator.itemgetter(1)):
        print("%s => %d" % (key, value))
