# Import the other file
from ShoppingPL import GroceryPL

# Defining list function, asking the amount of items ordered
def createListPL():
    ShoppingList = []

    orderItems = int(input("How many items will you order?:"))
    while True:
        if orderItems < 1:
            print("You must order at least one item.")
        else:
            break

# Looping the amount of ordered items, asking for amount of pounds and item type
    for i in range(orderItems):
        print("Item", i + 1)
        name = input("Name of item:")
        amount = eval(input("The amount of pounds: "))
        item = GroceryPL(name,amount)
        while True:
            if amount <= 0:
                print("Amount must be greater than 0")
                eval(input("Enter the amount of pounds: "))
            else:
                break
        ShoppingList.append(item)
    return ShoppingList

# Display the final result
def DisplayPL(newList):
    print("-"*30)
    print("Here is your items")
    for i in range(len(newList)):
        print("Item", i + 1)
        print(newList[i].__str__() + "\n")

# Display the total for everything
def CalculatePL(newList):
    print("-"*30)
    total = 0
    for i in range(len(newList)):
        total += newList[i].TotalPL()
    formatTotal = "$ {:,.2f}".format(total)
    return formatTotal

# Calling the functions
ShoppingList = createListPL()
DisplayPL(ShoppingList)
print("Total amount", CalculatePL(ShoppingList))
print("-"*30)