Weight = float(input("please enter your weight in Kilograms:"))
Height = float(input("please enter your height in Meters:"))

BMI = Weight/Height

if BMI > 35:
    BodyMass = "EXTREMELY OBESE"

if 30 < BMI < 34.9: 
    BodyMass = "OBESE"

if 25 < BMI < 29.9:
    BodyMass = "OVERWEIGHT"

if 18.5 < BMI < 24.9:
    BodyMass = "NORMAL"

if BMI < 18.5:
    BodyMass = "UNDERWEIGHT"

print(BodyMass)    

