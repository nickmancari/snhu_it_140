from random import randint

rooms = {
        'Entrance' : { 'East' : 'Dungeon Staircase' },
        'Dungeon Staircase' : { 'North' : 'Stalagmite Cove', 'South' : 'Forge', 'East' : ' Fire Cove',  'West' : 'Entrance',  'Item' : 'Pearl' },
        'Stalagmite Cove' : { 'South' : 'Dungeon Staircase', 'East' : 'Troll Lair', 'Item' : 'Diamond' },
        'Troll Lair' : { 'West' : 'Stalagmite Cove' },
        'Forge' : { 'North' : 'Dungeon Staircase', 'East' : 'Icy Room', 'West' : 'Ore Mine', 'Item' : 'Sword' },
        'Icy Room' : { 'West' : 'Forge', 'Item' : 'Gem' },
        'Ore Mine' : { 'East' : 'Forge', 'Item' : 'Coins' },
        'Fire Cavern' : { 'North' : 'Gold Mine', 'West' : 'Dungeon Staircase', 'Item' : 'Ruby' },
        'Gold Mine' : { 'South' : 'Fire Cavern', 'Item' : 'Doubloon' }

}

def instructions() :
        print("\n----------------------------------------------")
        print('{:^45s}'.format("~~~~DUNGEONS & TROLLS~~~~"))
        print("----------------------------------------------\n")
        print("Collect the 7 items to win the game.")
        print("But Beware the Troll Lair. You have a better chance at slaying the troll if you have a SWORD!")
        print("Maneuver the dungeonscape with these commands: North, South, East, and West.")
        print("To add items to your inventory: Answer the prompt Yes of No\n")

def villian_place(item_list):

    damage_roll = randint(1, 10)

    if 'Sword' in item_list:
        if damage_roll >= 3:
            print("You have defeated the troll!")
        else:
            print("You have fought and parished!\nBetter Luck Next Time!")
            exit
        
    else:
        print("You don't have a sword! Run away!")

def player_status(place, inventory) :

    print("You are in the "+place)
    print(inventory)

    if place == 'Troll Lair':
        print("You're in the Troll's Lair! Ahhh!")
        villian_place(inventory)


place = 'Entrance'
inventory = list()
item = ''

while True:
    #player_status func
    player_status(place, inventory)
    #chck room for item and enage user on item collection logic
    if 'Item' in rooms[place]:
        item = rooms[place]['Item']
        print("You see a"+item)

        collect_item = input("Collect the item in this room? Yes/No\n")
        if collect_item == 'Yes':
            inventory.append(item)

    player_input = input("------------\nEnter your move:\n")
    if player_input in rooms[place]:
        place = rooms[place][player_input]

    else:
        print("Not a valid direction")
