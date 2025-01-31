import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction_type, category, amount):
        transaction = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'category': category,
            'amount': amount
        }
        self.transactions.append(transaction)
        print("\nTransaction added successfully!")
        
    def calculate_budget(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = total_income - total_expenses
        return balance, total_income, total_expenses
    
    def show_transactions(self):
        if not self.transactions:
            print("\nNo transactions found!")
            return
            
        print("\n{:<20} {:<10} {:<15} {:<10}".format('Date', 'Type', 'Category', 'Amount'))
        print("-" * 55)
        for transaction in self.transactions:
            print("{:<20} {:<10} {:<15} ${:<10.2f}".format(
                transaction['date'],
                transaction['type'].title(),
                transaction['category'].title(),
                transaction['amount']
            ))
    
    def get_valid_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than 0!")
                    continue
                return amount
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def run(self):
        while True:
            print("\n=== Budget Tracker ===")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Current Budget")
            print("4. View Transaction History")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                category = input("Enter income category (e.g., Salary, Gift): ")
                amount = self.get_valid_amount("Enter income amount: $")
                self.add_transaction('income', category, amount)
                
            elif choice == '2':
                category = input("Enter expense category (e.g., Food, Rent): ")
                amount = self.get_valid_amount("Enter expense amount: $")
                self.add_transaction('expense', category, amount)
                
            elif choice == '3':
                balance, income, expenses = self.calculate_budget()
                print("\n=== Current Budget ===")
                print(f"Income: ${income:.2f}")
                print(f"Expenses: ${expenses:.2f}")
                print(f"Balance: ${balance:.2f}")
                
            elif choice == '4':
                print("\n=== Transaction History ===")
                self.show_transactions()
                
            elif choice == '5':
                print("\nExiting Budget Tracker. Goodbye!")
                break
                
            else:
                print("\nInvalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()