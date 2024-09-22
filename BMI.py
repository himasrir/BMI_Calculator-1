def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    # Determine BMI category
    if bmi < 18.5:
        return "Underweight: It's important to eat a balanced diet and consult a healthcare provider."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight: Keep up the good work with a balanced diet and regular exercise!"
    elif 25 <= bmi < 29.9:
        return "Overweight: Consider incorporating more physical activity and healthier food choices."
    else:
        return "Obesity: It's advisable to consult with a healthcare provider for guidance on a healthier lifestyle."

def main():
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    # Get category suggestion
    suggestion = bmi_category(bmi)
    print(suggestion)

if __name__ == "__main__":
    main()
