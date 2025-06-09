import requests
import matplotlib.pyplot as plt

# Get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(f"Status code for {city}: {response.status_code}")
    return response.json()

# Extract temperature and condition
def pick_weather(data):
    temp = data['main']['temp']
    condition = data['weather'][0]['description']
    return temp, condition

def main():
    api_key = "56ef1e192234f7c16d7d7f88a3a1a528"  # <--- Replace this with your real API key

    # Add your favorite cities here
    cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']

    temps = []
    conditions = []

    for city in cities:
        data = get_weather(city, api_key)
        temp, condition = pick_weather(data)
        print(f"Weather in {city}")
        print(f"Temperature: {temp} °C")
        print(f"Condition: {condition}\n")
        temps.append(temp)
        conditions.append(condition)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(cities, temps, color='skyblue')
    plt.title("Temperature in Indian Cities")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
