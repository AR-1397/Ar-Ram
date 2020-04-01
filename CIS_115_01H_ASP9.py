#Roberson
#10/29/2019
#CIS 115 01H
#Practice problems

#Problem 1

#Import random module
import random

#Define HeadsTails from user input
HeadsTails = float(input("Enter a 1 or 0:" ))

#Turn HeadsTails to random number variable
HeadsTails = random.randint(0, 1)

#Start if statement
#Condition is heads
if HeadsTails == 0:
    #Print heads
    print("Heads!")
#Condition is tails
elif HeadsTails == 1:
    #Print tails
    print("Tails!")
#Condition if not correct input
else:
    #print error 
    print("Invalid input.")


#Problem 2 - Subtraction Game

#Assign 2 random numbers 
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

#Display 2 random numbers
print(n1)
print(n2)

#User input the gues
n3 = float(input("Enter the answer: "))

#Start if statement
#Condition 1 - n1 >= 5 and n2 <= 5
if n1 >= 5 and n2 <= 5:
    #If condition is met, then subtract n1 & n2
    n3 = (n1 - n2)
    #Print statement
    print("Congrats! You guess the correct answer.")
    print(n3)

#Condition 2 - n1 <= 5 and n2 >= 5
elif n1 <= 5 and n2 >= 5:
    #If condition is met, then subtract n2 & n1
    n3 = (n2 - n1)
    #Print statement
    print("Congrats! You guess the correct answer.")
    print(n3)

#End if Statement w/ else error
else:
    print("You did not guess the correct answer")
    print("The correct answer is", n3)


#Program 3 - Divide by zero

#User input to assign y & z variables
y = float(input("Enter the Y variable: "))
z = float(input("Enter the Z variable: "))

#Start if statement
#Condition 1 - division by zero
if z == 0:
    #Print error
    print("Division by zero error.")

#End if statement w/ forula & answer 
else:
    x = (7*y)/(3*z)
    print(x)


#Program 4 - Government

#Assign age & years of citizen using user input
Age = float(input("Enter your age: "))
YearsCitizen = float(input("Enter how long you have been a citizen of the US: "))

#Condition 1 - age & years of citizen for senate
if Age >= 30 and YearsCitizen >= 9:
    #Print of eligiblity
    print("Eligible for US Senate application.")
#Condition 2 - age & years of citizen for representative 
elif Age >= 25 and YearsCitizen >= 7:
    print("Eligible for US Representative application.")
#End statement w/ ineligibility
else:
    #print statement
    print("Sorry, you do not qualify to run for either US", end=" ")
    print("Representative or US Senate.")


   
#Program 5 - Magic 8 Ball!

#Random answer
Answer = random.randint(0, 7)

#Input question from user input 
Question = input("Ask me a question, any question?: ")

#Start if statement
#conditions 0-6 will output different answers regardless of question
if Answer == 0:
    print("It is certain")
elif Answer == 1:
    print("Reply hazy, please try again.")
elif Answer == 2:
    print("Don't count on it.")
elif Answer == 3:
    print("It is decidedly so.")
elif Answer == 4:
    print("Ask again later.")
elif Answer == 5:
    print("My reply is no.")
elif Answer == 6:
    print("Most likely.")
elif Answer == 7:
    print("Yes - definitely!")

#Problem 6 - Currency Conversion

#Conversion rate for USD and Euros
#Conversion should be 0.735
ExchangeRate = float(input("Enter the exchange rate from US dollars to Euros: "))

#USD or Euro from user input
Currency = input("Enter USA convert from United States Dollars to Euros and Euro for vice versa:")

#Currency amount that is to be converted
Amount = float(input("Enter the dollar amount: "))

#Error message for else statement
Err = "Invalid input"

#Start if statement
#Currency = USD
if Currency == "USA" or ExchangeRate == "0.735":
    #Multiplying ExchangeRate with Amount for USD conversion
    ExchangeAmount = Amount*ExchangeRate
    print("$",Amount ,"is", ExchangeAmount,"euros") # <- Print statement
#Start elif statement
#Currency = Euros
elif Currency == "Euros" or ExchangeRate == "0.735":
    #Dividing Amount with ExchangeRate for Euro conversion
    ExchangeAmount = Amount/ExchangeRate
    #Print statement
    print(Amount, "Euros is", "$", ExchangeAmount)
#Start else statement
#Print error message 
else:
    print(Err)






















