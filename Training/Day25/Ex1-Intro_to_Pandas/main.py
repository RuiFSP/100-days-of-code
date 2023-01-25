# # worst approach
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for row in data:
#         data_stripped = row.strip()
#         print(data_stripped)
#
# # second approach: using csv
# import csv
#
# with open("weather_data.csv") as data_file1:
#     data1 = csv.reader(data_file1)
#     temperature = []
#     for row in data1:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# best approach : using pandas
import pandas
from statistics import mean

data = pandas.read_csv("weather_data.csv")
# # data frame  the whole table
# print(type(data["temp"]))  # series -> equivalent to a list

# data.to_dict converts to dict
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# you do not have to do this, take advanatge of pandas series
#
# avg_temp_list = sum(temp_list) / len(temp_list)
# avg_temp_list1 = mean(temp_list)
#
# print(avg_temp_list)
# print(avg_temp_list1)

# #pandas method mean
# print(f"The is the average temperature: {data['temp'].mean()}")
# print(f"The is the max temperature: {data['temp'].max()}")
# print(f"The is the min temperature: {data['temp'].min()}")
#
# #alternative way to call column data, by .name vs ['name']
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])

# get the data row where temp is max
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


# get temp for on ºf
def convert_to_fahrenheit(temperature):
    return 9 / 5 * temperature + 32


print(monday.temp.apply(convert_to_fahrenheit))
print(int(monday.temp) * 9 / 5 + 32)

# create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
