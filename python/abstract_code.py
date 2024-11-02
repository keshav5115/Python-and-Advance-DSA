from abc import ABC, abstractmethod

# Abstract class representing an ATM machine
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass
    
    @abstractmethod
    def enter_pin(self, pin: int):
        pass
    
    @abstractmethod
    def select_transaction(self, transaction_type: str):
        pass
    
    @abstractmethod
    def enter_amount(self, amount: float):
        pass
    
    @abstractmethod
    def dispense_cash(self):
        pass

# Concrete class implementing the ATM interface
class ConcreteATM(ATM):
    def __init__(self):
        self.card_inserted = False
        self.pin_entered = False
        self.balance = 1000.0  # Example balance

    def insert_card(self):
        self.card_inserted = True
        print("Card inserted.")

    def enter_pin(self, pin: int):
        # For simplicity, assume the correct PIN is 1234
        if pin == 1234:
            self.pin_entered = True
            print("PIN verified.")
        else:
            print("Incorrect PIN.")

    def select_transaction(self, transaction_type: str):
        if self.card_inserted and self.pin_entered:
            print(f"Transaction selected: {transaction_type}.")
        else:
            print("Please insert your card and enter your PIN first.")

    def enter_amount(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn. Remaining balance: {self.balance}.")
        else:
            print("Insufficient funds.")

    def dispense_cash(self):
        print("Cash dispensed.")

# Simulating the ATM usage
def main():
    atm = ConcreteATM()
    atm.insert_card()
    atm.enter_pin(1234)  # Correct PIN
    atm.select_transaction("Withdraw")
    atm.enter_amount(200)  # Withdraw $200
    atm.dispense_cash()

main()




'''
Explanation
ATM (Abstract Class): This is an abstract base class with abstract methods representing actions you can perform on an ATM.

ConcreteATM (Concrete Class): This class implements the ATM interface, defining how each action works internally.

Main Function: This simulates the process of using the ATM, where the user can insert their card, enter their PIN, select a transaction, enter an amount, and dispense cash.

Feel free to copy this code into your Python environment to test it out! Let me know if you need further assistance

'''
'''
Abstraction in programming refers to hiding the complex details and showing only the essential features of an object or system. To explain this with a real-time example, let's consider using an ATM machine.

ATM Machine as a Real-Time Example of Abstraction
When you use an ATM to withdraw cash, you are only concerned with a few simple actions:

Inserting your card.
Entering your PIN.
Selecting a transaction type (e.g., withdrawing money).
Entering the amount.
Receiving the money.
What you don’t see (the abstraction part):

You don’t see how the ATM communicates with the bank servers to verify your account balance.
You don’t see how the authentication of your PIN is managed by the bank's security protocols.
You don’t see how the money is deducted from your account in real-time.
You don’t need to know the mechanics of how the ATM machine dispenses the money.
All of these inner workings are abstracted away from you. The ATM machine presents you with a simple interface that hides all the complexities, allowing you to focus on the task you need to accomplish (withdrawing money).

This is exactly how abstraction works in software development: it simplifies interaction with complex systems by providing only the necessary functionality, while hiding the internal details.

'''