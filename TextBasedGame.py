# Nick Mancari 7-3 Project Two
from random import randint

RED = '\033[93m'
GREEN = '\033[92m'
NC = '\033[0m'
BOLD = '\033[1m'

#Dictionary for locations, movement, and items in rooms
rooms = {
        'Entrance' : { 'East' : 'Dungeon Staircase' },
        'Dungeon Staircase' : { 'North' : 'Stalagmite Cove', 'South' : 'Forge', 'East' : 'Fire Cavern',  'West' : 'Entrance',  'Item' : 'Pearl' },
        'Stalagmite Cove' : { 'South' : 'Dungeon Staircase', 'East' : 'Troll Lair', 'Item' : 'Diamond' },
        'Troll Lair' : { 'West' : 'Stalagmite Cove' },
        'Forge' : { 'North' : 'Dungeon Staircase', 'East' : 'Icy Room', 'West' : 'Ore Mine', 'Item' : 'Sword' },
        'Icy Room' : { 'West' : 'Forge', 'Item' : 'Gem' },
        'Ore Mine' : { 'East' : 'Forge', 'Item' : 'Coins' },
        'Fire Cavern' : { 'North' : 'Gold Mine', 'West' : 'Dungeon Staircase', 'Item' : 'Ruby' },
        'Gold Mine' : { 'South' : 'Fire Cavern', 'Item' : 'Doubloon' }

}

#Game start instructions to educate the player on objectives and gameplay
def instructions() :
        print("\n----------------------------------------------")
        print('{:^45s}'.format(BOLD+"~~~~DUNGEONS & TROLLS~~~~"+NC))
        print("----------------------------------------------\n")
        print("Collect the 7 items or slay the troll to win the game.")
        print("But Beware the Troll Lair. The angry Troll is fit to fight. You have a better chance at slaying the troll if you have a SWORD!")
        print("Maneuver the dungeonscape with these commands: North, South, East, and West.")
        print("To add items to your inventory: Answer the prompt Yes of No\n")

#Function to handle villain room situation
def villain_place(item_list):

    damage_roll = randint(1, 10)

    if 'Sword' in item_list:
        if damage_roll >= 3:
            print("\n**You have defeated the troll!**\n")
            print(GREEN+"\nYOU WIN!\n"+NC)
            exit()
        else:
            print(RED+"You have fought and parished!\nBetter Luck Next Time!"+NC)
            exit()
        
    else:
        print("You don't have a sword! Run away!")

#Function to update player on current status as they move through the dungeons and add items to their inventory
def player_status(place, inventory) :

    print("\nYou are in the "+place)
    print("Inventory: {}".format(inventory))

    if place == 'Troll Lair':
        print(BOLD+"~~~~~~~~~~~~~~~~~\nThe Troll is here!! Ahhh!\n~~~~~~~~~~~~~~~~~"+NC)
        villain_place(inventory)


instructions()
place = 'Entrance'
inventory = list()
item = ''

while True:
    #player_status func
    player_status(place, inventory)
    #check room for item and enage user on item collection logic
    if 'Item' in rooms[place]:
        item = rooms[place]['Item']
        print("You see a {}".format(item))

        collect_item = input("Collect the item in this room? Yes/No\n")
        if collect_item == 'Yes':
            inventory.append(item)
            if len(inventory) == 7:
                print(GREEN+"\nYOU WIN!\n"+NC)
                exit()
            del rooms[place]['Item']
    #player movement logic
    player_input = input("------------\nEnter your move:\n")
    if player_input in rooms[place]:
        place = rooms[place][player_input]

    else:
        print("\nNot a valid direction\n")
