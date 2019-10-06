# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
shopping_cart = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]



# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = input("Which would you like? ")

    # Get index of the pie from the selected number
    # YOUR CODE HERE
    choice_index = int(pie_choice) - 1
    
    
    # Add pie to the pie list by finding the matching index and adding one to its value
    # YOUR CODE HERE
    shopping_cart.append(pie_choice) 
    shopping_cart[int(pie_choice)] += 1
    
    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")

    # Provide exit option
    # Prompt the user if they would like to make another purchase
    # YOUR CODE HERE
    shopping = input("Would you like to make another selection? ('y' or 'n') ")
# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
# YOUR FOR LOOP HERE

for pies in range(len(pie_list)):
    print(f"{shopping_cart[pies]} {pie_list[pies]}")
    # Gather the count of each pie in the pie list and print them alongside the pies
    # YOUR CODE HERE
