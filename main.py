import random

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Stormy"]

city = input("Enter your city: ")
forecast = random.choice(weather_conditions)
print(f"The weather in {city} is: {forecast}")
