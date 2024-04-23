from items import items

class LocalStore:
    def __init__(self):
        self.items = items
        self.cart = {}


    def display_items(self):
        """
        Display store items into two separate columns with price rate
        """
        print("____Available Items____")
        #Separate into two columns
        half_len = len(self.items) // 2
        #Left column
        left_column = list(self.items.items())[:half_len]
        #Right column
        right_column = list(self.items.items())[half_len:]

        for left_item, right_item in zip(left_column, right_column):
            #Price tag for each item in the list
            print(f"{left_item[0].capitalize()}: £{left_item[1]:.2f}\t\t{right_item[0].capitalize()}: £{right_item[1]:.2f}")
    

    def add_to_cart(self, item):
        """
        Creats a cart for user to track the items added and able to selcet the quantity of items
        """
        if item.lower() in self.items:
            #Can select the amount of quantity of items upto 100 per item
            quantity = input(f"How many {item.capitalize()} do you want to add to your cart? (Limit 100): ")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity <= 100:
                    if item.lower() not in self.cart:
                        self.cart[item.lower()] = quantity * self.items[items.lower()]
                    else:
                        self.cart[item.lower()] += quantity * self.items[item.lower()]
                        print(f"{quantity} {item.capitalize()} added to your cart. ")
                        self.display_cart()
                else:
                    print("You can only add up to 100 of each item.")
            else:
                print("Invalid quantity. Please enter correct number.")
        else:
            print("Invalid quantity. Please select from the list.")

    def remove_from_cart(self, item):
        """
        Asks user if they want to remove items from their existing cart with total amount users want to remove
        """
        if item.lower() in self.cart:
            #Remove added items from cart where removed items cannot be more than added items & items cannot be different
            quantity = input(f"Hom many {item.capitalize()} do you want to remove from your cart? (Limit: {self.cart[item.lower()]})")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity <= self.cart[item.lower()]:
                    self.cart[item.lower()] -= quantity * self.items[items.lower()]
                    print(f"{quantity} {item.capitalize()} removed from your cart.")
                    self.display_cart()

                else:
                    print("Invalid quantity. Please enter correct number.")
            else:
                print("Please enter correct number.")
        else:
            print("Item not found in your cart.")


