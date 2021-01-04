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
            roomid = int(line_items[1].split(' ')[1])
            rooms[roomid] = Room(roomid, float(line_items[2]), 
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

# pathfinder(rooms)

start_point = rooms[2]
end_point = rooms[9]
processed_queue = list()
path = list()
current_point = start_point

while True:
    path.append(current_point.roomid)
    print(current_point.roomid)
    if current_point.roomid == end_point.roomid:
        break

    neighbors = list(current_point.rooms)
    # if len(neighbors) == 1 and neighbors[0] != end_point.roomid:
    for neighbor in neighbors:
        if neighbor.wasthere:
            continue
        else:
            processed_queue.append(neighbor)
    
    current_point.wasthere = True
    current_point = processed_queue.pop()

print(path)
# for r in rooms.keys():
#     print(rooms[r])
