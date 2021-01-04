from geom import Door, Room

'''Связывание помещений'''
def linking():
    f = open("t.in", "r")
    rooms = dict()
    doors = dict()
    for line in f:
        line_items = line.split(',')
        if line.startswith('COMPA'):
            rid = int(line_items[1].split(' ')[1])
            rooms[rid] = Room(rid, float(line_items[2]), 
                                float(line_items[3]), float(line_items[4]))
        elif line.startswith('HVENT'):
            d = Door(int(line_items[1]), int(line_items[2]))
            doors[d.did] = d
            
            room1 = rooms[d.room1] # Берем объект из словаря rooms
            room2 = rooms[d.room2]
            
            room1.add_room(room2)
            room2.add_room(room1)
            room1.add_door(d.did)
            room2.add_door(d.did)
    f.close()
    return rooms, doors


rooms = linking()[0]

for r in rooms.keys():
    pass
    # print(rooms[r])

def pathfinder(rooms):
    # inp = input().split()
    # start_room = rooms[int(inp[0])]
    # end_room = rooms[int(inp[1])]

    start_room = rooms[2]
    end_room = rooms[5]

    where = start_room

    numer = 0

    path = []
    print(where)
    while where != end_room:
        neighbors = list(where.rooms)

        # print(len(neighbors))

        if neighbors[numer].wasthere == False:
            where.wasthere = True
            path.append(where)
            where = neighbors[numer]
            numer = 0
        elif numer < len(neighbors) - 1:
            numer += 1
        else:
            where = path[len(path) - 1]
            numer = 0
        
        print(where)

        #debug
        # where = end_room

pathfinder(rooms)