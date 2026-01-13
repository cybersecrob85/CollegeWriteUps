#Robert Potter, 11/15/2025, Milestone 4

#Welcome message
print("Welcome to the Green Valley Grocery Store!")

#Dictonary to store items and prices
items = {
    "apple": "$0.99",
    "milk": "$3.99",
    "steak": "$10.99",
    "lobster": "$15.00",
    "bread": "$2.49",
    "eggs": "$2.99"
}

#Empty shopping list
shopping_list = []

#Input For loop for adding items
print("You can add up to 3 items to your shopping list.")
for i in range(3):
    item = input("Enter the item you want to add to your shopping list: ").lower()
    shopping_list.append(item)

#empty list to store prices
price_results = []

#For loop to get prices of items in shopping list if item not found return "Price not available."
for item in shopping_list: 
    price = items.get(item)     
    if price:
        price_results.append(f"The {item} is {price}") 
    else:
        price_results.append(f"The price for {item} is not available.")


#create receipt file And print List in console
with open("receipt.txt", "w") as file:
    file.write("Green Valley Grocers Price Checker Receipt:\n")
    print("Here are the prices for the items in your shopping list:")
    for price_results in price_results:  
        file.write(f"{price_results}\n")
        print(price_results)