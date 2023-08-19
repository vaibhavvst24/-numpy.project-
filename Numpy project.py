import numpy as np
#represent the data in the numpy array
data =[ 
[       
    #november
    
     {"month": "November", "week": "week1", "day": "monday", "data":[15,31]},
     {"month": "November", "week": "week1", "day":"tuesday", "data":[6,25]},
     {"month": "November", "week": "week1", "day":"wednesday","data":[14,23]},
     {"month": "November", "week": "week1", "day":"thrusday","data":[13,32]},
     {"month": "November", "week": "week1", "day":"friday","data":[13,20]},
     {"month": "November", "week": "week1", "day":"saturday","data":[9,22]},
     {"month": "November", "week": "week1", "day":"sunday","data":[8,26]},
     
     {"month": "November", "week": "week2", "day":"monday", "data":[15,21]},
     {"month": "November", "week": "week2", "day":"tuesday", "data":[10,26]},
     {"month": "November", "week": "week2", "day":"wednesday", "data":[14,32]},
     {"month": "November", "week": "week2", "day":"thrusday", "data":[-13,27]},
     {"month": "November", "week": "week2", "day":"friday", "data":[10,26]},
     {"month": "November", "week": "week2", "day":"saturday", "data":[7,28]},
     {"month": "November", "week": "week2", "day":"sunday", "data":[10,23]},

     {"month": "November", "week":"week3", "day":"monday", "data":[14,24]},
     {"month": "November", "week":"week3", "day":"tuesday", "data":[14,26]},
     {"month": "November", "week":"week3", "day":"wednesday", "data":[15,27]},
     {"month": "November", "week":"week3", "day":"thrusday", "data":[13,25]},
     {"month": "November", "week":"week3", "day":"friday", "data":[9,22]},
     {"month": "November", "week":"week3", "day":"saturday", "data":[11,29]},
     {"month": "November", "week":"week3", "day":"sunday", "data":[12,23]},
     
     {"month":"November", "week":"week4", "day":"monday", "data":[15,20]},
     {"month":"November", "week":"week4", "day":"tuesday", "data":[8,26]},
     {"month":"November", "week":"week4", "day":"wednesday", "data":[10,31]},
     {"month":"November", "week":"week4", "day":"thrusday", "data":[10,32]},
     {"month":"November", "week":"week4", "day":"friday", "data":[11,30]},
     {"month":"November", "week":"week4", "day":"saturday", "data":[8,23]},
     {"month":"November", "week":"week4", "day":"sunday", "data":[12,22]},
],
    #DECEMBER
[
     {"month": "December", "week":"week1", "day":"monday", "data":[15,31]},
     {"month": "December", "week":"week1", "day":"tuesday", "data":[6,20]},
     {"month": "December", "week":"week1", "day":"wednesday", "data":[11,23]},
     {"month": "December", "week":"week1", "day":"thrusday", "data":[15,24]},
     {"month": "December", "week":"week1", "day":"friday", "data":[6,21]},
     {"month": "December", "week":"week1", "day":"saturday", "data":[6,29]},
     {"month": "December", "week":"week1", "day":"sunday", "data":[12,26]},

     {"month": "December", "week":"week2", "day":"monday", "data":[10,24]},
     {"month": "December", "week":"week2", "day":"tuesday", "data":[8,22]},
     {"month": "December", "week":"week2", "day":"wednesday", "data":[15,21]},
     {"month": "December", "week":"week2", "day":"thrusday", "data":[10,24]},
     {"month": "December", "week":"week2", "day":"friday", "data":[15,32]},
     {"month": "December", "week":"week2", "day":"saturday", "data":[14,30]},
     {"month": "December", "week":"week2", "day":"sunday", "data":[12,21]},
     
     {"month": "December", "week":"week3", "day":"monday", "data":[15,26]},
     {"month": "December", "week":"week3", "day":"tuesday", "data":[9,27]},
     {"month": "December", "week":"week3", "day":"wednesday", "data":[14,22]},
     {"month": "December", "week":"week3", "day":"thrusday", "data":[15,30]},
     {"month": "December", "week":"week3", "day":"friday", "data":[15,21]},
     {"month": "December", "week":"week3", "day":"saturday", "data":[7,23]},
     {"month": "December", "week":"week3", "day":"sunday", "data":[15,29]},
    
     {"month":"December", "week":"week4", "day":"monday", "data":[8,25]},
     {"month":"December", "week":"week4", "day":"tuesday", "data":[8,23]},
     {"month":"December", "week":"week4", "day":"wednesday", "data":[6,27]},
     {"month":"December", "week":"week4", "day":"thrusday", "data":[15,21]},
     {"month":"December", "week":"week4", "day":"friday", "data":[10,21]},
     {"month":"December", "week":"week4", "day":"saturday", "data":[11,26]},
     {"month":"December", "week":"week4", "day":"sunday", "data":[6,23]}
],
    #JANUARY
[
     {"month":"January", "week":"week1", "day":"monday", "data":[4,20]},
     {"month":"January", "week":"week1", "day":"tuesday", "data":[7,19]},
     {"month":"January", "week":"week1", "day":"wednesday", "data":[2,21]},
     {"month":"January", "week":"week1", "day":"thrusday", "data":[5,18]},
     {"month":"January", "week":"week1", "day":"friday", "data":[8,18]},
     {"month":"January", "week":"week1", "day":"saturday", "data":[2,4]},
     {"month":"January", "week":"week1", "day":"sunday", "data":[18,6]},
    
     {"month":"January", "week":"week2","day":"monday", "data":[2,22]},
     {"month":"January", "week":"week2","day":"tuesday", "data":[5,21]},
     {"month":"January", "week":"week2","day":"wednesday", "data":[6,18]},
     {"month":"January", "week":"week2","day":"thrusday", "data":[7,22]},
     {"month":"January", "week":"week2","day":"friday", "data":[7,21]},
     {"month":"January", "week":"week2","day":"saturday", "data":[7,5]},
     {"month":"January", "week":"week2","day":"sunday", "data":[18,2]},
    
     {"month":"January", "week":"week3", "day":"monday", "data":[4,22]},
     {"month":"January", "week":"week3", "day":"tuesday", "data":[5,20]},
     {"month":"January", "week":"week3", "day":"wednesday", "data":[5,18]},
     {"month":"January", "week":"week3", "day":"thrusday", "data":[4,18]},
     {"month":"January", "week":"week3", "day":"friday", "data":[3,21]},
     {"month":"January", "week":"week3", "day":"saturday", "data":[6,7]},
     {"month":"January", "week":"week3", "day":"sunday", "data":[21,8]},
    
     {"month":"January", "week":"week4", "day":"monday", "data":[7,19]},
     {"month":"January", "week":"week4", "day":"tuesday", "data":[5,19]},
     {"month":"January", "week":"week4", "day":"wednesday", "data":[4,18]},
     {"month":"January", "week":"week4", "day": "thrusday", "data":[8,22]},
     {"month":"January", "week":"week4", "day":"friday", "data":[6,20]},
     {"month":"January", "week":"week4", "day":"saturday", "data":[8,8]},
     {"month":"January", "week":"week4", "day":"sunday", "data":[20,6]}
],
    #FEBRUARY
[
     {"month":"February", "week":"week1", "day":"monday", "data":[9,18]},
     {"month":"February", "week":"week1", "day":"tuesday", "data":[8,19]},
     {"month":"February", "week":"week1", "day":"wednesday", "data":[-10,22]},
     {"month":"February", "week":"week1", "day":"thrusday", "data":[10,22]},
     {"month":"February", "week":"week1", "day":"friday", "data":[8,20]},
     {"month":"February", "week":"week1", "day":"saturday", "data":[9,71]},
     {"month":"February", "week":"week1", "day":"sunday", "data":[22,9]},
    
     {"month":"February", "week":"week2", "day":"monday", "data":[7,20]},
     {"month":"February", "week":"week2", "day":"tuesday", "data":[8,20]},
     {"month":"February", "week":"week2", "day":"wednesday", "data":[12,19]},
     {"month":"February", "week":"week2", "day":"thrusday", "data":[10,19,]},
     {"month":"February", "week":"week2", "day":"friday", "data":[10,19]},
     {"month":"February", "week":"week2", "day":"saturday", "data":[8,8]},
     {"month":"February", "week":"week2", "day":"sunday", "data":[19,10]},

     {"month":"February", "week":"week3", "day":"monday", "data":[12,22]},
     {"month":"February", "week":"week3", "day":"tuesday", "data":[8,19]},
     {"month":"February", "week":"week3", "day":"wednesday", "data":[10,22]},
     {"month":"February", "week":"week3", "day":"thrusday", "data":[11,19]},
     {"month":"February", "week":"week3", "day":"friday", "data":[12,20]},
     {"month":"February", "week":"week3", "day":"saturday", "data":[10,11]},
     {"month":"February", "week":"week3", "day":"sunday", "data":[19,10]},

    {"month":"February", "week":"week4", "day":"monday", "data":[12,20]},
    {"month":"February", "week":"week4", "day":"tuesday", "data":[8,22]},
    {"month":"February", "week":"week4", "day":"wednesday", "data":[7,19]},
    {"month":"February", "week":"week4", "day":"thrusday", "data":[11,20]},
    {"month":"February", "week":"week4", "day":"friday", "data":[7,21]},
    {"month":"February", "week":"week4", "day":"saturday", "data":[9,10]},
    {"month":"February", "week":"week4", "day":"sunday", "data":[21,12]}
],    
]

