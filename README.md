Banking System in Python
A simple command-line banking system that allows users to check their balance, deposit money, and withdraw funds.

🚀 Features
✅ Show Balance – View the current account balance.
✅ Deposit Money – Add money to your account (only positive values are accepted).
✅ Withdraw Money – Withdraw money if you have sufficient balance.
✅ Exit Option – Quit the program when finished.

🛠 How It Works
The program starts with an initial balance of $0.
The user is presented with a menu of options:
1 Show Balance
2 Deposit
3 Withdraw
4 Exit
The user selects an option by entering a number (1-4).
The program ensures valid inputs:
Deposits must be positive.
Withdrawals cannot exceed the available balance.
Withdrawals must be greater than 0.
The program continues running until the user selects Exit (4).
📌 Example Usage
pgsql
Copy
Edit
-----------------------
--- Welcome to the Bank ---
-----------------------
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
What service do you want, Sir/Mam? (1-4): 2
Enter the amount you want to deposit: 200
Successfully deposited $200. Your new balance is $200.

What service do you want, Sir/Mam? (1-4): 3
How much money do you want to withdraw?: 50
Successfully withdrew $50. Your new balance is $150.

What service do you want, Sir/Mam? (1-4): 1
Your current balance is $150.

What service do you want, Sir/Mam? (1-4): 4
Thank you for visiting the bank!
🏗 Future Improvements
🔹 Implement user authentication (PIN/Password).
🔹 Support for multiple user accounts.
🔹 Store transaction history in a database or file.
🔹 Add graphical user interface (GUI) using Tkinter or PyQt.

📂 How to Run the Program
Clone the repository:
bash
Copy
Edit
git clone https://github.com/Rjrameez67/banking-system.git
Navigate to the project folder:
bash
Copy
Edit
cd banking-system
Run the script:
bash
Copy
Edit
python banking.py
🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License
This project is licensed under the MIT License.
