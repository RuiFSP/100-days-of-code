import pandas

FUR_COLOR = 'Primary Fur Color'

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# count the primary color squirrels
# build a dataframe with that summary statistics


data_fur_color_cleaned = data[FUR_COLOR].dropna()

# count data
count_gray = len(data_fur_color_cleaned[data[FUR_COLOR] == "Gray"])
count_cinnamon = len(data_fur_color_cleaned[data[FUR_COLOR] == "Cinnamon"])
count_black = len(data_fur_color_cleaned[data[FUR_COLOR] == "Black"])

# construct dataframe

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count")
