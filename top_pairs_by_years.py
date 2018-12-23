import operator

from extract_data import OUTPUT_FILENAME as INPUT_FILENAME
from service import DataLoader, filter_by_year
from top_pairs import get_pairs


if __name__ == "__main__":
    results = []
    DATA_LOADER = DataLoader(INPUT_FILENAME)
    YEARS = range(1957, 2018 + 1)
    NUMBER_OF_TOP_NUMBERS = 6

    for year in YEARS:
        results = DATA_LOADER.load(filter=filter_by_year(year))
        number_of_pairs = {}
        for r in results:
            extracted_pairs = get_pairs(r.results)
            for p in extracted_pairs:
                if p in number_of_pairs:
                    number_of_pairs[p] = number_of_pairs[p] + 1
                else:
                    number_of_pairs[p] = 1
        sorted_results = sorted(number_of_pairs.items(), key=operator.itemgetter(1), reverse=True)
        print("Year: %d" % year)
        for i in range(0, NUMBER_OF_TOP_NUMBERS):
            print("%d: pair=%s hits=%d" % (i + 1, str(sorted_results[i][0]), sorted_results[i][1]))
