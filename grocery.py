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

