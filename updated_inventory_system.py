"""
Inventory System
----------------
A simple Python inventory management system demonstrating
static code analysis improvements with Pylint, Flake8, and Bandit.
"""

import json
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add_item(stock_data, item, qty):
    """Add quantity of an item to the inventory."""
    if not isinstance(item, str):
        raise ValueError("Item name must be a string.")
    if not isinstance(qty, int):
        raise ValueError("Quantity must be an integer.")
    stock_data[item] = stock_data.get(item, 0) + qty
    logging.info("Added %d of %s", qty, item)
    return stock_data


def remove_item(stock_data, item):
    """Remove an item from the inventory if it exists."""
    try:
        del stock_data[item]
        logging.info("Removed item: %s", item)
    except KeyError:
        logging.warning("Attempted to remove non-existent item: %s", item)
    return stock_data


def get_qty(stock_data, item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("File not found. Returning empty inventory.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON file. Returning empty inventory.")
        return {}


def save_data(stock_data, file_path="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory data saved successfully to %s", file_path)


def print_data(stock_data):
    """Print the inventory report."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return items with quantities below a specified threshold."""
    low_items = {
        item: qty for item, qty in stock_data.items() if qty < threshold
    }
    logging.info(
        "Low stock items (threshold %d): %s", threshold, low_items
    )
    return low_items


def main():
    """Main function to demonstrate inventory operations."""
    stock_data = load_data()
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", 3)
    remove_item(stock_data, "apple")
    print("Apple stock:", get_qty(stock_data, "apple"))
    low_items = check_low_items(stock_data, threshold=5)
    print("Low items:", low_items)
    save_data(stock_data)
    print_data(stock_data)


if __name__ == "__main__":
    main()
