def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


temperature = 20
print(f"{temperature} C = {celsius_to_fahrenheit(temperature):.1f} F")
