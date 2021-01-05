class Room:
    wasthere = False
    step_in_graph = -1 # Номер шага, на котором было обработано помещение
    def __init__(self, room_id, width, depth, height):
        self.room_id = room_id
        self.width = width
        self.height = height
        self.depth = depth
        self.doors = set()
        self.neighbors = set()
    
    def area(self):
        return self.width * self.depth

    def add_door(self, did):
        self.doors.add(did)
    
    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def __str__(self):
        # return f'Room is {self.room_id}: w:{self.width}, d:{self.depth}, h:{self.height}, doors:{self.doors}, neighbors: {self.neighbors}'
        return f'Room num {self.room_id}'

class Door:
    _did = 0
    def __init__(self, r1, r2):
        self.room1 = r1
        self.room2 = r2
        self.did = Door._did
        Door._did += 1