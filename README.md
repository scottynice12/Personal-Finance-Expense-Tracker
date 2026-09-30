📊 Personal Finance & Expense Tracker
A lightweight, terminal-based financial utility built using Python 3.14. This application allows you to securely input expenses, validate data entries, dynamically organize transactions by categories, and automatically save data to a local spreadsheet (expenses.csv).
🚀 Setup & Installation
Before running the application, ensure you have Python 3.14 installed on your system and that your file is named exactly finance_tracker.py.
Place your file inside your project directory:
C:\Users\YourUserName\OneDrive\Documents\FinanceExpenseTracker

🎛️ How to Run the Application
You can run this application using either your computer's regular terminal (Command Prompt) or directly inside the standalone Python 3.14 Application. Choose the method that matches your setup below:
Method 1: Using the Regular Terminal (Command Prompt / cmd)
1. Open your computer's standard terminal (cmd).
   
2. Navigate to your project folder using the cd command:cmd
cd OneDrive\Documents\FinanceExpenseTracker

Use code with caution.
4. Launch the script directly:cmd
   
python finance_tracker.py

Method 2: Using the Standalone Python 3.14 Application
If you have launched the official Python 3.14 window (where the prompt shows >>>), standard terminal commands like cd will not work. Follow these steps instead:
1. Open the Python 3.14 App.
2. Change your active folder directory by running this line and pressing Enter:
import os; os.chdir(r"C:\Users\Username\OneDrive\Documents\FinanceExpenseTracker")

3. Force Python to open and decode your file with proper layout compatibility by running this command:
4.  python exec(open("finance_tracker.py", encoding="utf-8").read())
Use code with caution.
🕹️ How to Navigate the Menu
Once the application opens, follow the on-screen numbers to manage your budget:
• Type 1 and press Enter to add a new expense. You will be asked for the Amount ($), a Category number (1–5), and a short Description.
• Type 2 and press Enter to view your running financial totals along with an automatic percentage breakdown of your spending habits.
• Type 3 and press Enter to safely close the application.

