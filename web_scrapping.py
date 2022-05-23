# Program to read a web page and give back a list of the 10 most expensive books from among the most popular
from bs4 import *
import requests


def book_info():
    """
    Function to fetch book information: title, number of reviews and price
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 '
                      'Safari/537.36'
    }
    page1_info = requests.get(
        "https://www.amazon.com/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1", headers=header).text

    page1_html = BeautifulSoup(page1_info, 'lxml')
    page1_books = page1_html.select(".zg-item-immersion")

    books_dict = {}

    for book in page1_books:
        book_price = float(book.find(name="span", class_="p13n-sc-price").text.strip().replace("$", ""))
        book_name = book.find(name="div", class_="p13n-sc-truncate p13n-sc-line-clamp-1").text.strip()

        # leaves out books with no published number of reviews
        if book.find(name="a", class_="a-size-small a-link-normal") is None:
            continue
        else:
            book_review = int(book.find(name="a", class_="a-size-small a-link-normal").text.replace(",", ""))
            books_dict[book_name] = [book_review, book_price]
    review(books_dict)


def review(books_dict):
    """
    Function to filter the top 30 books with most reviews
    :param books_dict: A dictionary containing information about the books on the website's first page

    """
    reviews_list = []
    reviews_dict = {}
    for book in books_dict:
        reviews_list.append(books_dict[book][0])
    x = sorted(reviews_list, reverse=True)
    y = x[:30]
    for book in books_dict:
        for item in y:
            if books_dict[book][0] == item:
                reviews_dict[book] = books_dict[book]

    price(reviews_dict)


def price(reviews_dict):
    """
    Function to filter the top 10 most expensive books from the 30 books with most reviews
    :param reviews_dict: A dictionary containing information on the top 30 books with the most reviews
    """
    price_list = []
    price_dict = {}
    for book in reviews_dict:
        price_list.append(reviews_dict[book][1])
    x = sorted(price_list, reverse=True)
    for item in x[:10]:
        for book in reviews_dict:
            if reviews_dict[book][1] == item:
                price_dict[book] = reviews_dict[book]
    display(price_dict)


def display(price_dict):
    """
    Function to display information on the top 10 most expensive books
    among the top 30 with most reviews
    :param price_dict: A dictionary containing information on the top 10 most
     expensive books among those with most reviews
    """
    for book in price_dict:
        print("Title: {}, Reviews: {}, Price: ${:.2f}".format(book, price_dict[book][0], price_dict[book][1]))


book_info()
