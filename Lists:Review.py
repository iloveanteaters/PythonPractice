inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Amount of items in list
inventory_len = len(inventory)
# First item in list
first = inventory[0]
# Last item
last = inventory[-1]
# Select items 2 to 6 (not including 6)
inventory_2_6 = inventory[2:6]
# First 3 items
first_3 = inventory[:3]
# How many twin beds are in the list
twin_beds = inventory.count("twin bed")
# Remove the 5th element 
removed_item = inventory.pop(4)
# Add new item as 11th item in list 
inventory.insert(10,"19th Century Bed Frame")
# Sort inventory
inventory.sort()
print(inventory)
