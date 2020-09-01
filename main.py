# Author: Alex Koretke ajk6357@psu.edu
# Collaborator: Riwk Sen sbs6426@psu.edu
# Collaborator: Kyle Funck kjf5474@psu.edu
# Collaborator: Hannah Johnson hlj5107@psu.edu



temperature = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")

if unit == "F" or unit == "f":
  fahrenheit = temperature
  celsius = 5/9*(fahrenheit-32)
  print(f'{fahrenheit}{chr(176)} in Fahrenheit is equivalent to {celsius}{chr(176)} Celsius.')

elif unit == "C" or unit == "c":
  celsius = temperature
  fahrenheit = (9/5*celsius + 32)
  print(f'{celsius}{chr(176)} in Celsius is equivalent to {fahrenheit}{chr(176)} Fahrenheit.')

else:
  print(f"Invalid unit({unit}).")