# Create a structured array dtype
dtype = [('month', 'U10'), ('week', 'U10'), ('day', 'U10'), ('data', '2int')]

# Create an empty structured array
data_array = np.empty(sum(len(month_data) for month_data in data), dtype=dtype)

# Populate the structured array
index = 0
for month_data in data:
    for entry in month_data:
        data_array[index] = (entry["month"], entry["week"], entry["day"], tuple(entry["data"]))
        index += 1

# Accessing the data
print(data_array)

current_month = data_array[0]["month"]
print(data_array[0])
for entry in data_array[1:]:
    if entry["month"] != current_month:
        print()  # Print a blank line between months
        current_month = entry["month"]
    print(entry,"\n")

temperature_array = np.array([
    entry['data'] for month_data in data for entry in month_data
])
print(temperature_array)

#dimension and shape of array
arr = np.array([[4,4,7,min,max]])
print("\nThe Dimension and Shape of array:",arr.shape,"\n")

#daily temperature of the first week of month
first_week_temperatures = temperature_array[:, 0]
print("Daily Temperatures for the First Week of Each Month:")
print(first_week_temperatures,"\n")

# Access the temperatures for Tuesday (second day) across all weeks and months
import numpy as np

# Convert data to a structured NumPy array
dtype = [('month', 'U20'), ('week', 'U20'), ('day', 'U20'), ('data', '2int')]
temperature_array = np.array([tuple(day.values()) for month in data for day in month], dtype=dtype)

