#Roberson
#11/20/2019
#Practice problems - Loops

#Problem one - Square root


num = int(input("Enter an interger greater than 2: "))      #Assign num variable
num0 = 0
while num < 2:                                              #Start while loop
    print("Invalid input, Please try again!")
    num = int(input("Enter an interger greater than 2: "))  #Data vailidation
while num > 2 or num0 == num:
    sqrt = num**(1/2)
    num = sqrt
    num0 += 1
    print(num0,":",round(num, 3))                           #Round answer
print("Done")

#Problem two - Data validation

y = float(input("Enter the value for y: "))             #Y variable
z = float(input("Enter the value for z: "))             #Z variable
count = 0
while z == -3 and count < 3:                            #Start while loop
    print("Division by zero error, please try again!")  #Print error
    z = float(input("Enter the value for z: "))         #Reassign Z
x = (y-2)/(3*z)                                         #Z will work
print(x)                                
print("Done")

#Problem three - Factors

count = 0                               #Count counter
num = int(input("Enter an interger: ")) #Input num 
x = 1
while x < num :                         #Start while loop
    if num%x == 0:                      #If statement
        count += 1                      #Count increase
        print(x)                        #Print x
    x+=1                                #X increase

if count == 2:                          #If statement (Prime number)
    print("Prime number")
     
#Problem four - guessing game

import random    #Import random

count = 1        #Count variable
again = "yes"    #Again variable

while again == "yes":                                               #Start while
    secret = random.randint(0, 10)                                  #random num
    guess = int(input("Enter a number guess between 0 and 10: "))   #Input guess
    while secret != guess:                                          #While guess is not secret
        if guess < secret:                                          #Less than
            count += 1
            print("Too low")
            guess = int(input("Enter guess: "))                     #Reassign num
        if guess > secret:                                          #Greater than
            count += 1
            print("Too high")
            guess = int(input("Enter guess: "))                     #Reassign num
    print("Congrats! You got it correct!")                          #Correct num
    again = input("Enter yes to go again: ")                        #Play again option
    again = again.lower()                                           #Change again variable input to lower case 

if count <= 3:                                                      #If statement for count variable
    print("Count is", count,"Extra congrats!")

#Problem 5 - multiplication table (Nested loops)

num = 144                           #Num equals 144
for row in range(1, 11):            #For loop for rows 
    for column in range(1, 11):     #For loop for columns
        multp = row * column        #Repeat num for rows and columns
        print(multp, end = "\t")    #Print multp and tab
    print()                         #Repeat to next row 






































