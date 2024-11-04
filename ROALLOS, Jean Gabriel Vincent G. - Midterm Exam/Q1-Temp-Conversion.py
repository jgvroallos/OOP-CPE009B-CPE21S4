def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    # C to F Conversion
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    # F to C Conversion [Added Process]
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return ((self._temp - 32) * 5) / 9

    # C to K Conversion
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    # K to C Conversion [Added Process]
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15
    
    # prompt to convert C to K
    tempInCelsius = float(input("Enter the temperature in Celsius (convert to K): "))

    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")

    # prompt to convert C to F
    tempInCelsius = float(input("Enter the temperature in Celsius (convert to F): "))

    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    # prompt to convert K to C
    tempInCelsius = float(input("Enter the temperature in Kelvin (convert to C): "))

    convert = KelvinToCelsius(tempInCelsius)
    print(str(convert.conversion()) + " Celsius")

    # prompt to convert F to C 
    tempInCelsius = float(input("Enter the temperature in Fahrenheit (convert to C): "))

    convert = FahrenheitToCelsius(tempInCelsius)
    print(str(convert.conversion()) + " Celsius")

# initialize program
main()
