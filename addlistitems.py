# change data 
thislist = ["apple", "banana", "cherry"] 
thislist[1:3] = ["watermelon"] 
print(thislist)

thislist = ["apple", "banana", "cherry"] 
tropical = ["mango", "pineapple", "papaya"] 
thislist.extend(tropical) 
print(thislist)
# remeove list items               
thislist = ["apple", "banana", "cherry"]  
thislist.remove("apple") 
print(thislist)

#  Add List Items 
thislist = ["apple", "banana", "cherry"] 
tropical = ["mango", "pineapple", "papaya"] 
thislist.extend(tropical) 
print(thislist)

 # Looping Using List Comprehension
thislist = ["apple", "banana", "cherry" , "vaibhav","sid"] 
for x in thislist: 
    print(x) 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newlist = [] 
for x in fruits: 
  if "a" in x: 
     newlist.append(x) 
print(newlist)  

#  Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newlist = [x for x in fruits if "e" in x] 
print(newlist)

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort() 
print(thislist)

#  Sort Descending 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort(reverse = True) 
print(thislist) 

 # case insensitive sort
thislist = ["Kiwi", "cherry"] 
thislist.sort() 
print(thislist)

#  Reverse Order
thislist = ["vaibhav", "mihir", "sid"] 
thislist.reverse() 
print(thislist)

# Join Two Lists
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3] 
list3 = list1 + list2 
print(list3) 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3] 
for x in list2: 
  list1.append(x)
print(list1)

# list count() method 
fruits = ['banana', 'cherry'] 
x = fruits.count("cherry")