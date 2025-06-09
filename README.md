# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SOUMYA RAI

*INTERN ID*: CT06DN45

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

As part of my internship project at Codtech, I was assigned a task to demonstrate my ability to integrate with a public API and visualize the retrieved data using Python. The specific instructions were to use any public API (e.g., OpenWeatherMap), fetch real-time data, and create visual representations of that data using libraries such as Matplotlib or Seaborn. The final deliverables required for this task included a working Python script and a clean, informative visualization dashboard.

**Objective and Planning**
The objective of this task was to practice and showcase real-world API integration and data visualization skills. I chose the OpenWeatherMap API, which provides real-time weather data for cities around the world. My idea was to build a weather dashboard that displays the current temperature of multiple Indian cities using a bar chart. I selected five major Indian cities: Delhi, Mumbai, Bangalore, Chennai, and Kolkata.

Before starting the implementation, I planned the entire flow of the script:

1. Register for and retrieve an API key from OpenWeatherMap.

2. Use the requests library in Python to fetch weather data for each city.

3. Parse the JSON responses to extract relevant information (temperature and weather condition).

4. Store this data in appropriate variables.

5. Use matplotlib.pyplot to generate a clean and visually appealing bar chart of the temperatures.

**Tools and Technologies Used**
Python 3 – The core programming language used for the entire script.

OpenWeatherMap API – The public API I integrated with to get live weather data.

Requests library – Used to make HTTP requests to the API endpoint.

Matplotlib – Used for plotting the temperature data in a visual bar chart format.

VS Code and Terminal – My development environment and command-line tool to run the script.

**Development and Execution**
First, I signed up on the OpenWeatherMap website and obtained my unique API key. Then, I installed the required Python libraries using pip commands in the terminal:
pip install requests matplotlib

Next, I created a Python script where I defined a function to send requests to the API endpoint for each city. The API returned a JSON response containing weather details, from which I extracted the temperature and description of the weather conditions.

To handle errors like invalid API keys or wrong city names, I added error-checking code that checks the API response and prints useful messages in case of failure (e.g., status code 401 for unauthorized access).

Once I had successfully retrieved temperature data for all five cities, I used Matplotlib to plot the data as a bar chart. Each bar represented a city, and the height of the bar represented the current temperature in that city (in Celsius). I customized the chart with a title, axis labels, colors, and grid lines to make it easy to understand and visually appealing.

I tested the script thoroughly to ensure that the data was fetched correctly and that the chart displayed accurate and updated information. I also included screenshots of the output as part of the deliverables.

**Outcome**
The final output was a fully functional Python script that:

Connects to the OpenWeatherMap API

Retrieves weather data for multiple cities

Parses and processes the data

Visualizes the data in a well-labeled, professional-looking bar chart

The project helped me understand the end-to-end flow of working with REST APIs and representing real-time data visually. It also gave me hands-on experience with libraries like Requests and Matplotlib.

**Conclusion**
This task gave me a solid foundation in API integration and basic data visualization using Python. It fulfilled all the internship requirements, and I now feel more confident in working with real-world data and building dashboards. It was an enriching and practical experience that aligned well with my learning goals and the internship objectives.

