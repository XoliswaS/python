
# Create a shopping cart programme that will contionously ask the user fora food product and the price of the product
# Have an exist clause if the user wishes to stop adding morethings to their cart 
# At the end show the food iteams and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a foood to buy or press to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the of the {food}: R"))
        foods.append(food)
        prices.append(price)
            
    print("----- YOUR CART -----")
        
    for food in foods:
        print(food, end= " ")
            
        for price in prices:
            total +=price
           
    print("\n")        
    print(f"Your total is: R{total}")