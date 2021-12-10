# Create Class
class GroceryPL:

# Initializer method with parameters for name and amount
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.price = 0
        self.total = 0

# Private method for the price list of the items
    def __ListPL(self):
        if self.name == 'Dry Cured Iberian Ham':
            self.price = 177.8
        elif self.name == 'Wagyu Steaks':
            self.price = 450
        elif self.name == 'Matsutake Mushrooms':
            self.price = 272
        elif self.name == 'Kopi Luwak Coffee':
            self.price = 306.5
        elif self.name == 'Moose Cheese':
            self.price = 487.2
        elif self.name == 'White Truffles':
            self.price = 3600
        elif self.name == 'Blue Fin Tuna':
            self.price = 3603
        elif self.name == 'Le Bonnotte Potatoes':
            self.price = 270.81
        else:
            self.price = 0.00

# A method for the total price
    def TotalPL(self):
        self.__ListPL()
        self.total = self.price * self.amount
        return self.total

# A method to return the format in dollar form
    def Format (self):
        self.__ListPL()
        self.TotalPL()
        self.priceFormat = "$ {:,.2f}".format(self.price)
        self.totalFormat = "$ {:,.2f}".format(self.total)
        return self.totalFormat, self.priceFormat
    
# accessor method to return all the things bought
    def __str__(self):
        self.__ListPL()
        self.TotalPL()
        self.Format()
        return f" Item:{self.name} \n Amount: {self.amount} \n Price: {self.priceFormat} \n Total: {self.totalFormat}"    