import operator

from model import LottoResult, Pair
from extract_data import OUTPUT_FILENAME as INPUT_FILENAME


def get_pairs(numbers):
    pairs = []
    for i in range(0, len(numbers) - 1):
        for m in range(i+1, len(numbers)):
            pairs.append(Pair(numbers[i], numbers[m]))
    return pairs


results = []
with open(INPUT_FILENAME) as file:
    results = [LottoResult.from_csv_entry(l) for l in file.readlines() if "2018" in l]
    # results = [LottoResult.from_csv_entry(l) for l in file.readlines()]
    number_of_pairs = {}
    for r in results:
        pairs = get_pairs(r.results)
        for p in pairs:
            if p in number_of_pairs:
                number_of_pairs[p] = number_of_pairs[p] + 1
            else:
                number_of_pairs[p] = 1

    for key, value in sorted(number_of_pairs.items(), key=operator.itemgetter(1)):
        print("%s => %d" % (key, value))
