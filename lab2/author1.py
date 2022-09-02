class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        book_list = ", ".join(self.books) or "None"
        return f"Author: {self.name}\nBooks published: {book_list}"

    def publish(self, title):
        self.books.append(title)


def main():
    drSeuss = Author("Dr. Seuss")
    drSeuss.publish("Green Eggs and Ham")
    drSeuss.publish("The Cat in the Hat")
    drSeuss.publish("Oh, the Places You'll Go")
    print(drSeuss)


main()
