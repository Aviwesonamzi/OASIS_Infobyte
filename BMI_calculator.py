# asking for input from the users  
the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  

BMI=the_weight/(the_height*the_height)
print("BMI Calculated is:  ",BMI)
 
# printing the BMI  
print("Your Body Mass Index is", BMI)  
# using the if-elif-else conditions  
if BMI <= 18.5:  
    print("You are underweight.")  
elif BMI <= 24.9:  
    print("You are healthy.")  
elif BMI <= 29.9:  
    the_print("You are over weight.")  
else:  
    print("You are obese.")
