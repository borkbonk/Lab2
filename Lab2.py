"""
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
"""
import statistics

def main():
    display_main_menu()
    user_input = get_user_input()
    calc_average(user_input)
    find_min_max(user_input)
    sort_tempereature(user_input)
    calc_median_temperature(user_input)

def display_main_menu():
    print("Enter some numbers separated by commas e.g. 5, 67, 32")

def get_user_input():
    print("get_user_input")
    input_str = input("Enter numbers separated by commas: ")
    input_list = input_str.split(',')
    input_list = [float(num) for num in input_list]
    return input_list

def calc_average(numbers):
    print("calc_average")
    no = len(numbers)
    if no > 0:
        average = sum(numbers) / no
        print("Average:", average)
        return average
    else:
        print("No numbers to calculate the average.")

# Call the main function to start the program


def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    print("Max is", maximum)
    print("Min is", minimum)
    return minimum, maximum




def sort_tempereature(numbers):
    print("sort_temperature")
    sorted(numbers)
def calc_median_temperature(numbers):
    print("calc_median_temperature")
    median=statistics.median(numbers)
    print("Median is", median)
    return median
if __name__ == "__main__":
    main()