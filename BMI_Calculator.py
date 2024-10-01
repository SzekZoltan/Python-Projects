def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

name = input("Enter your name: ")

weight = get_float_input("Enter your weight in kg: ")
height = get_float_input("Enter your height in cm: ")

BMI = weight / ((height / 100) ** 2)

if BMI > 0:
    if BMI < 18.5:
        print(f"{name}, you are underweight.")
    elif BMI <= 24.9:
        print(f"{name}, you are normal weight.")
    elif BMI <= 29.9:
        print(f"{name}, you are overweight.")
    elif BMI <= 39.9:
        print(f"{name}, you are obese.")
    else:
        print(f"{name}, you are morbidly obese, you should consult with a doctor.")