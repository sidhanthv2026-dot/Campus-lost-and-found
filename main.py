"""
Campus Lost & Found Management System
A beginner-friendly Python OOP project.

OOP concepts demonstrated:
1. Classes and objects
2. Inheritance
3. Encapsulation
4. Polymorphism

Run using: python main.py
"""

class Item:
    """Base class representing an item reported on campus."""

    def __init__(self, item_id, name, category, location, description):
        self.__item_id = item_id
        self.__name = name
        self.__category = category
        self.__location = location
        self.__description = description
        self.__status = "Open"

    # Getter methods demonstrate controlled access to private attributes.
    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_location(self):
        return self.__location

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def mark_returned(self):
        self.__status = "Returned"

    def display(self):
        """Common display method; overridden by child classes."""
        print(f"ID          : {self.__item_id}")
        print(f"Item        : {self.__name}")
        print(f"Category    : {self.__category}")
        print(f"Location    : {self.__location}")
        print(f"Description : {self.__description}")
        print(f"Status      : {self.__status}")


class LostItem(Item):
    """Represents an item that someone has lost."""

    def __init__(self, item_id, name, category, location, description, contact):
        super().__init__(item_id, name, category, location, description)
        self.__contact = contact

    def display(self):
        print("\n--- LOST ITEM ---")
        super().display()
        print(f"Contact     : {self.__contact}")


class FoundItem(Item):
    """Represents an item that someone has found."""

    def __init__(self, item_id, name, category, location, description, finder):
        super().__init__(item_id, name, category, location, description)
        self.__finder = finder

    def display(self):
        print("\n--- FOUND ITEM ---")
        super().display()
        print(f"Reported by : {self.__finder}")


class LostAndFoundSystem:
    """Manages all lost and found reports."""

    def __init__(self):
        self.items = []
        self.next_id = 1

    def report_lost_item(self):
        print("\nREPORT A LOST ITEM")
        name = input("Item name: ").strip()
        category = input("Category (e.g. Electronics, ID Card): ").strip()
        location = input("Where was it last seen? ").strip()
        description = input("Description: ").strip()
        contact = input("Your contact details: ").strip()

        if not all([name, category, location, description, contact]):
            print("All fields are required. Report not saved.")
            return

        item = LostItem(self.next_id, name, category, location, description, contact)
        self.items.append(item)
        self.next_id += 1
        print("Lost-item report submitted successfully.")

    def report_found_item(self):
        print("\nREPORT A FOUND ITEM")
        name = input("Item name: ").strip()
        category = input("Category (e.g. Electronics, ID Card): ").strip()
        location = input("Where was it found? ").strip()
        description = input("Description: ").strip()
        finder = input("Your name: ").strip()

        if not all([name, category, location, description, finder]):
            print("All fields are required. Report not saved.")
            return

        item = FoundItem(self.next_id, name, category, location, description, finder)
        self.items.append(item)
        self.next_id += 1
        print("Found-item report submitted successfully.")

    def view_all_items(self):
        print("\nALL ITEM REPORTS")
        if not self.items:
            print("No reports have been submitted yet.")
            return

        for item in self.items:
            item.display()  # Polymorphism: the correct child display() runs.

    def search_items(self):
        keyword = input("\nEnter item name or category to search: ").strip().lower()
        if not keyword:
            print("Please enter a search term.")
            return

        matches = [
            item for item in self.items
            if keyword in item.get_name().lower()
            or keyword in item.get_category().lower()
        ]

        if not matches:
            print("No matching reports found.")
            return

        print(f"\nFound {len(matches)} matching report(s):")
        for item in matches:
            item.display()

    def mark_item_returned(self):
        try:
            item_id = int(input("\nEnter the ID of the item to mark as returned: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        for item in self.items:
            if item.get_item_id() == item_id:
                if item.get_status() == "Returned":
                    print("This item has already been marked as returned.")
                else:
                    item.mark_returned()
                    print("Item status updated to Returned.")
                return

        print("No item found with that ID.")

    def run(self):
        while True:
            print("\n======================================")
            print(" CAMPUS LOST & FOUND MANAGEMENT SYSTEM")
            print("======================================")
            print("1. Report a lost item")
            print("2. Report a found item")
            print("3. View all reports")
            print("4. Search for an item")
            print("5. Mark an item as returned")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.report_lost_item()
            elif choice == "2":
                self.report_found_item()
            elif choice == "3":
                self.view_all_items()
            elif choice == "4":
                self.search_items()
            elif choice == "5":
                self.mark_item_returned()
            elif choice == "6":
                print("Thank you for using the Campus Lost & Found System!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    system = LostAndFoundSystem()
    system.run()
