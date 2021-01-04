class Room:
    wasthere = False

    def __init__(self, rid, width, depth, height):
        self.rid = rid
        self.width = width
        self.height = height
        self.depth = depth
        self.doors = set()
        self.rooms = set()
    
    def area(self):
        return self.width * self.depth

    def add_door(self, did):
        self.doors.add(did)
    
    def add_room(self, room):
        self.rooms.add(room)

    def __str__(self):
        # return f'Room is {self.rid}: w:{self.width}, d:{self.depth}, h:{self.height}, doors:{self.doors}, neighbors: {self.rooms}'
        return f'Room num {self.rid}'

class Door:
    _did = 0
    def __init__(self, r1, r2):
        self.room1 = r1
        self.room2 = r2
        self.did = Door._did
        Door._did += 1