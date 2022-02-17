
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

while True:
    #player_status func
    #item handling
    #take player input
    #change location with player input
