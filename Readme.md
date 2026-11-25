# BankATM README

## Default Details
- **Name:** Hari
- **Default PIN:** `1234`
- **Starting Balance:** `Rs. 10000.00`
- **Wrong PIN Limit:** 3 tries (then card locks)

## What the Program Does
- **PIN First:** Checks your PIN before showing the menu.
- **Show Balance:** Shows current balance, previous balance, and logs the check.
- **Deposit:** Saves old balance, adds amount to current balance, and logs it.
- **Withdraw:** Checks if amount is valid and enough balance exists, updates both balances, and logs it.
- **Change PIN:** Checks old PIN, makes sure new PIN is 4 digits and different, updates PIN, and asks you to log in again.
- **History:** Shows all actions done in the current run.
- **Exit:** Closes the program.

## What Happens on Restart
Data is only saved in memory while the program runs, not in a file:
- **Balance:** Resets back to `Rs. 10000.00`.
- **PIN:** Resets back to `1234`.
- **History:** Clears old transactions and starts fresh.
- **Card Lock:** Resets so you get 3 new PIN tries.