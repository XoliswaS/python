#Loop Control Statements 

fruits = {"apples", "banana", "cherry", "date"}

for fruit in fruits:
    if fruit == "cherry":
        break #exist the loop if cherry is found 
    print(fruit)
    
    
    for fruit in fruits:
        if fruit == "cherry":
         continue #skips cherry and movesto the next iteration 
    print(fruit)
    
    for fruit in fruits:
        if fruit == "cherry":
            pass #a placeholder , no action is needed 
        print(fruit)
        