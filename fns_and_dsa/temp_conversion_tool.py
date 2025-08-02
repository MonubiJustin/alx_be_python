CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        if choice == 'C':
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        elif choice == 'F':
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        else:
            print("Invalid choice. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == '__main__':
    main()
