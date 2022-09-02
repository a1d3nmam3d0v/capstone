class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print(f"{title} has already been published. Write something new.")
        else:
            self.books.append(title)

    def __str__(self):
        book_list = ", ".join(self.books) or "None"
        return f"Author: {self.name}\nBooks published: {book_list}"


def main():
    drSeuss = Author("Dr. Seuss")
    drSeuss.publish("Green Eggs and Ham")
    drSeuss.publish("The Cat in the Hat")
    drSeuss.publish("Oh, the Places You'll Go")
    drSeuss.publish("Green Eggs and Ham")
    print(drSeuss)


main()
