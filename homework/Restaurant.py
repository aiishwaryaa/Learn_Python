# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders.
#  add methods like add_item_to_menu, book_tables, and customer_order. 
                
# Perform the following tasks now:                                         
#  Now add items to the menu.
#     Make table reservations.
#     Take customer orders.
#     Print the menu.
#     Print table reservations.
#     Print customer orders.

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_items_to_menu(self, item, price):
        self.menu_items[item] = price
        print(f"{item} added to the menu with Rs.{price}")

    def book_tables(self, table_num):
        self.book_table.append(table_num)
        print(f"Table {table_num} booked successfully.")


    def customer_order(self, item):
        if item in self.menu_items:
            self.customer_orders.append(item)
            print(f"Order placed for : {item}")
        else:
            print(f"{item} not available in the menu.")

            

r = Restaurant()
r.add_items_to_menu("pizza",250)  #pizza added to the menu with Rs.250
r.add_items_to_menu("burger",150) #burger added to the menu with Rs.150
r.book_tables(5)          #Table 5 booked successfully.
r.customer_order("pizza") #Order placed for : pizza
r.customer_order("fries") #fries not available in the menu.
print(r.menu_items)       #{'pizza': 250, 'burger': 150}
print(r.book_table)        #[5]
print(r.customer_orders)   #['pizza']