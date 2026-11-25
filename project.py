class BankATM:
    def __init__(self, owner, start_bal=10000, user_pin="1234"):
        self.owner = owner
        self.__bal = float(start_bal)
        self.__last_bal = float(start_bal)
        self.__pin = str(user_pin)
        self.__txns = ["Account started with Rs." + format(self.__bal, ".2f")]

    def check_pin(self, pin_try):
        return pin_try == self.__pin

    def view_bal(self):
        print("\n=== Account Balance ===")
        print("Holder:", self.owner)
        print("Current Balance: Rs." + format(self.__bal, ".2f"))
        print("Previous Balance: Rs." + format(self.__last_bal, ".2f"))
        print("=======================\n")
        self.__txns.append("Viewed balance: Rs." + format(self.__bal, ".2f"))

    def add_money(self, amt):
        if amt <= 0:
            print("Enter a positive amount.\n")
            return
        self.__last_bal = self.__bal
        self.__bal = self.__bal + amt
        self.__txns.append(
            f"Added Rs.{amt:.2f} | Prev: Rs.{self.__last_bal:.2f} -> Curr: Rs.{self.__bal:.2f}"
        )
        print("Deposited Rs." + format(amt, ".2f"))
        print("Previous Balance: Rs." + format(self.__last_bal, ".2f"))
        print("Current Balance: Rs." + format(self.__bal, ".2f") + "\n")

    def take_money(self, amt):
        if amt <= 0:
            print("Enter a positive amount.\n")
            return
        if amt > self.__bal:
            print("Not enough balance. Available: Rs." + format(self.__bal, ".2f") + "\n")
            return
        self.__last_bal = self.__bal
        self.__bal = self.__bal - amt
        self.__txns.append(
            f"Withdrew Rs.{amt:.2f} | Prev: Rs.{self.__last_bal:.2f} -> Curr: Rs.{self.__bal:.2f}"
        )
        print("Withdrew Rs." + format(amt, ".2f"))
        print("Previous Balance: Rs." + format(self.__last_bal, ".2f"))
        print("Current Balance: Rs." + format(self.__bal, ".2f") + "\n")

    def update_pin(self, old_p, new_p):
        if not self.check_pin(old_p):
            print("Current PIN is wrong.\n")
            return False
        if not (new_p.isdigit() and len(new_p) == 4):
            print("New PIN must be 4 digits.\n")
            return False
        if new_p == self.__pin:
            print("New PIN is same as old PIN.\n")
            return False
        self.__pin = new_p
        self.__txns.append("PIN changed")
        print("PIN changed successfully.\n")
        return True

    def history(self):
        print("\n--- Transactions ---")
        n = 1
        for t in self.__txns:
            print(str(n) + ". " + t)
            n = n + 1
        print("--------------------\n")


def pin_screen(machine):
    left = 3
    print("\nWelcome, " + machine.owner)
    while left > 0:
        entered = input("Enter PIN: ").strip()
        if machine.check_pin(entered):
            print("PIN verified.\n")
            return True
        left = left - 1
        print("Wrong PIN. Attempts left:", left)
    print("Card locked.\n")
    return False


def run():
    my_atm = BankATM("Hari", 10000, "1234")
    if not pin_screen(my_atm):
        return

    while True:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        opt = input("Select option: ").strip()

        if opt == "1":
            my_atm.view_bal()
        elif opt == "2":
            try:
                x = float(input("Enter deposit amount: "))
                my_atm.add_money(x)
            except ValueError:
                print("Please type a number.\n")
        elif opt == "3":
            try:
                x = float(input("Enter withdraw amount: "))
                my_atm.take_money(x)
            except ValueError:
                print("Please type a number.\n")
        elif opt == "4":
            p1 = input("Enter old PIN: ").strip()
            p2 = input("Enter new 4-digit PIN: ").strip()
            if my_atm.update_pin(p1, p2):
                print("Enter new PIN to continue:")
                if not pin_screen(my_atm):
                    return
        elif opt == "5":
            my_atm.history()
        elif opt == "6":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice.\n")


run()