# Access the temperatures for Tuesday across all weeks and months
tuesday_temperatures = temperature_array[(temperature_array['day'] == 'tuesday')]['data']
print("Temperatures for Tuesday Across All Weeks and Months: \n")
print(tuesday_temperatures,"\n")

# Filter and access the maximum temperatures for weekdays (Monday to Friday) of December and February
dec_feb_weekday_max_temperatures = temperature_array[
    np.logical_and.reduce([
        temperature_array['month'] == 'December',
        temperature_array['day'] != 'saturday',  # Exclude Saturday
        temperature_array['day'] != 'sunday'     # Exclude Sunday
    ])
]['data'][:, 1]  # Extract maximum temperature values
print("Maximum Temperatures for Weekdays (Mon-Fri) of December and February:")
print(dec_feb_weekday_max_temperatures)

# Filter and access the days in November when minimum temperature was less than 8 degrees
nov_days_min_less_than_8 = temperature_array[
    np.logical_and.reduce([
        temperature_array['month'] == 'November',
        temperature_array['data'][:, 0] < 8  # Minimum temperature less than 8 degrees
    ])
]
print("\nDays in November with Minimum Temperature Less than 8 degrees: \n",nov_days_min_less_than_8)
for entry in nov_days_min_less_than_8:
    print(f"\nWeek {entry['week']}, {entry['day']}, Min Temp: {entry['data'][0]}")
    print(entry)

# Threshold temperature
threshold_temp = 20

# Filter and access the weeks in December and January where maximum temperature crossed the threshold
dec_jan_weeks_above_threshold = np.unique(temperature_array[
    np.logical_and.reduce([
        np.isin(temperature_array['month'], ['December', 'January']),
        temperature_array['data'][:, 1] > threshold_temp  # Maximum temperature above threshold
    ])
]['week'])

