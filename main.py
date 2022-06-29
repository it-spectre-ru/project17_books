from urllib import response
import requests
from bs4 import BeautifulSoup

def get_data():
  headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

  url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"

  response = requests.get(url=url, headers=headers)
  soup = BeautifulSoup(response.text, "lxml")

  pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)
  
  # for page in range(1, pages_count + 1):
  for page in range(1, 2):
    url = f"https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table&page={page}"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    book_items = soup.find("tbody", class_="products-table__body").find_all("tr")

    for bi in book_items:
      book_data = bi.find_all("td")

      try:
        book_title = book_data[0].find("a").text.strip()
      except:
        book_title = "Not books name"

      print(book_title)




def main():
  get_data()


if __name__ == '__main__':
  main()