# Financial Management System

## Overview
This is a simple financial management system that allows users to create and manage bank accounts, transfer funds, track transactions, and visualize financial data. The system is built using Python with SQLModel and SQLite for database management.

## Features
- **Create account**: Open a new bank account.
- **Deactivate account**: Deactivate an existing account (only if balance is zero).
- **Transfer money**: Move funds between accounts.
- **Move money**: Deposit or withdraw funds from an account.
- **Total accounts**: Display all existing accounts and total balance.
- **Filter history**: Search for transactions based on criteria.
- **Graphic**: Visualize account balances and transaction trends.
- **Exit program**: Close the application.

## Technologies Used
- **Python**
- **SQLModel** (ORM for database handling)
- **SQLite** (Lightweight database)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/financial-management.git
   cd financial-management
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv    # On Linux use: python3 -m venv venv
   venv\Scripts\activate  # On Linux use: source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install sqlmodel
   pip install matplotlib
   ```
4. Run the program:
   ```sh
   python templates.py
   ```

## Usage
Once the program starts, a menu will appear with the following options:
```
[1] -> Create account
[2] -> Deactivate account
[3] -> Transfer money
[4] -> Move money
[5] -> Total accounts
[6] -> Filter history
[7] -> Graphic
[8] -> Exit program
```
### Creating an Account
To create a new account, select option **1**, then provide the required details such as bank name and initial balance.

### Transferring Money
To transfer funds, select option **3**, then specify the source and destination accounts along with the transfer amount.

### Moving Money
To deposit or withdraw funds, select option **4**, choose the account, and specify the amount.

### Viewing Account Data
To see a list of all accounts, select **5**. To filter transaction history, select **6**. To visualize data through graphs, choose **7**.

### Exiting the Program
Select **8** to exit.

## Database Schema
The system uses two main database tables:
- **Account**: Stores account details (ID, bank name, status, balance).
  Example:
  <p align="center">
      <img src="https://github.com/user-attachments/assets/26e08f57-ba01-490d-a4ed-abdedc985d57" alt="" width="700">
</p>

- **Historic**: Stores transaction records (ID, account ID, type, amount, date).
  Example:
  <p align="center">
      <img src="https://github.com/user-attachments/assets/5ac7513d-eafd-4aa2-b9ed-f9d098338ef6" alt="" width="700">
  </p>

## Error Handling
- Prevents creating duplicate accounts with the same bank.
- Disallows deactivating accounts with a nonzero balance.
- Ensures sufficient balance before processing withdrawals or transfers.

## Observations
- IDE used in the project: <a href="https://code.visualstudio.com/download">Visual Studio Code</a>.
- Database viewer used <a href="https://github.com/qwtel/sqlite-viewer-vscode">SQLite Viwer for VS Code</a>.
