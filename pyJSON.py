#Import json library
import json

#Create the data dictionary
data1 = {
    'name' : 'Linda',
    'age': 27,
    'city' : 'Bothell, WA',
    'interests' : ['Traveling', 'Hiking', 'Puzzles', 'Videogames', 'Music'],
    'is_student': True
}

###############
#Open json file and write the information from the dictionary
with open('data1.json','w') as json_file:
    #Dump the Data Dictionary into the json file
    json.dump(data1, json_file, indent=4)

print("You have successfully written to data1.json")


################
#Open json file and read the data inside
with open('data1.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

################
#Replace information in the dictionary from the jason file referencing the corresponding keys
loaded_data['age'] = 28
loaded_data['interests'].append('Food')

################
#Open jason file and write the changes made to the dictionary

with open('data1.json','w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print("You have successfully re-written to data1.json")