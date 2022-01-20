class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 69000")

    def withdrawl(self,amount):
        new_amount = 69000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("Card No.:- ")
    pin_number  = input("Pin:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Check Your Balance   2.withdrawl")
    activity = int(input("Choose Activity :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter The Amount:- "))
        new_user.withdrawl(amount)
    else:
        print("Enter A Vaild Pin")


if __name__ == "__main__":
    main()