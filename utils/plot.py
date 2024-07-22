# utils/plot.py
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def create_plot(weather):
    times = [datetime.strptime(ts, '%Y-%m-%dT%H:%M') for ts in weather['hourly']['time']]
    temperatures = weather['hourly']['temperature_2m']

    # Create figure and plot data
    plt.figure(figsize=(12, 6))
    plt.plot(times, temperatures, marker='o')

    # Set x-axis locator and formatter
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Show all points
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # Format time as hours and minutes

    # Create a list of all days between start and end times
    start_time = times[0]
    end_time = times[-1]
    day_range = [start_time + timedelta(days=x) for x in range((end_time - start_time).days + 1)]

    # Add ticks for the start of each day
    plt.gca().set_xticks(day_range)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.title('Hourly Temperature Forecast')
    plt.grid(False)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return base64.b64encode(buf.getvalue()).decode('utf-8')

