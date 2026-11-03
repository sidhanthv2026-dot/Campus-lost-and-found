# Campus Lost & Found Management System

A menu-driven Python project that helps a college campus maintain reports of lost and found belongings.

## Features

- Report a lost item with its name, category, last-seen location, description and contact details.
- Report a found item with its name, category, found location, description and finder's name.
- View all submitted reports.
- Search reports by item name or category.
- Mark an item as returned.
- Validate empty inputs and invalid item IDs.

## Python OOP concepts used

### 1. Classes and objects
`Item`, `LostItem`, `FoundItem` and `LostAndFoundSystem` are classes. The program creates objects from `LostItem` and `FoundItem` whenever a report is submitted.

### 2. Inheritance
`LostItem` and `FoundItem` inherit from the parent class `Item`. The `super()` function is used to call the parent class constructor and reuse its attributes and methods.

### 3. Encapsulation
The `Item` class stores its data in private attributes such as `__name`, `__category` and `__status`. These values are accessed through getter methods. The status is changed through `mark_returned()` rather than being modified directly from outside the class.

### 4. Polymorphism
Both `LostItem` and `FoundItem` override the `display()` method. When the program calls `item.display()`, Python executes the version belonging to that object's actual class.

## Requirements

- Python 3.8 or later
- No external libraries are required.

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Project structure

```text
Campus-Lost-and-Found/
├── main.py
├── README.md
└── screenshots/
```

## Note

This is a console-based academic demonstration. Reports are stored in memory while the program is running and are cleared when it exits. It does not use a database or collect information online.
