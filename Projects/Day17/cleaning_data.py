# This was not asked, but i want to prepare the data, without manually removing fields as instructor did
# json library si handy to deal with JSON files
import json

my_saved_list = []

# Opening JSON file - this was a copy form the random generated data from web
f = open('trivia_database_clean.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json and building my list of dictionaries
for i in data['results']:
    my_saved_list.append({"text": i['question'], "answer": i['correct_answer']})

# Closing file
f.close()
