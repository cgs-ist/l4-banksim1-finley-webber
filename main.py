# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #
    action = action[0]
    
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)