def BMI():
    print("Welcome to BMI Calculator!\nDo you prefer to enter your height and weight in US units (feet/pounds) or in Metric Units (cms/kg)?")
    units = input("Press U or M : ")
    
    
    if units == "U":
        height_fi = list(map(int, input("Enter your height in feet & inches\nEg: 5 4: ").split()))
        feet, inches = height_fi[0], height_fi[1]
        metre = ((inches + (feet*12)) * 2.54)/100
        print(f"Height(m) : {metre:.2f}") 

        weight_lbs = int(input("Enter your weight in pounds (lbs) : "))
        kilo = weight_lbs * 0.453592
        print(f"Weight(kg) : {kilo:.2f}")

        bmi = kilo/(metre ** 2)

        print(f"Your BMI (Body Mass Index) : {bmi:.2f} kg/m^2)")
        
        

    elif units == "M":
        height_cm = int(input("Enter your height in cm : "))
        metre = height_cm/100
        print(f"Height (m) : {metre:.2f}")

        weight = int(input("Enter your weight in kg : "))
        print(f"Weight (kg) : {weight:.2f}")

        bmi = weight/(metre ** 2)

        print(f"Your BMI (Body Mass Index) : {bmi:.2f} kg/m^2)")

    if bmi < 18.5:
        print("Underweight")
    elif (bmi >= 18.5 and bmi <= 24.9):
        print("Normal Weight")
    elif (bmi >= 25 and bmi <= 29.9):
        print("Over Weight")
    elif (bmi >= 30 and bmi <= 34.9):
        print("Obesity (Class I)")
    elif (bmi >= 35 and bmi <= 39.9):
        print("Obesity (Class II)")
    elif bmi > 40:
        print("Obesity (Class III)")

    
BMI()


