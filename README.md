[Uploading README.md…]()
# Zenith-Bank# Zenith Bank: Bank Management System

Zenith Bank is a terminal-based Bank Management System built specifically to satisfy the project rubric expectations, using fundamental Python concepts. It offers a highly aesthetic interface, robust error handling, and file-based data persistence.

## 2.1 Functional Requirements

### Three Major Functional Modules
1. **Authentication & Account Management (`modules/auth.py`)**: Handles new account creation, secure login via PIN, and automated unique Account Number generation.
2. **Transaction Management (`modules/transactions.py`)**: Facilitates deposits, withdrawals, and peer-to-peer transfers between accounts. It also tracks the transaction history to generate account statements.
3. **Loan Management (`modules/loans.py`)**: Allows users to apply for bank loans with automated instant approval (for values <= $10,000) and enables them to pay off active loans.

### Clear Input/Output Structure
- **Inputs**: User prompts for integers and floats during transactions (e.g., amount to withdraw, PIN).
- **Outputs**: Detailed, color-coded terminal interfaces (Dashboards, Success/Error prompts, and formatted tabular statements).

### Logical Workflow
1. User creates a new bank account, receives a unique Account Number, and logs in.
2. The user interacts with their personalized Dashboard displaying their current balance.
3. The user executes transactions (like depositing cash or transferring to a friend).
4. The user views their Account Statement to see a historically logged list of the transactions.
5. If the user needs money, they apply for a loan and later use their account balance to pay it off.

## 2.2 Non-Functional Requirements

1. **Usability (Aesthetics)**: The terminal output heavily uses ANSI color codes. It simulates a modern, clean command-line UI with banners, menus, and clear screen transitions.
2. **Error Handling**: Using custom input validation wrappers (`get_int_input`, `get_float_input` in `utils/ui.py`), it guarantees the app won't crash when strings are entered instead of transaction amounts. It also handles edge cases like insufficient funds or paying towards non-existent loans.
3. **Maintainability**: The application is highly structured across 6 different Python modules in dedicated folders, ensuring clean, logical separation of concerns (SoC).
4. **Reliability (Persistence)**: It uses a unified `storage.py` manager to save data persistently to `accounts.json`, `transactions.json`, and `loans.json` so no bank data is lost after shutting down.

## 3. Technical Expectations

- **Modular Design**: The project has exactly 6 meaningful classes/modules (`auth.py`, `transactions.py`, `loans.py`, `storage.py`, `ui.py`, `main.py`).
- **Clean Folder Structure**: Categorized neatly into `data/`, `modules/`, and `utils/`.
- **Validation**: All monetary transactions prevent negative values, and login logic manages blocked/invalid account states gracefully.

## How to Run

1. Open your terminal.
2. Navigate to the `ZenithBank` directory:
   ```bash
   cd c:\Users\ADMIN\ANTIG\ZenithBank
   ```
3. Run the main file:
   ```bash
   python main.py
   ```
