#  pattern
  
rows = 5 
for i in range(rows): 
  for j in range(i+1): 
   print("* ", end="") 
print("\n")

# 

n = 5 
for i in range(0, n): 
  for j in range(n-i): 
    print("*", end=" ") 
print()

#  
rows = 5 
for i in range(rows): 
    for j in range(i+1): 
        print(j+1, end=" ") 
    print("\n") 
    
    #
rows = 5 
 
for i in range(rows, 0, -1): 
    for j in range(0, i): 
        print("* ", end=" ") 
     
    print("\n") 
    
      #
      
for i in range(rows, 0, -1): 
    for j in range(1, i+1): 
        print(j, end=" ") 
     
    print("\n") 
    
    # 
    
    rows = 5 
 
for i in range(rows, 1, -1): 
    for space in range(0, rows-i): 
        print("  ", end="") 
    for j in range(i, 2*i-1): 
        print("* ", end="") 
    for j in range(1, i-1): 
        print("* ", end="") 
    print()
    
    # 
    
    a = 8 
for i in range(0, 5): 
    for j in range(0, a): 
        print(end=" ") 
    a = a - 2 
    for j in range(0, i+1): 
        print("* ", end="") 
    print()
    
