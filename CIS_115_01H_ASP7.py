#Amber Roberson
#10/02/2019
#Test 2 - Practice Problems 2

#Program 1 - (Radians to degrees) 
import math

#Input radians
radians = float(input("Enter the Radians: "))

#Radians to degrees conversion
degrees = (radians*1)*(180/math.pi)

#Output degrees in print
print("The conversion of", radians, "radians is", degrees, "degrees.")


#Program 2 - (Repeating strings)

#Input a number
str1 = input("Enter a number: ")

#Output the number twice 
print(str1 + str1)


#Program 3 - (Net paycheck)

#Input Statements
empname = input("Employee Name: ")
hourswrk = float(input("Hours Worked: "))
payrate = float(input("Pay Rate: "))
fedtax = float(input("Federal tax: "))
statax = float(input("State tax: "))

#Gross pay calculation
grosspay =  hourswrk * payrate

#Federal deduction
fedduc = grosspay * 0.2

#State deduction
statduc = grosspay * 0.09

#Total deductions
deductions = fedduc + statduc

#Total net pay
netpay = grosspay - deductions

#Output Statements
print("Employee Name: ", empname, sep="")
print("Pay Rate: ", hourswrk, sep="")
print("Pay Rate: $", payrate, sep="")
print("Gross Pay: $", grosspay, sep="")
print("Deductions:")
print("\t Federal Withholdings (20.0%): $", fedduc, sep="")
print("\t State Witholdings (9.0%): $", statduc, sep="")
print("\t Total Deductions: $", deductions, sep="")
print("Net Pay: $", netpay, sep="")


#Program 4 - (Quadratic Formula)

#Input Statements for a, b, & c
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))

#D = b^2- 4ac
d = b**2 - 4*a*c

#Square Root d
d = math.sqrt(d)

#Variables for x outputs
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

#Output Statements
print(x1)
print(x2)

