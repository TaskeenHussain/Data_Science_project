#Subject of the python programme
#Author by: Taskeen Hussain
#Contact: taskeenuaf@gmail.com, github link
#Step1: why to use singgle quotation? 
#print('Taskeen Hussain') #When we are writing a string
#print("What's up?")

#step2: When to use "" double quotation?
#print("Taskeen") 
#print("What's up?") #when writing strings and making use of other quotation marks

#Step3: When to use ''' tripple quotation mark?
#print(''''
      
#      ''')# tripple quotation mark is used when we have to more than 2 lines of code
#Assignment:When to use comments in python? Mention 10 study cases.


import random

def get_weather_data():
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Windy', 'Snowy']
    temperatures = [32, 50, 60, 70, 80]

    return {
        'condition': random.choice(weather_conditions),
        'temperature': random.choice(temperatures),
        'humidity': random.randint(20, 100),
        'wind_speed': random.randint(0, 20)
    }

def display_weather():
    weather = get_weather_data()
    print("=== Weather Forecast ===")
    print(f"Condition: {weather['condition']}")
    print(f"Temperature: {weather['temperature']}°F")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/h")
    print("========================")

if __name__ == "__main__":
    display_weather()
