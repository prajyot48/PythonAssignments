def analyze_temperatures(temperature_readings):
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    max_temp = max(temperature_readings)
    min_temp = min(temperature_readings)
    print("Average Temperature:", avg_temp)
    print("Highest Temperature:", max_temp)
    print("Lowest Temperature:", min_temp)
temperature_readings = [25, 28, 21, 24, 27]
analyze_temperatures(temperature_readings)
