#wheather key or value exist in dictionary
book={
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "year": 1958
}
if 1958 in book.values():
    print("Year is 1958")
else:
    print("Year is not 1958")
    