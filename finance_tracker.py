import csv
from datetime import datetime
import os
from pathlib import Path

# File setup
DATA_FILE = Path("expenses.csv")

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist yet."""
    if not DATA_FILE.exists():
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount ($)", "Category", "Description"])
        print(f"✨ Created a brand new tracking sheet: {DATA_FILE}")

def add_expense():
    """Prompts user for input and appends a new row to the CSV."""
    print("\n--- 💸 Add New Expense ---")
    
    # 1. Get and validate Amount
    while True:
        try:
            amount = float(input("Enter amount spent ($): "))
            if amount <= 0:
                print("❌ Please enter an amount greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number (e.g., 12.50).")

    # 2. Get Category
    print("\nSelect a category:")
    categories = ["Food", "Transport", "Rent/Bills", "Entertainment", "Other"]
    for i, cat in enumerate(categories, 1):
        print(f" [{i}] {cat}")
    
    while True:
        try:
            choice = int(input("Choose a category number: "))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            print(f"❌ Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    # 3. Get Description
    description = input("Enter a brief description: ").strip()
    if not description:
        description = "Unspecified"

    # 4. Get Current Date/Time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 5. Save to File
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([current_date, f"{amount:.2f}", category, description])
    
    print(f"✅ Successfully logged ${amount:.2f} under '{category}'!")

def view_summary():
    """Reads the CSV file to calculate totals and breakdown percentages."""
    print("\n--- 📊 Financial Summary ---")
    if not DATA_FILE.exists():
        print("No expenses recorded yet!")
        return

    total_spending = 0.0
    category_totals = {}

    with open(DATA_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header row
        
        rows = list(reader)
        if not rows:
            print("Your expense log is currently empty.")
            return

        for row in rows:
            amount = float(row[1])
            category = row[2]
            
            total_spending += amount
            category_totals[category] = category_totals.get(category, 0.0) + amount

    # Display results
    print(f"🔹 Total Money Spent: ${total_spending:.2f}\n")
    print("Category Breakdown:")
    for cat, subtotal in category_totals.items():
        percentage = (subtotal / total_spending) * 100
        print(f" 📦 {cat:<15} : ${subtotal:>7.2f} ({percentage:.1f}%)")

# Main Application Loop
def main():
    initialize_file()
    while True:
        print("\n==============================")
        print("     PYTHON FINANCE TOOL      ")
        print("==============================")
        print(" [1] Log a New Expense")
        print(" [2] View Spending Summary")
        print(" [3] Exit App")
        
        choice = input("What would you like to do? ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("\n👋 Goodbye! Keep budget tracking!")
            break
        else:
            print("❌ Invalid selection. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()
