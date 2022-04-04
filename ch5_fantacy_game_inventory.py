stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
         print(value, key)
         item_total += value
    print("Total number of items: " + str(item_total))
     
#display_inventory(stuff)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


print('You arrive at the cave and see the Dragon. Your current inventory is:')
display_inventory(stuff)

while True:
    fight = input('Do you fight the Dragon? (y/n)')
    if fight == 'Y' or fight == 'y':
        import random
        fight_outcome = (random.randint(1, 10))
        if fight_outcome % 2 == 0:
            print('You died')
        else:
            print('You win')
            print('The Dragon dropped:')
            print(*dragonLoot, sep = '\n')
            print('You now have')            
            add_to_inventory(stuff, dragonLoot)
            display_inventory(stuff)
            break
    elif fight == 'N' or fight == 'n':
        print('Game over.')
        break
    elif fight != 'Y' or fight != 'N':
        print('Please enter Y or N.')
        continue
