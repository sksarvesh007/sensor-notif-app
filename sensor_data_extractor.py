import machine
import utime
import dht
import uos

# Configure the sensor data pin
DATA_PIN = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

# Create an instance of the DHT22 sensor
sensor = dht.DHT22(DATA_PIN)

# Open (or create) a CSV file to save the data
file_name = "sensor_data.csv"

# Write headers to the CSV file
with open(file_name, 'w') as file:
    file.write("Time,Temperature(°C),Humidity(%)\n")

def read_and_save_data():
    # Function to read and save data from the DHT22 sensor
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        current_time = utime.localtime()
        formatted_time = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
        
        # Write the data to the CSV file
        with open(file_name, 'a') as file:
            file.write("{},{:.2f},{:.2f}\n".format(formatted_time, temp, humidity))
        
        # Print the data to the console
        print("{:<10} {:<15.2f} {:<15.2f}".format(formatted_time, temp, humidity))
        
    except Exception as e:
        print("Error reading sensor data:", e)

# Print headers to the console
print("{:<10} {:<15} {:<15}".format("Time", "Temperature(°C)", "Humidity(%)"))

# Main loop
while True:
    read_and_save_data()
    utime.sleep(1)  # Wait for 1 second before reading the data again
