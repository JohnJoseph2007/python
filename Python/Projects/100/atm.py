import random

numberinput = input("Enter Card number: ")
pininput = input("Enter Card PIN number: ")

class ATM:
    def __init__(self, pin, card):
        self.pin = pin
        self.card = card
        self.anon = ""
        self.bal = random.randrange(100000, 5000000, 1)

    def anonymous(self):
        card = str(self.card)
        reverse = card[::-1]
        indletterlist = []
        for i in range(0, 4):
          indletterlist.append(reverse[i])
        conc = ''.join(indletterlist)
        rconc = conc[::-1]
        anonstring = f"XXXX XXXX XXXX {rconc}"
        print(anonstring)
        self.anon = anonstring
    
    def cashwithdrawal(self, amt):
      print(f"Hi there, user of Card Number \"{self.anon}\".")
      print(f"Successfully withdrew amount of {amt} from account.")
      print(f"Balance before withdrawal: {self.bal}")
      print(f"New balance: {self.bal-amt}")

    def BalanceEnquiry(self):
      print(f"Balance: {self.bal}")

lol = ATM(pininput, numberinput)
lol.anonymous()
lol.cashwithdrawal(12000)
lol.BalanceEnquiry()