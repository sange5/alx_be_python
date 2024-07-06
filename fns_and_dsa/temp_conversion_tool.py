# Define global conversion factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  
  
def convert_to_celsius(fahrenheit):  
    """  
    Convert Fahrenheit to Celsius  
    """  
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  
  
def convert_to_fahrenheit(celsius):  
    """  
    Convert Celsius to Fahrenheit  
    """  
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  
  
def main():  
    # Prompt user for temperature and unit  
    temperature = input("Enter the temperature to convert: ")  
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")  
  
    # Validate user input  
    try:  
        temperature = float(temperature)  
    except ValueError:  
        raise ValueError("Invalid temperature. Please enter a numeric value.")  
  
    # Perform conversion based on user input  
    if unit.upper() == 'C':  
        result = convert_to_fahrenheit(temperature)  
        print(f"{temperature}°C is {result}°F")  
    elif unit.upper() == 'F':  
        result = convert_to_celsius(temperature)  
        print(f"{temperature}°F is {result}°C")  
    else:  
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")  
  
if __name__ == "__main__":  
    main()  
