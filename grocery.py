from item import items  # Importing items


class LocalGroceryStore:
    def __init__(self):
        self.items = items
        self.cart = {}

    def display_items(self):
        """Display the shop items in two columns with price tags."""
        print("Available Items:")
        half_len = len(self.items) // 2
        left_column = list(self.items.items())[:half_len]
        right_column = list(self.items.items())[half_len:]

        for left_item, right_item in zip(left_column, right_column):
            print(f"{left_item[0].capitalize()}: \
            £{left_item[1]:.2f}\t\t{right_item[0]\
            .capitalize()}: £{right_item[1]:.2f}")

    def add_to_cart(self, item):# Adds items from list to cart
        """Add items to the cart."""
        """Items can only be added from list"""
        """Correct name of item should be added"""
        if item.lower() in self.items:
            quantity = self.get_valid_quantity()
            if quantity is not None:
                if item.lower() not in self.cart:
                    self.cart[item.lower()] = quantity * self.items
                    [item.lower()]
                else:
                    self.cart[item.lower()] += quantity * self.items
                    [item.lower()]
                print(f"{quantity} {item.capitalize()} added to cart.")
                self.display_cart()
        else:
            print("Item doesn't exist. Please select from the list.")

    def get_valid_quantity(self):#
        """Validate and return a valid quantity input."""
        while True:
            quantity = input("How many do you want to \
            add to your cart? (Limit: 100): ")
            if quantity.isdigit():
                quantity = int(quantity)
                if 0 < quantity <= 100:
                    return quantity
                else:
                    print("Invalid quantity. Please enter a\
                    number between 1 and 100.")
            else:
                print("Invalid input. Please enter a valid number.")

    def remove_from_cart(self, item):
        """Remove items from the cart."""
        if item.lower() in self.cart:
            current_quantity = self.cart[item.lower()] / self.items
            [item.lower()]
            quantity = self.get_valid_quantity_remove(current_quantity)
            if quantity is not None:
                self.cart[item.lower()] -= quantity * self.items[item.lower()]
                print(f"{quantity} {item.capitalize()} removed from cart.")
                self.display_cart()
        else:
            print("Item not found in your cart.")

    def get_valid_quantity_remove(self, current_quantity):
        """Validate and return a valid quantity to remove."""
        while True:
            quantity = input(f"How many do you want to remove \
            from your cart? (Limit: {current_quantity}) ")
            if quantity.isdigit():
                quantity = int(quantity)
                if 0 < quantity <= current_quantity:
                    return quantity
                else:
                    print(f"Invalid quantity. Please enter a number \
                    between 1 and {current_quantity}.")
            else:
                print("Invalid input. Please enter a valid number.")

    def display_cart(self):
        """Display the items in the cart along with the total."""
        print("\nYour Cart:")
        for item, price in self.cart.items():
            print(f"{item.capitalize()}: £{price:.2f}")
        print(f"Total: £{sum(self.cart.values()):.2f}")

    def start_shopping(self):
        """Start the shopping process."""
        print("Welcome to the Grocery Store!")
        self.display_items()

        while True:
            choice = input("Enter the item you want to add to cart \
            (or 'exit' to end shopping): ").lower()
            if choice == 'exit':
                break
            elif choice.isdigit():
                print("Please select items from the list.")
            else:
                self.add_to_cart(choice)
                while True:
                    continue_shopping = input("Do you want to \
                    continue shopping? (y/n): ").lower()
                    if continue_shopping in ['y', 'n']:
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                if continue_shopping == 'n':
                    break

        if self.cart:
            while True:
                remove_choice = input("Do you want to remove items \
                from your cart? (y/n): ").lower()
                if remove_choice == 'y':
                    item_to_remove = input("Enter the item you want \
                    to remove from your cart: ").lower()
                    self.remove_from_cart(item_to_remove)
                    if not self.cart:
                        break
                elif remove_choice == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        print("\n***Thanks for shopping! See you soon***")
        print("\nYour total is:")
        self.display_cart()


store = LocalGroceryStore()
store.start_shopping()
