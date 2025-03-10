#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Musthak diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper()) 
    else: 
      print('Invalid option, choose either N, X, Q') #calls a function for adding to the orders

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))
  item_name, item_price = functions.get_item_information(item_code)
  #using print statement for item descriptions
  print(f"Item Name: {item_name}, Quantity: {quantity}, Unit Item Price: {item_price}$")
  # updating the items ordered
  add_more_items = str(input("Want to add any other items y/n : "))

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


