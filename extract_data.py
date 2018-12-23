from bs4 import BeautifulSoup
from model import LottoResult

INPUT_FILENAME = "resources/data.html"
OUTPUT_FILENAME = "resources/data.csv"

if __name__ == "__main__":
    results = []

    with open(INPUT_FILENAME) as file:
        soup = BeautifulSoup(file, features="html.parser")
        for ul in soup.find_all('ul'):
            lis = ul.find_all('li')
            result = LottoResult.from_html_lis(lis)
            results.append(result)

    with open(OUTPUT_FILENAME, mode='w') as file:
        results.reverse()
        file.writelines([r.to_csv_entry() + "\n" for r in results])

    # soup.find_all('ul')[0].find_all('li')
