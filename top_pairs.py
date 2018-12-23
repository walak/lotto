import operator

from model import LottoResult, Pair
from extract_data import OUTPUT_FILENAME as INPUT_FILENAME
from service import DataLoader, filter_by_year


def get_pairs(numbers):
    extracted_pairs = []
    for i in range(0, len(numbers) - 1):
        for m in range(i + 1, len(numbers)):
            extracted_pairs.append(Pair(numbers[i], numbers[m]))
    return extracted_pairs


if __name__ == "__main__":
    DATA_LOADER = DataLoader(INPUT_FILENAME)
    results = DATA_LOADER.load(filter_by_year(2018))
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
