from geom import Door, Room

class Building:
    rooms = dict()
    doors = dict()

'''Связывание помещений'''
def linking(aFile_name, aBuilding):
    f = open(aFile_name, "r")
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
    aBuilding.rooms = rooms
    aBuilding.doors = doors
    # return rooms, doors

linking("t3.in", Building)
rooms = Building.rooms

def pathfinder(rooms):
    # inp = input().split()
    # start_room = rooms[int(inp[0])]
    # end_room = rooms[int(inp[1])]

    start_room = rooms[4]
    end_room = rooms[5]

    where = start_room

    numer = 0

    path = []
    print(where)
    while where != end_room:
        neighbors = list(where.rooms)

        if neighbors[numer].wasthere == False:
            where.wasthere = True
            path.append(where)
            where = neighbors[numer]
            numer = 0
        elif numer < len(neighbors) - 1:
            numer += 1
        else:
            path.append(where)
            where.wasthere = True
            where = path[len(path) - 2]
            numer = 0
        
        print(where)

pathfinder(rooms)

for r in rooms.keys():
    print(rooms[r])
