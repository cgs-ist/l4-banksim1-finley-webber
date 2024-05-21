# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'
accountCookie = 0
running = True

class Account():
    def __init__(self, accountName, accountBalance, accountPassword):
        self.accountName = accountName
        self.accountBalance = accountBalance
        self.accountPassword = accountPassword
    
    def showBalance(self):
        print(self.accountBalance)
    
    def makeDeposit(self):
        deposit = input("How much money would you like to deposit? ")
        if (checkStringForChar(deposit)):
            print("Invalid Deposit")
        else:
            deposit = (int)(deposit)
            if deposit < 0:
                print("Invalid deposit")
            else:
                self.accountBalance += deposit

    def makeWithdrawal(self):
        withdrawal = input("How much money would you like to withdraw? ")
        if (checkStringForChar(withdrawal)):
            print("Invalid Withdrawal")
        else:
            withdrawal = (int)(withdrawal)
            if withdrawal < 0 or self.accountBalance - withdrawal < 0:
                print("Invalid Withdrawal")
            else:
                self.accountBalance -= withdrawal
                print("Withdrawal Accepted!")
                
    def showAccount(self):
        print("-----------------")
        print("Name: " + self.accountName)
        print("Balance: " + str(self.accountBalance))
        print("Account Password: " + self.accountPassword)
        print("-----------------")


JoeAccount = Account(accountName, accountBalance, accountPassword)

def choice(letter):
    match letter:
        case 'b':
            JoeAccount.showBalance()
        case 'd':
            JoeAccount.makeDeposit()
        case 'w':
            JoeAccount.makeWithdrawal()
        case 's':
            JoeAccount.showAccount()
        case 'q':
            global running
            running = False
            
    

def checkStringForChar(string):
    for x in string:
        if x.isalpha():
            return True
    return False

while running:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #
    action = action[0]
    
    if accountCookie != 1:
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            accountCookie = 1
            choice(action)
    else:
        choice(action)