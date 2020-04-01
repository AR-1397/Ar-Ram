#Amber Roberson
#CIS_115_01H
#Programming assignment 1


#Program 1
#Print Statement
print("Stay hungry, Stay Foolish. \t-Steve Jobs")

#Program 2
#Input SubTotal and Gratuity Percentage
SubTotal = input("What is the Subtotal?: ")
GratPercent = input("What is the Gratuity Rate? (Input a decimal for the percentage): ")

#Convert SubTotal and Gratuity Percentage to numbers (int and float)
SubTotal = float(SubTotal)
GratPercent = float(GratPercent)

#Multiply SubTotal and GratPercent to calculate Gratuity Rate
GratRate = SubTotal*GratPercent

#Addition of Subtotal & GratRate
GrandTotal = SubTotal+GratRate

#Output the total Gratuity Rate due
print("Your gratuity owed is", GratRate)

#Output the total
print(GrandTotal)


#Program 3
#Input v & A from user
a = input("What is the airplane's acceleration (m/s^2)?: ")
v = input("What is airplane's take-off speed (m/s)?: ")

#Convert v & a to float for use of decimals
a = float(a)
v = float(v)

#Calcuate length by taking v^2 / 2*a
length = (v**2)/(2*a)

#Output length
print("The Length of the runway will be", length, "meters")

#Program 4 - part I
#Input weight(kg) & height(me) from user
weightkg = input("What is the weight in kilograms?: ")
heightme = input("What is the height in meters?: ")

#Convert weight & height to float 
weightkg = float(weightkg)
heightme = float(heightme)

#Calculating BMI
BMI = weightkg/heightme**2

#Output BMI result
print("The BMI is ",BMI)

#Program 2 - part II
#Input weight(lb) & height(in) from user
weightlb = input("What is the weight in Pounds?: ")
heightin = input("What is the height in inches?: ")

#Convert weight & height to float
weightlb = float(weightlb)
heightin = float(heightin)

#Convert weight(lb) to weight(kg)
WeightKgNew = weightlb/2.205

#Convert height(in) to height(me)
HeightMeNew = heightin/39.37

#Calculating BMI
BMI2 = WeightKgNew/HeightMeNew**2

#Output BMI into a sentence
print("The BMI is ",BMI2)






