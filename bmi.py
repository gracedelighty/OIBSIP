print("BMI calculator")
the_height = float(input("Enter the height (cm): "))
the_weight = float(input("Enter the weight (kg): "))

the_BMI = the_weight / (the_height/100)**2

print("Your Body Mass Index is", the_BMI)

if the_BMI <= 18.5:
    print("Oops! You are underweight.")
elif the_BMI <= 24.9:
    print("Awesome! You are healthy and normal.")
elif the_BMI <= 29.9:
    the_print("Eee! You are overweight.")
else:
    print("Seesh! You are obese.")