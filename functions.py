def my_function(): 
 print("Hello from a function")
my_function()

# 
def my_function(fname): 
 print(fname + " Refsnes") 
my_function("Email") 
my_function("Vaibhav") 
my_function("Linus")

#arbitrary arguments,*args
def my_function(*kids): 
 print("The youngest child is " + kids[2]) 
my_function("ved", "mihir", "sid")  

#  Arbitrary Keyword Arguments, **kwargs 
def my_function(**kid): 
 print("His last name is " + kid["lname"]) 
my_function(fname = "Vaibhav", lname = "patel")
