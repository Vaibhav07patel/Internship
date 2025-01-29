thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
mydict = thisdict.copy() 
print(mydict) 

# Nested dictionaries

myfamily = { 
"child1" : { 
"name" : "Email", 
"year" : 2004 
}, 
"child2" : { 
"name" : "vaibhav", 
"year" : 2001 
}, 
"child3" : { 
 "name" : "Linus", 
"year" : 2011 
} 
} 
print(myfamily) 

# python if else 
a = 33 
b = 200 
if b > a: 
 print("b is greater than a") 
a = 33 
b = 33 
if b > a: 
 print("b is greater than a") 
elif a == b: 
 print("a and b are equal") 
 
#  short hand if else
a = 330 
b = 330 
print("A") if a > b else print("=") if a == b else print("B")

# nested if

x = 41 
if x > 10: 
  print("Above ten,") 
if x > 20: 
 print("and also above 20!") 
else: 
 print("but not above 20.")
 
#   nested loops

adj = ["red", "big", "tasty"] 
fruits = ["apple", "banana", "cherry"] 
for x in adj: 
 for y in fruits: 
  print(x, y)
  
   
  
    
