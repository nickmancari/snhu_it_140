
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
        print("To add items to your inventory: get 'item name'\n")

def player_status(place, inventory, item) :

        print("You are in the "+place)
        print(inventory)
#        if item == '':
#            print("Room contains no item")
#        else:
#            print("You see a "+item)

        if place == 'Troll Lair':
            print("You're in the Troll's Lair! Ahhh!")


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
