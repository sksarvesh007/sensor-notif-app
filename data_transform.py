import pandas as pd
import datetime

file_path = 'data.csv'  
data = pd.read_csv(file_path)

start_time = datetime.datetime.strptime("09:00", "%H:%M")
start_date = datetime.date(2024, 6, 20)

date_list = []
time_list = []

time_increment = datetime.timedelta(seconds=180)  
current_time = start_time
current_date = start_date

for i in range(len(data)):
    if current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:  
        current_date += datetime.timedelta(days=1)  

    date_list.append(current_date)
    time_list.append(current_time.time())
    current_time += time_increment

data['Date'] = date_list
data['Time'] = time_list
data = data.drop(columns=['Pump Data' , 'Soil Moisture'])
updated_file_path = 'updated_data.csv' 
data.to_csv(updated_file_path, index=False)