# Grocery shop items list
from item import items


class LocalGroceryStore:
    def __init__(self):
        self.items = items
        self.cart = {}

    def display_items(self):
        """
        Displays the shop items into two different columns with price tags
        """
        print("Available Items:")
        # Divides the shop items into two columns
        half_len = len(self.items) // 2
        # left column
        left_column = list(self.items.items())[:half_len]
        # right column
        right_column = list(self.items.items())[half_len:]

        # Creats price tags for each items in the left and right columns
        for left_item, right_item in zip(left_column, right_column):
            print(
                 f"{left_item[0].capitalize()}: £{left_item[1]:.2f}\t\t"
                 f"{right_item[0].capitalize()}: £{right_item[1]:.2f}"
                 )

    # Adds items to the cart
    def add_to_cart(self, item):
        """
        Creating shopping cart for user where user can
        add items from the list
        according to their names and select
        the quantity .
        User can only add upto 100 of each item .
        User can only add valid qantity in numbers or
        program will ask for valid amount and numbers.
        Items that are not in the list is not accepted by program.
        """
        if item.lower() in self.items:
            quantity = input(
                             f"How many {item.capitalize()} do you want "
                             "to add to your cart?(Limit: 100): "
                             )

            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= 100:
                    if item.lower() not in self.cart:
                        self.cart[item.lower()] = (
                                     quantity * self.items[item.lower()]
                                                  )

                    else:
                        self.cart[item.lower()] += (
                              quantity * self.items[item.lower()]
                                                   )

                    print(f"{quantity} {item.capitalize()} added to cart.")
                    self.display_cart()
                elif quantity == 0:
                    print("Quantity cannot be 0.")
                    while True:
                        add_option = input(
                                     "Add valid quantity? (y/n):"
                                     ).lower()
                        if add_option == 'y':
                            self.add_to_cart(item)
                            break
                        elif add_option == 'n':
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    print("You can only add up to 100 of each item.")
            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Item doesn't exist. Please select from the list.")

    # Remove items from the cart
    def remove_from_cart(self, item):
        """
        If user wants to remove certain items from their existing cart,
        user can remove items at the end of their checkout.
        The items user wants to remove will only be accepted
        as their names in list.
        Users can only remove the quantity of items, not the price.
        """
        if item.lower() in self.cart:
            current_quantity = (
                 self.cart[item.lower()] / self.items[item.lower()]
                               )

            quantity = input(
             f"How many {item.capitalize()} do you want to remove "
             f"from your cart?(Limit: {current_quantity}) "
                            )

            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0 and quantity <= current_quantity:
                    self.cart[item.lower()] -= (
                     quantity * self.items[item.lower()]
                                                )

                    print(f"{quantity} {item.capitalize()} removed from cart.")
                    self.display_cart()
                    return True
                elif quantity == 0:
                    print("Quantity cannot be 0.")
                else:
                    print(
                     f"Invalid quantity. You cannot remove more than "
                     f"{current_quantity} of {item.capitalize()}."
                          )

            else:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Item not found in your cart.")
        return False
    # Display cart with items names and sum-total

    def display_cart(self):
        if self.cart:
            print("\nYour Cart:")
            for item, price in self.cart.items():
                print(f"{item.capitalize()}: £{price:.2f}")
            print(f"Total: £{sum(self.cart.values()):.2f}")
        else:
            print("\nYour cart is empty.")

    # Display message and options on running program
    def start_shopping(self):
        """
        User will be presented with welcome messsage from the shop.
        User will be provided the list of items from shop where user can enter
        the items name to add to their cart.
        At the start of program user will be provide with options of wheter
        the user wants to shop or not, if the user wants to shop they
        can continue adding to their cart.
        If the user doesn't wants to shop and enters 'exit' the program will
        end and user receives their sum-total and goodbye message.
        """
        print("Welcome to the Grocery Store!")
        self.display_items()
        while True:
            choice = input("Enter the item you want to add to "
                           "cart (or 'exit' to end shopping): ").lower()
            if choice == 'exit':
                break
            elif choice.isdigit():
                print("Please select items from the list.")
            else:
                self.add_to_cart(choice)
                while True:
                    continue_shopping = input("Do you want to continue "
                                              "shopping? (y/n): ").lower()
                    if continue_shopping in ['y', 'n']:
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                if continue_shopping == 'n':
                    break
        if self.cart:
            while True:
                remove_choice = input("Do you want to remove items "
                                      "from your cart? (y/n): ").lower()
                if remove_choice == 'y':
                    item_to_remove = input("Enter the item you want to "
                                           "remove from your cart: ").lower()
                    removed = self.remove_from_cart(item_to_remove)
                    if removed:
                        continue_shopping = input("Do you want to continue "
                                                  "shopping? (y/n): ").lower()
                        if continue_shopping == 'n':
                            break
                    if not self.cart:
                        break
                elif remove_choice == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        print("\n____Thanks for shopping in Local "
              "Grocery Store! See you soon____")
        if self.cart:
            print("\n__Your total is:")
            self.display_cart()


store = LocalGroceryStore()
store.start_shopping()
