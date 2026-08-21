from LibraryResource import LibraryResource


class magazine(LibraryResource):

    def __init__(self, resource_id, title, author, issue_number):
        super().__init__(resource_id, title, author)
        self.__issue_number = issue_number
    def get_issue_number(self):
      return self.__issue_number
    def display(self):
        print("\n--- Magazine ---")
        print("ID:", self.get_id())
        print("Title:", self.get_title())
        print("Author:", self.get_author())
        print("Issue Number:", self.__issue_number)
        print("Status:", "Available" if self.is_available() else "Borrowed")