def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    bmi2 = f"{bmi:.2f}"  # Corrected formatting

    if bmi < 18.5:
        print(f"Your BMI is {bmi2}. You are Underweight.")
    elif 18.5 <= bmi <= 25.0:
        print(f"Your BMI is {bmi2}. You are Normal Weight.")
    elif bmi > 25.0:
        print(f"Your BMI is {bmi2}. You are Overweight.")

calculate_bmi(weight=57, height=1.73)
