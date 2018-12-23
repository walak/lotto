from model import LottoResult


def no_filtering(lotto_result):
    return True


def filter_by_year(year):
    def filter_year(lotto_result):
        return str(year) in lotto_result.date

    return filter_year


class DataLoader:

    def __init__(self, data_file):
        self.data_file = data_file

    def load(self, filter=no_filtering):
        with open(self.data_file) as file:
            return [r for r in [LottoResult.from_csv_entry(l) for l in file.readlines()] if filter(r)]
