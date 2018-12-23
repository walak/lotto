class LottoResult:

    def __init__(self, id, date, results):
        self.id = id
        self.date = date
        self.results = results

    def to_csv_entry(self):
        return "%s, %s, %s" % (self.id, self.date, ", ".join(self.results))

    @staticmethod
    def from_html_lis(li_tags):
        return LottoResultBuilder().with_lis(li_tags).build()

    @staticmethod
    def from_csv_entry(line):
        elements = [e.strip() for e in line.split(",")]
        return LottoResult(elements[0], elements[1], elements[2:])


class LottoResultBuilder:
    def __init__(self):
        self.lis = []

    def with_lis(self, lis):
        self.lis = lis
        return self

    def build(self):
        number = self.get_name(self.lis[0])
        date = self.lis[1].text
        results = self.get_numbers(self.lis[2:])
        return LottoResult(number, date, results)

    def get_name(self, li):
        return li.text.replace(".", "")

    def get_numbers(self, lis):
        return [l.text.strip() for l in lis]


class Pair:

    def __init__(self, a, b):
        if a > b:
            self.a = b
            self.b = a
        else:
            self.a = a
            self.b = b

    def __hash__(self):
        return 37 * self.a + 41 * self.b

    def __eq__(self, other):
        if other is None or not isinstance(other, Pair):
            return False
        else:
            return self.a == other.a and self.b == other.b
