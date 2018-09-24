ERROR_MESSAGE = "User did not input a number."

try:
    degrees_celsius = int(input("Temperature in C? "))
    degrees_fahrenheit = degrees_celsius * 1.8 + 32
    print("%.1f F" % degrees_fahrenheit)
except:
    print(ERROR_MESSAGE)
