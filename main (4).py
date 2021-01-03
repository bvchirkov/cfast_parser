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

obj = linking()
rooms = obj[0]

for r in rooms.keys():
    print(rooms[r])


