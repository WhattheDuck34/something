import random

def detect_blood_in_water(person_name, min_detect=35):
    """
    Simulates detecting blood in water.

    Parameters:
        person_name (str): The name of the person to detect.
        min_detect (float): Minimum blood percentage required to detect.
    """
    blood_percent = random.uniform(0, 100)
    print(f"Detected blood percentage: {blood_percent:.2f}%")

    if blood_percent >= min_detect:
        print(f"Detected: {person_name}")
    else:
        print("No detection.")

name = input("Enter the person's name (default: Jonnathan): ")
if not name:  # If user presses Enter without typing anything
    name = "Jonnathan"

detect_blood_in_water(name)
