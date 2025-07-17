class atm:
    def __init__(self,balance=0):
        self.balance=balance

    def check_balance(self):
        print(f"Your balance is: ${self.balance}") 

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} doposit sucessfully")
            
        else:
            print("invalid amount")

def main():
    ATM=atm(balance=1000)

    while True:
        print("1.Check balance")
        print("2.deposit")
        print("3.Exit")

        choice=input("Enter the Choice (0-3):")

        if choice=='1':
            ATM.check_balance()

        elif choice=='2':
            try:
                amount=float(input("Enter your doposit: $"))
                ATM.deposit(amount)
            except ValueError:
                print("Please enter valid number")
        elif choice=='3':
            print("THANK YOU!!!")
        else:
            print("Choice between (1-3)")

if __name__=="__main__":
    main()            



        


            





































