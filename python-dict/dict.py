from collections import defaultdict



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

res_list = defaultdict(list)
res_int = defaultdict(int)
res_string = defaultdict(str)

res_list["hello"].append("world")
res_int["hello"] = 5
res_string["hello"] = "mars"
print(res_list, "LIST")
print(res_int, "INT")
print(res_string, "STRING")


strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list) # dict of lists for values


for words in strs: # loop through array 
    res["".join(sorted(words))].append(words) #create key of each sorted word and append word.
    #if key already exists the sorted word will append to corresponding key
    # if key does not exist, the key will be created and append the word to its sorted version
    # return the values (LISTS) of all the keys
    print(res)
print(res.values())