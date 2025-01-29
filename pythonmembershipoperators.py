# Python Membership Operators 
x = ["apple", "banana"] 
print("banana" in x) 
x = ["apple", "banana"] 
print("pineapple" not in x)
# Operator Precedence
print((6 + 3) - (6 + 3))
# python lists 
thislist = ["apple", "banana", "cherry", "apple", "cherry"] 
print(thislist)
thislist = ["apple", "banana", "cherry"] 
print(thislist[1]) 
thislist = ["apple", "banana", "cherry"] 
print(thislist[-1]) 
thislistn= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] 
print(thislist[2:5]) 
thislist = ["apple", "banana", "cherry"] 
if "apple" in thislist: 
  print("Yes, 'apple' is in the fruits list")
  
#   Remove specified index
thislist = ["apple", "banana", "cherry"] 
thislist.pop(1) 
print(thislist) 
thislist = ["apple", "banana", "cherry"] 
del thislist[0] 
print(thislist) 
thislist = ["apple", "banana", "cherry"] 
del thislist