# 🏦 Bank Management System – Python OOP

A simple **console-based Bank Management System** built using **Python and Object-Oriented Programming (OOP)** concepts.

This project allows users to create and manage bank accounts, perform deposits and withdrawals, view account details, update account information, and delete accounts. Account data is stored persistently in a **JSON file**.

## 📌 Project Overview

The main purpose of this project is to practice Python OOP concepts by implementing a real-world banking application.

The application provides a menu-driven interface where users can perform different banking operations using their account number and PIN.

## ✨ Features

### 1. Create Account
Users can create a new bank account by providing:

- Name
- Age
- Email
- 4-digit PIN

The system automatically generates a unique account number.

**Account creation rules:**
- User must be at least 18 years old.
- PIN must contain exactly 4 digits.
- Initial account balance is ₹0.

### 2. Deposit Money

Users can deposit money into their account after authentication using:

- Account number
- PIN

The current implementation allows deposits greater than ₹0 and up to ₹10,000 per transaction.

### 3. Withdraw Money

Users can withdraw money after entering their account number and PIN.

The system checks:

- Whether the account exists
- Whether the PIN is correct
- Whether the withdrawal amount is valid
- Whether sufficient balance is available

The withdrawal limit is ₹10,000 per transaction.

### 4. View Account Details

Authenticated users can view their:

- Name
- Age
- Email
- PIN
- Account number
- Balance

### 5. Update Account Details

Users can update:

- Name
- Email
- PIN

The following fields cannot be changed:

- Age
- Account number
- Balance

Users can leave a field blank if they don't want to modify it.

### 6. Delete Account

Users can delete their account after entering the correct account number and PIN.

The system asks for confirmation before deleting the account.

### 7. JSON Data Storage

Account information is stored in:

```text
data.json
```

The application reads the existing data when the program starts and updates the JSON file whenever account information changes.

## 🧠 OOP Concepts Used

This project currently demonstrates several Python OOP concepts.

### Class

The main class used is:

```python
class Bank:
```

The class contains the banking data and operations.

### Class Variables

The project uses class variables:

```python
database = 'data.json'
data = []
```

These are used to maintain the JSON database location and account data.

### Class Methods

The project uses `@classmethod` for operations that work with class-level data:

```python
@classmethod
def __update(cls):
```

and:

```python
@classmethod
def __generate_account_number(cls):
```

### Encapsulation

Private methods are created using double underscores:

```python
__update()
__generate_account_number()
```

These methods are intended to be used internally by the `Bank` class.

### Objects

An object of the `Bank` class is created using:

```python
user = Bank()
```

The object is then used to perform banking operations.

## 🛠️ Technologies Used

- **Python 3**
- **JSON**
- **OOP (Object-Oriented Programming)**
- **Pathlib**
- **Random**
- **String**

## 📂 Project Structure

```text
BANK MANAGEMENT/
│
├── main.py
├── data.json
└── README.md
```

> The filenames may differ depending on how the project is organized locally.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/azeem-shaik/bank-management-system-python.git
```

### 2. Navigate to the project directory

```bash
cd bank-management-system-python
```

### 3. Run the Python program

```bash
python main.py
```

## 💻 Application Menu

When the program starts, it provides the following options:

```text
Press 1 for creating an account:
Press 2 for Depositing the money in your account:
Press 3 for Withdrawing the money:
Press 4 for Details:
Press 5 for Updating the details:
Press 6 for deleting your account:
```

The user can select an operation by entering the corresponding number.

## 🔐 Authentication

The following operations require authentication:

- Deposit
- Withdraw
- View Details
- Update Details
- Delete Account

Authentication is performed using:

```text
Account Number + PIN
```

## 📄 Example Account Data

The account information is stored in JSON format similar to:

```json
[
    {
        "name": "Azeem",
        "age": 24,
        "email": "azeem@example.com",
        "pin": 1234,
        "accountNo.": "AbC123@",
        "balance": 5000
    }
]
```

## 🔮 Future Improvements

The project can be extended with:

- Transaction history
- Money transfer between accounts
- Savings account and current account classes
- Interest calculation
- Better input validation
- Exception handling for invalid user input
- Password/PIN security improvements
- SQLite or MySQL database integration
- Unit testing
- Improved menu loop
- GUI or web-based interface
- Multiple users and role-based access

## ⚠️ Disclaimer

This project is created for **educational purposes** to practice Python programming and OOP concepts.

It is **not intended for handling real financial transactions or sensitive banking information**.

## 👨‍💻 Author

**Azeem Shaik**

GitHub:  
https://github.com/azeem-shaik

## ⭐ Project

If you find this project useful for learning Python OOP, feel free to explore the repository.