print("\nWeeks in December and January with Maximum Temperature above 20 degrees:")
print(dec_jan_weeks_above_threshold)

# Filter and identify absurd temperature values
# Define a reasonable temperature range (in degrees Celsius)
min_temp_range = -30
max_temp_range = 50

absurd_temperatures = temperature_array[
    np.logical_or.reduce([
        temperature_array['data'][:, 0] < min_temp_range,  # Minimum temperature below range
        temperature_array['data'][:, 0] > max_temp_range,  # Minimum temperature above range
        temperature_array['data'][:, 1] < min_temp_range,  # Maximum temperature below range
        temperature_array['data'][:, 1] > max_temp_range   # Maximum temperature above range
    ])
]

if absurd_temperatures.shape[0] == 0:
    print("No absurd temperature values found in the dataset.")
else:
    print("\nAbsurd Temperature Values:")
    for entry in absurd_temperatures:
        print(f"Month: {entry['month']}, Week: {entry['week']}, Day: {entry['day']}, Min Temp: {entry['data'][0]}, Max Temp: {entry['data'][1]}\n")

# Calculate z-scores for both minimum and maximum temperatures
z_scores_min = (temperature_array['data'][:, 0] - np.mean(temperature_array['data'][:, 0])) / np.std(temperature_array['data'][:, 0])
z_scores_max = (temperature_array['data'][:, 1] - np.mean(temperature_array['data'][:, 1])) / np.std(temperature_array['data'][:, 1])

# Define a threshold for considering values as outliers (e.g., z-score above 3)
z_score_threshold = 3

# Find indexes of outlier values (both minimum and maximum temperatures)
outlier_indexes_min = np.where(np.abs(z_scores_min) > z_score_threshold)[0]
outlier_indexes_max = np.where(np.abs(z_scores_max) > z_score_threshold)[0]

print("Indexes of Outlier Values (Minimum Temperatures): \n", outlier_indexes_min)
print("Indexes of Outlier Values (Maximum Temperatures): \n", outlier_indexes_max)

# Replace outlier values with the median of the respective temperature
median_min_temp = np.median(temperature_array['data'][:, 0])
median_max_temp = np.median(temperature_array['data'][:, 1])

temperature_array['data'][:, 0][np.abs(z_scores_min) > z_score_threshold] = median_min_temp
temperature_array['data'][:, 1][np.abs(z_scores_max) > z_score_threshold] = median_max_temp

# Print the replaced values for verification
for entry in temperature_array:
    print(f"\nMonth: {entry['month']}, Week: {entry['week']}, Day: {entry['day']}, Replaced Min Temp: {entry['data'][0]}, Replaced Max Temp: {entry['data'][1]}")
    print(entry)

# Filter data for winter months (December, January, and February) in Jaipur
winter_months = ['December', 'January', 'February']
jaipur_winter_temps = temperature_array[
    np.logical_and.reduce([
        np.isin(temperature_array['month'], winter_months),
        np.isin(temperature_array['week'], ['week1', 'week2', 'week3', 'week4']),  # Assuming all weeks are winter weeks
        temperature_array['day'] != 'saturday',  # Exclude Saturday
        temperature_array['day'] != 'sunday'     # Exclude Sunday
    ])
]

# Calculate the average maximum temperature for winter months in Jaipur
avg_max_temp = np.mean(jaipur_winter_temps['data'][:, 1])
print("\nAverage Max Temperature for Winter Months in Jaipur:", avg_max_temp)

# Filter data for the month of December in Jaipur
december_temps_jaipur = temperature_array[
    np.logical_and.reduce([
        temperature_array['month'] == 'December',
        temperature_array['week'] != 'week5'  # Assuming there are only 4 weeks in December
    ])
]

# Calculate the weekly average minimum temperature for December in Jaipur
weekly_avg_min_temp = []
current_week = None
week_temps = []

for entry in december_temps_jaipur:
    if current_week is None:
        current_week = entry['week']
    if entry['week'] != current_week:
        weekly_avg_min_temp.append((current_week, np.mean(week_temps)))
        week_temps = []
        current_week = entry['week']
    week_temps.append(entry['data'][0])

