person = {"name": "Tim", "age": 29, "city": "San Antonio"}

# looping through just accesses keys

for key in person:
    print(key, ":", person[key])

#Important to remember accessing keys is called by using dict name this square brackets with key name inside to get the value
# if a value is already assigned to a key then adding another value to it will replace the current value
# HOWEVER you can add multiple values to a key, MUTABLE
    
person["weight"] = 170
person.update({"height": 6})
print(person)

# Both of the above are valid ways to add to a dict - notice keys were not present prior to adding


key_name = 'city'
if key_name in person.keys():
    print("city name is", person[key_name])
else:
    print("Key not found")