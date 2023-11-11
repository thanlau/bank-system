# Simple Banking System

## Introduction
This banking application simulates basic functionalities of a banking system. It includes two main components: a `data_server` class that handles database operations and a `BankMenu` class that provides a user interface. The application uses SQLite for database management, allowing users to create accounts, check balances, transfer funds, and more.

## Features
- **Account Management**: Create and log into bank accounts.
- **Balance Inquiry**: Check the balance of an account.
- **Income Addition**: Deposit money into an account.
- **Funds Transfer**: Transfer money between accounts.
- **Account Closure**: Close and delete an account from the system.
- **User-Friendly Interface**: Navigate the banking system through a menu-driven interface.

## Database
The application uses SQLite (`card.s3db`) for storing user accounts and transaction details.

## Installation
Ensure you have Python installed on your system. No additional libraries are required beyond the standard Python libraries and SQLite.

## Usage
Run the script from the command line to start interacting with the banking system:

```bash
python [script_name].py
```

Follow the on-screen prompts to perform various banking operations. The menu options are:

- 1: Create an account
- 2: Log into an account
- 3: Check balance
- 4: Add income
- 5: Transfer funds
- 6: Close account
- 0: Exit the application
