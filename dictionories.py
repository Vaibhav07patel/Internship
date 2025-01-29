thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
print(thisdict)

# print dictionaries 

thisdict = { 
"brand": "Ford", 
"electric": False, 
"year": 1964, 
"colors": ["red", "white", "blue"] 
} 
print(thisdict)
# print models

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict["model"] 
print(x)
# print keys

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict.keys() 
print(x)

# keys adding
car = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = car.keys() 
print(x) #before the change 
car["color"] = "white" 
print(x) #after the change 

# print values

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict.values() 
print(x) 

# thisdict = 
{ 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict.items() 
print(x)

# 

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
if "model" in thisdict: 
 print("Yes, 'model' is one of the keys in the thisdict dictionary")
 
#   change dictionary iteams

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict["year"] = 2018 
print(thisdict)

# add dictionary items
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict["color"] = "red" 
print(thisdict) 

#  remove dictionary items
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict.pop("model") 
print(thisdict)
#  loop

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict: 
 print(thisdict[x]) 
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict.values(): 
  print(x) 

# 
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict.keys(): 
 print(x) 
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x, y in thisdict.items(): 
 print(x, y)
 
