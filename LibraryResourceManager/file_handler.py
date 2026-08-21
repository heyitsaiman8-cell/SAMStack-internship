import json
import csv
from book import book
from magazine import magazine
def save_to_txt(resources):
    with open("resources.txt", "w") as file:
        for resource in resources:
            file.write(
                f"{resource.get_id()} | "
                f"{resource.get_title()} | "
                f"{resource.get_author()} | "
                f"{resource.get_status()}\n"
            )
def save_to_json(resources):
    data = []
    for resource in resources:
        if resource.__class__.__name__ == "book":
            resource_type = "Book"
            extra = resource.get_pages()
        else:
            resource_type = "Magazine"
            extra = resource.get_issue_number()
        data.append({
            "type": resource_type,
            "id": resource.get_id(),
            "title": resource.get_title(),
            "author": resource.get_author(),
            "extra": extra,
            "status": resource.get_status()
        })
    with open("resources.json", "w") as file:
        json.dump(data, file, indent=4)
def save_to_csv(resources):
    with open("resources.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Type",
            "ID",
            "Title",
            "Author",
            "Extra",
            "Status"
        ])
        for resource in resources:
            if resource.__class__.__name__ == "book":
                resource_type = "Book"
                extra = resource.get_pages()
            else:
                resource_type = "Magazine"
                extra = resource.get_issue_number()
            writer.writerow([
                resource_type,
                resource.get_id(),
                resource.get_title(),
                resource.get_author(),
                extra,
                resource.get_status()
            ])
def save_all(resources):
    save_to_txt(resources)
    save_to_json(resources)
    save_to_csv(resources)
    print("\nData saved successfully!")
    print("Created: resources.txt")
    print("Created: resources.json")
    print("Created: resources.csv")
def load_from_json():
    try:
        with open("resources.json", "r") as file:
            data = json.load(file)
        resources = []
        for item in data:
            if item["type"] == "Book":
                resource = book(
                    item["id"],
                    item["title"],
                    item["author"],
                    item["extra"]
                )
            else:
                resource = magazine(
                    item["id"],
                    item["title"],
                    item["author"],
                    item["extra"]
                )
            if item["status"] == "Borrowed":
                resource.borrow()
            resources.append(resource)
        return resources
    except FileNotFoundError:
        return []