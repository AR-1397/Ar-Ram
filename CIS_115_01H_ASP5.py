#Amber Roberson
#09/24/2019
#CIS 115 01H - Error Code


#Receive the amount
amount = float(input("Enter the amount: ")) #NonType logic error - Replaced 'print'

#Convert to cents
changedAmount = int(amount*100)

#Dollars
numDollars = changedAmount//100 #Out of order
changedAmount = changedAmount%100 

#Quarters
numQuarters = changedAmount//25 #Out of order / MATH Error - 'changedAmount/25'
changedAmount = changedAmount%25 # Syntax - lower case error in 'changedAmount' / MATH Error - 'changedAmount*25'

#Dimes
numDimes = changedAmount//10 #Out of order / NameType 'angedAmount'
changedAmount = changedAmount%10

#Nickels
numNickels = changedAmount//5 #Out of order / NameType 'angedAmount'
ChangedAmount = changedAmount%5 #Syntax error - cases error 'ChangedAmount'

#Pennies
numPennies = changedAmount

#Output
print("For $", amount, "consists of: \n\t", numDollars, "dollars \n\t", numQuarters, "quarters \n\t", numDimes, "dimes \n\t", numNickels, "nickels \n\t", numPennies, "pennies") # Syntax error

'''
^
line 32 column 83-100
Syntax error - missing comma after 'numDimes'
Syntax error - spacing between '\n\ t" '
Syntax error - NameType errors for 'chnumDimes' & 'chnumNickles
'''
