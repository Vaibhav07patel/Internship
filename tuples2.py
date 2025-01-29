# Unpack tuple
fruits = ("apple", "banana", "cherry","orange") 
(green, yellow, *red) = fruits 
print(green) 
print(yellow) 
print(red)

# Loop through a tuple

thistuple = ("apple", "banana", "cherry") 
for x in thistuple: 
 print(x) 
 thistuple = ("apple", "banana", "orange") 
for i in range(len(thistuple)): 
 print(thistuple[i])
 
#  Join two tuplles

tuple1 = ("a", "b" , "c") 
tuple2 = (9, 7, 3) 
tuple3 = tuple1 + tuple2 
print(tuple3)

# Multiply tuples
Brokers = ("IIFL", "dhan", "zerodha") 
mytuple = Brokers * 2 
print(mytuple) 



#  Test
# 1)
list = [1,2,3,4]
print(len(list))

# 2)

b = "Hello,World!" 
print(b[-5:-2]) 

# 3)Print 100 number using loop in list ,number will start from 0
i=0
for i in range (100):
    print(i)
    
#  4) thistuple = (0, "banana", "cherry",”mango”,7,4) 
# Remove 3rd index and print it

thistuple = (0, "banana", "cherry", "mango", 7, 4)

# Create a new tuple without the element at index 3
_newtuple = thistuple[:3] + thistuple[4:]

print(_newtuple)