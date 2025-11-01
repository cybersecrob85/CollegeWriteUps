#Robert J Potter, 10/27/2025, Milestone 1

#Empty Shopping List
Shopping_List = []

#Greeting Message for User
print("Welcome to Green Valley Grocers Shopping List App!")


#Create and Store Items For Shopping List
New_Item = input("Please enter an item to add to your shopping list: ")
Shopping_List.append(New_Item)
New_Item1 = input("Please enter an item to add to your shopping list: ")
Shopping_List.append(New_Item1)
New_Item2 = input("Please enter an item to add to your shopping list: ")
Shopping_List.append(New_Item2)


#Display Current Shopping List
print(f"Your current shopping list is: {Shopping_List}")
