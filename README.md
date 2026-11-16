# Expense Tracker (Python Mini Project) 💰

A beginner-friendly, interactive command-line **Expense Tracker** built completely with pure Python—no external libraries required. It uses Python lists and dictionaries to record daily expenses, view transaction history, and calculate total spending.

## ✨ Features

- **Interactive Menu Loop:** Simple numbered menu (`1`–`4`) for smooth navigation.
- **Add Expenses:** Record each expense with a **Date**, **Category** (food, travel, shopping, etc.), **Description**, and **Amount**.
- **View All Expenses:** Displays a numbered list of all recorded expenses (or notifies you if the list is empty).
- **Total Expense Calculation:** Automatically calculates the sum of all recorded expenses.
- **Zero Dependencies:** Runs using only built-in Python features (`list`, `dict`, loops, and `sum()`).

## 📋 Menu Options

| Option | Action | Description |
| :---: | :--- | :--- |
| `1` | **Add expense** | Enter date, category, details, and amount to save a new expense |
| `2` | **View all expenses** | Lists all stored expenses in numbered order |
| `3` | **Total expense** | Calculates and displays the total amount spent |
| `4` | **Exit** | Exits the application |

## 🛠️ Built With

- **Language:** Python 3.x

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd expense-tracker
   ```

3. **Run the application**
   ```bash
   python main.py
   ```
   *(Replace `main.py` with your actual `.py` filename if different.)*

## 💻 Example Usage

```text
Welcome🙋🏻 in Expense Tracker : invest your money on right place😊
«««MENU»»»
1 :Add expense
2:view all expenses
3:Total expense
4:Exit 
enter your choice: 1
Enter date of expense: 16-11-2026
Enter type (food, travel, shopping etc.): food
Enter the details: Lunch
Enter total amount: 150
[{'Date': '16-11-2026', 'Category': 'food', 'Description': 'Lunch', 'Amount': 150.0}]
Bro!  Expense added successfully 😊.

«««MENU»»»
1 :Add expense
2:view all expenses
3:Total expense
4:Exit 
enter your choice: 2
 This is your all expenses —
Expense number-1→
16-11-2026 ,food ,     Lunch ,150.0

«««MENU»»»
1 :Add expense
2:view all expenses
3:Total expense
4:Exit 
enter your choice: 3
Total expense: 150.0

«««MENU»»»
1 :Add expense
2:view all expenses
3:Total expense
4:Exit 
enter your choice: 4
Exiting. Goodbye! Thanks for using our system.
```

## 🧠 Concepts Practiced

- Storing structured records using a **list of dictionaries**
- Infinite `while True` loops and `break` statements
- Conditional branching (`if` / `elif` / `else`)
- User input handling and type conversion (`int()`, `float()`)
- Calculating totals with `sum()` and generator expressions
- String formatting using Python `f-strings`

## 🔮 Future Improvements

- Save expenses permanently to a `.csv` or `.json` file
- Add error handling (`try-except`) for invalid menu or amount inputs
- Filter expenses by category or date

## 📝 License

This project is open source and available under the [MIT License](LICENSE).


