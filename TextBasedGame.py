
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