# Print the weekly average minimum temperatures for December in Jaipur
print("\nWeekly Average Minimum Temperatures for December in Jaipur:")
for week, avg_temp in weekly_avg_min_temp:
    print(f"Week {week}: {avg_temp:.2f}")

#filter the overall avg temp for the months Dec and Jan
dec_jan_temps = temperature_array[
    np.logical_or.reduce([
        temperature_array['month'] == 'December',
        temperature_array['month'] == 'January'
    ])
]

# Calculate the overall average temperature for December and January
overall_avg_temp = np.mean(dec_jan_temps['data'])
print("\nOverall Average Temperature for December and January:", overall_avg_temp)

# Find the least temperature and corresponding date
least_temp_index = np.argmin(dec_jan_temps['data'][:, 0])  # Index of least temperature
least_temp = dec_jan_temps['data'][least_temp_index, 0]    # Least temperature
least_temp_day = dec_jan_temps['day'][least_temp_index]    # Day of the week
least_temp_week = dec_jan_temps['week'][least_temp_index]  # Week of the month
least_temp_month = dec_jan_temps['month'][least_temp_index]  # Month

print("\nLeast Temperature:", least_temp)
print("Date (Day/Week/Month):", least_temp_day, least_temp_week, least_temp_month)

# Filter data for the month of February
feb_temps = temperature_array[temperature_array['month'] == 'February']

# Find the maximum temperature and corresponding date
max_temp_index = np.argmax(feb_temps['data'][:, 1])  # Index of maximum temperature
max_temp = feb_temps['data'][max_temp_index, 1]      # Maximum temperature
max_temp_day = feb_temps['day'][max_temp_index]      # Day of the week
max_temp_week = feb_temps['week'][max_temp_index]    # Week of the month
max_temp_month = feb_temps['month'][max_temp_index]  # Month

print("\nMaximum Temperature:", max_temp)
print("Date (Day/Week/Month):", max_temp_day, max_temp_week, max_temp_month)

# Filter data for the month of February
nov_temps = temperature_array[temperature_array['month'] == 'November']

# Calculate the average maximum temperature for November
avg_max_temp_nov = np.mean(nov_temps['data'][:, 1])

# Find days where the max temp dropped below the average max temp of the month
days_below_avg = nov_temps[nov_temps['data'][:, 1] < avg_max_temp_nov]

# Print the days where max temp dropped below the average max temp
print("\nDays in November where Max Temp dropped below Avg Max Temp:")
for entry in days_below_avg:
    print(f"Date (Day/Week): {entry['day']}/{entry['week']}, Max Temp: {entry['data'][1]}, Avg Max Temp: {avg_max_temp_nov:.2f}")

# Create a dictionary to organize weeks by month
organized_data = {}

# Group weeks by month
for entry in temperature_array:
    month = entry['month']
    if month not in organized_data:
        organized_data[month] = []
    organized_data[month].append(entry)

# Create an organized array with rows having weeks of the same month
organized_array = []
for month in organized_data:
    organized_array.append(organized_data[month])

# Convert organized array to NumPy array
organized_array = np.array(organized_array)

# Print the organized array
for row in organized_array:
    for entry in row:
        print("\norganised week by month:",entry)

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Convert data to a structured NumPy array
dtype = [('month', 'U20'), ('week', 'U20'), ('day', 'U20'), ('data', '2int')]
temperature_array_celsius = np.array([tuple(day.values()) for month in data for day in month], dtype=dtype)

# Convert Celsius temperatures to Fahrenheit
temperature_array_fahrenheit = temperature_array_celsius.copy()
temperature_array_fahrenheit['data'] = celsius_to_fahrenheit(temperature_array_celsius['data'])

# Create a dictionary to organize weeks by month
organized_data_fahrenheit = {}

# Group weeks by month
for entry in temperature_array_fahrenheit:
    month = entry['month']
    if month not in organized_data_fahrenheit:
        organized_data_fahrenheit[month] = []
    organized_data_fahrenheit[month].append(entry)

# Create an organized array with rows having weeks of the same month
organized_array_fahrenheit = []
for month in organized_data_fahrenheit:
    organized_array_fahrenheit.append(organized_data_fahrenheit[month])

