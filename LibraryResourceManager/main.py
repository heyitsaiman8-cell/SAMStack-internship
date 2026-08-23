from book import book
from magazine import magazine
from file_handler import save_all, load_from_json
resources = load_from_json()
if resources:
    print("\n--- Loaded Saved Resources ---")
    for resource in resources:
        resource.display()
else:
    books = book(101, "Python Basics", "Ali", 250)
    magazines = magazine(102, "Tech World", "Ahmed", 15)
    resources = [books, magazines]
    print("\n--- New Resources ---")
    for resource in resources:
        resource.display()
print("\nBorrowing Book...")
resources[0].borrow()
resources[0].display()
print("\nBorrowing Magazine...")
resources[1].borrow()
resources[1].display()
save_all(resources)