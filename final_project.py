import time

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
# /033 is formatting for ANSI which is use for color

# ==========================================================
#  CONTEXT MANAGER — Logs start/end of every conversion
# ==========================================================
class ConversionLogger:
    def __enter__(self):
        print(CYAN + "\nStarting conversion..." + RESET)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb): #Python always gives them to the method when the with block ends
        if exc_type:
            print(RED + "An error occurred during conversion!" + RESET)
        else:
            print(GREEN + "Conversion completed successfully." + RESET)
        return False
    


class HistoryIterator:
    def __init__(self, history_list):
        self.history = history_list
        self.index = 0



    def __iter__(self): #tells Python this object can be looped over (like a list).
        return self

    def __next__(self):
        
        if self.index >= len(self.history):
            raise StopIteration
        value = self.history[self.index]
        self.index += 1
        return value

# Iterator → manual version
# Generator → automatic version using yield

def loading():
    print(CYAN + "Converting", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print(RESET)


history = []


print(r"""
 _   _       _                          _   _   _       _ _     _____                           _            
| | | |     (_)                        | | | | | |     (_) |   /  __ \                         | |           
| | | |_ __  ___   _____ _ __ ___  __ _| | | | | |_ __  _| |_  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
| | | | '_ \| \ \ / / _ \ '__/ __|/ _` | | | | | | '_ \| | __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |_| | | | | |\ V /  __/ |  \__ \ (_| | | | |_| | | | | | |_  | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
 \___/|_| |_|_| \_/ \___|_|  |___/\__,_|_|  \___/|_| |_|_|\__|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                                                      
""")

running = True


while running:
    print(CYAN + "\nSelect the unit you want to convert from:" + RESET)
    print("1. Meter (m)                 2. Kilometer (km)       3. Centimeter (cm)     4. Millimeter (mm)    5. Mile (mi)")
    print("5. Mile (mi)                 6. Kilogram (kg)        7. Gram (g)            8. Milligram (mg)     9. Pound (lb)")
    print("10. Ounce (oz)               11. Celsius (°C)        12. Fahrenheit (°F)    13. Kelvin (K)        14. Liter (L)")
    print("15. Milliliter (mL)          16. Second (s)          17. Minute (min)       18. Hour (h)          19. Meter/second (m/s)")
    print("20. Kilometer/hour (km/h)    21. Miles/hour (mph)    22. View History       23. Exit")


    from_unit = input("\nEnter your choice (1–23): ")

    # Error handling
    if not from_unit.isdigit() or int(from_unit) < 1 or int(from_unit) > 23:
        print(RED + "Please select a number from 1–23." + RESET)
        input("Press Enter to return to the menu...")
        continue

    if from_unit == "23":
        print(GREEN + "Goodbye!" + RESET)
        break

    # View history
    if from_unit == "22":
        print(YELLOW + "\n--- Conversion History ---" + RESET)

        try:
            if len(history) == 0:
                print("No conversions yet.")
            else:
                for item in HistoryIterator(history):
                    print(item)

        except Exception:
            print(RED + "Error reading history!" + RESET)

        input("\nPress Enter to continue...")
        continue


    

    # Valid unit names
    unit_names = {
        "1": "meters", 
        "2": "kilometers", 
        "3": "centimeters",
        "4": "millimeters", 
        "5": "miles",
        "6": "kilograms", 
        "7": "grams", 
        "8": "milligrams",
        "9": "pounds", 
        "10": "ounces",
        "11": "Celsius", 
        "12": "Fahrenheit", 
        "13": "Kelvin",
        "14": "liters",
        "15": "milliliters",
        "16": "seconds", 
        "17": "minutes", 
        "18": "hours",
        "19": "meters/second", 
        "20": "kilometers/hour", 
        "21": "miles/hour"
    }

    # Handle input errors
    value_input = input(f"Enter the value (no fractions!) --> ({unit_names[from_unit]}): ")

    if not value_input.strip():
        print(RED + "Please enter a valid number." + RESET)
        input("Press Enter to return to the menu...")
        continue

    try:
        value = float(value_input)
    except:
        print(RED + "Invalid number!" + RESET)
        input("Press Enter to continue...")
        continue

    # Show target units based on category (same as your original logic)
    categories = {
        "1": ["1", "2", "3", "4", "5"],
        "2": ["1", "2", "3", "4", "5"],
        "3": ["1", "2", "3", "4", "5"],
        "4": ["1", "2", "3", "4", "5"],
        "5": ["1", "2", "3", "4", "5"],
        "6": ["6", "7", "8", "9", "10"],
        "7": ["6", "7", "8", "9", "10"],
        "8": ["6", "7", "8", "9", "10"],
        "9": ["6", "7", "8", "9", "10"],
        "10": ["6", "7", "8", "9", "10"],
        "11": ["11", "12", "13"],
        "12": ["11", "12", "13"],
        "13": ["11", "12", "13"],
        "14": ["14", "15"],
        "15": ["14", "15"],
        "16": ["16", "17", "18"],
        "17": ["16", "17", "18"],
        "18": ["16", "17", "18"],
        "19": ["19", "20", "21"],
        "20": ["19", "20", "21"],
        "21": ["19", "20", "21"]
    }

    # Display valid options
    print("\nConvert TO:")
    for u in categories[from_unit]:
        print(f"{u}. {unit_names[u]}")

    to_unit = input("Enter your target unit number: ")

    if to_unit not in categories[from_unit]:
        print(RED + "Invalid target unit!" + RESET)
        input("Press Enter...")
        continue


    loading()



    with ConversionLogger():
        try:
            result = 0
            unit_name = unit_names[to_unit]

            # LENGTH
            if from_unit in ["1", "2", "3", "4", "5"]:
                base = value * {
                    "1": 1, "2": 1000, "3": 0.01, "4": 0.001, "5": 1609.34
                }[from_unit]
                result = base / {
                    "1": 1, "2": 1000, "3": 0.01, "4": 0.001, "5": 1609.34
                }[to_unit]

            # WEIGHT
            elif from_unit in ["6", "7", "8", "9", "10"]:
                base = value * {
                    "6": 1, "7": 0.001, "8": 0.000001, "9": 0.453592, "10": 0.0283495
                }[from_unit]
                result = base / {
                    "6": 1, "7": 0.001, "8": 0.000001, "9": 0.453592, "10": 0.0283495
                }[to_unit]

            # TEMPERATURE
            elif from_unit in ["11", "12", "13"]:
                if from_unit == "11":
                    base = value
                elif from_unit == "12":
                    base = (value - 32) * 5/9
                elif from_unit == "13":
                    base = value - 273.15

                if to_unit == "11":
                    result = base
                elif to_unit == "12":
                    result = base * 9/5 + 32
                elif to_unit == "13":
                    result = base + 273.15

            # VOLUME
            elif from_unit in ["14", "15"]:
                base = value * {"14": 1, "15": 0.001}[from_unit]
                result = base / {"14": 1, "15": 0.001}[to_unit]

            # TIME
            elif from_unit in ["16", "17", "18"]:
                base = value * {"16": 1, "17": 60, "18": 3600}[from_unit]
                result = base / {"16": 1, "17": 60, "18": 3600}[to_unit]

            # SPEED
            elif from_unit in ["19", "20", "21"]:
                base = value * {"19": 1, "20": 0.277778, "21": 0.44704}[from_unit]
                result = base / {"19": 1, "20": 0.277778, "21": 0.44704}[to_unit]

            print(GREEN + f"\nResult: {result} {unit_name}" + RESET)

            history.append(
                f"{value} {unit_names[from_unit]} → {result} {unit_names[to_unit]}"
            )

        except KeyError:
            print(RED + "Conversion error: invalid unit key!" + RESET)

        except ZeroDivisionError:
            print(RED + "Math error: division by zero!" + RESET)

        except Exception as e:
            print(RED + f"Unexpected conversion error: {e}" + RESET)
