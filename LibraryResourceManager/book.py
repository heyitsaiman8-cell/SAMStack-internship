from LibraryResource import LibraryResource


class book(LibraryResource):
    def __init__(self, resource_id, title, author, pages):
        super().__init__(resource_id, title, author)
        self.__pages = pages
    def get_pages(self):
      return self.__pages
    def display(self):
        print("\n--- Book ---")
        print("ID:", self.get_id())
        print("Title:", self.get_title())
        print("Author:", self.get_author())
        print("Pages:", self.__pages)
        print("Status:", "Available" if self.is_available() else "Borrowed")