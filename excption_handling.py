
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went wrong")
    
    
    x = 5 
    
    if x < 0:
        raise Exception("Sorry, no numbers below zero")