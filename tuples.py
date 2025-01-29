# python tuples
thistuple = ("zerodha", "IIFL") 
print(thistuple)

#  duplicates

thistuple = ("apple", "banana", "cherry","apple","cherry") 
print(thistuple)

#  tuple lenght
thistuple = ("nirav", "sid", "mihir") 
print(len(thistuple)) 

# tuple wiith one item
thistuple = ("vaibhav",) 
print(type(thistuple)) 

#  data types
tuple1 = ("abc", 34, True, 40, "male") 
thistuple = ("apple", "banana", "cherry") 
print(thistuple[1]) 
thistuple = ("apple", "banana", "cherry") 
print(thistuple[-1]) 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") 
print(thistuple[2:5]) 

thistuple = ("apple", "banana", "cherry") 
if "apple" in thistuple: 
    print("Yes, 'apple' is in the fruits tuple")
    
    # Update tuples
x = ("apple", "banana", "cherry") 
y = list(x) 
y[1] = "beeries" 
x = tuple(y) 
print(x) 
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.append("orange") 
thistuple = tuple(y) 

#   Remove items
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.remove("apple") 
thistuple = tuple(y)
thistuple = ("apple", "banana", "cherry") 
del thistuple 
print(thistuple)      # this will raise an error as tuple is not exists.


