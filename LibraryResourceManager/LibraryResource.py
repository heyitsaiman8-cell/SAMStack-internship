class LibraryResource:
    def __init__(self, resource_id, title, author):
        self.__resource_id = resource_id
        self.__title = title
        self.__author = author
        self.__available = True
    def get_id(self):
        return self.__resource_id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def is_available(self):
        return self.__available
    def borrow(self):
        if self.__available:
            self.__available = False
            print("Resource borrowed successfully.")
        else:
            print("Resource is already borrowed.")
    def return_resource(self):
        if not self.__available:
            self.__available = True
            print("Resource returned successfully.")
        else:
            print("Resource is already available.")
    def display(self):
        print("ID:", self.__resource_id)
        print("Title:", self.__title)
        print("Author:", self.__author)
        print("Status:", "Available" if self.__available else "Borrowed")
    def get_status(self):
        return "Available" if self.__available else "Borrowed"