# Convert organized array to NumPy array
organized_array_fahrenheit = np.array(organized_array_fahrenheit)

# Print the organized array in Fahrenheit
for row in organized_array_fahrenheit:
    for entry in row:
        print("\nArray in Faherenheit: ",entry)

# Filter data for the month of December
dec_temps = temperature_array[temperature_array['month'] == 'December']

# Calculate the weekly average temperatures for December
weekly_avg_temps = {}
for entry in dec_temps:
    if entry['week'] not in weekly_avg_temps:
        weekly_avg_temps[entry['week']] = []
    weekly_avg_temps[entry['week']].append(entry['data'][1])  # Max temperature

for week in weekly_avg_temps:
    weekly_avg_temps[week] = np.mean(weekly_avg_temps[week])

# Sort the data in descending order based on weekly average for December
sorted_dec_data = sorted(dec_temps, key=lambda x: weekly_avg_temps[x['week']], reverse=True)

# Print the sorted data
for entry in sorted_dec_data:
    print("\nweekly average temperature for december:\n",entry)
    
# Filter data for the winter months (December, January, February)
winter_temps = temperature_array[
    np.logical_or.reduce([
        temperature_array['month'] == 'December',
        temperature_array['month'] == 'January',
        temperature_array['month'] == 'February'
    ])
]

# Filter data for the first three days of each month
first_three_days = winter_temps[
    np.logical_or.reduce([
        np.logical_and(winter_temps['month'] == 'December', np.arange(1, len(winter_temps) + 1) <= 3),
        np.logical_and(winter_temps['month'] == 'January', np.arange(1, len(winter_temps) + 1) <= 3),
        np.logical_and(winter_temps['month'] == 'February', np.arange(1, len(winter_temps) + 1) <= 3)
    ])
]

# Calculate the overall average temperature for the entire winter
overall_avg_temp = np.mean(winter_temps['data'][:, 1])

# Sort the data in descending order based on overall average for the whole winter
sorted_data = sorted(first_three_days, key=lambda x: overall_avg_temp - x['data'][1], reverse=True)

# Print the sorted data
for entry in sorted_data:
    print("\ndata for the winter month:",entry)
    
# Calculate the difference between min and max temperatures for each day
temperature_diffs = []
for entry in winter_temps:
    temp_diff = entry['data'][1] - entry['data'][0]
    temperature_diffs.append(temp_diff)

# Convert temperature differences to a NumPy array
temperature_diffs_array = np.array(temperature_diffs)

# Print the temperature differences array
print("\nTemperature Differences Array:")
print(temperature_diffs_array)

# Create a dictionary to store temperature differences by month
temp_diff_by_month = {}

# Calculate the difference between max temps of consecutive days for each month
for entry in winter_temps:
    month = entry['month']
    if month not in temp_diff_by_month:
        temp_diff_by_month[month] = []

    # Find the index of the entry for the previous day
    prev_day_index = np.where(winter_temps['week'] == entry['week'])[0][0] - 1
    
    # Check if the previous day index is valid
    if prev_day_index >= 0:
        temp_diff = abs(entry['data'][1] - winter_temps[prev_day_index]['data'][1])
        temp_diff_by_month[month].append(temp_diff)

# Convert temperature differences to a NumPy array
temp_diff_array = np.array([(month, np.mean(temp_diff_by_month[month])) for month in temp_diff_by_month],
                           dtype=[('month', 'U20'), ('avg_temp_diff', 'float')])

# Print the temperature difference array
print("\nTemperature Difference Array for month:")
print(temp_diff_array)

# Create a dictionary to store temperature differences by day
temp_diff_by_day = {}

# Calculate the difference between min and max temps for each day
for entry in winter_temps:
    day = entry['day']
    if day not in temp_diff_by_day:
        temp_diff_by_day[day] = []
    
    temp_diff = abs(entry['data'][1] - entry['data'][0])
    temp_diff_by_day[day].append(temp_diff)

# Convert temperature differences to a NumPy array
temp_diff_array = np.array([(day, np.mean(temp_diff_by_day[day])) for day in temp_diff_by_day],
                           dtype=[('day', 'U20'), ('avg_temp_diff', 'float')])

# Print the temperature difference array
print("\nTemperature Difference Array for day:")
print(temp_diff_array)