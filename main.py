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
            room_id = int(line_items[1].split(' ')[1])
            rooms[room_id] = Room(room_id, float(line_items[2]), 
                                float(line_items[3]), float(line_items[4]))
        elif line.startswith('HVENT'):
            d = Door(int(line_items[1]), int(line_items[2]))
            doors[d.did] = d
            
            room1 = rooms[d.room1] # Берем объект из словаря rooms
            room2 = rooms[d.room2]
            
            room1.add_neighbor(room2)
            room2.add_neighbor(room1)
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

current_point = rooms[2]    # Текущая (стартовая) точка
end_point = rooms[9]        # Конечная точка
processed_queue = list()    # Очеред на обработку
step_in_graph = 0           # Шаг обработки

'''Обход графа от стартовой до конечной точки'''
while True:
    # Останов если дошли до конечной точки
    if current_point.room_id == end_point.room_id:
        # Для конечной точки тоже отмечаем, что там побывали и на каком шаге
        end_point.wasthere = True              
        end_point.step_in_graph = step_in_graph
        break

    # Обход всех соседей
    for neighbor in current_point.neighbors:
        if neighbor.wasthere:
            continue
        else:
            # В очередь попадают только те, в которых не были
            processed_queue.append(neighbor)

    current_point.wasthere = True               # Отмечаем, что побывали в узле
    current_point.step_in_graph = step_in_graph # Устанавливаем для текущего узла шаг, на котором он был обработан
    step_in_graph += 1                          # Увеличиваем шаг
    
    current_point = processed_queue.pop()       # Достаем узел из очереди на обработку

'''Восстановление пути от конечной точки'''
path = list()                       # Путь от начальной до конечной точки
path.append(current_point.room_id)  # Добавляем первый элемент пути - конечную точку

while True:
    # Обходим всех соседей точки, на которой остановились в предыдущем цикле
    for neighbor in current_point.neighbors:
        if neighbor.step_in_graph == -1: # Если не были в узле, то пропускаем этого соседа
            continue
        # Иначе сравниваем шаг, на котором закончили его обрабатывать, с шагом, на котором остановились в цикле выше
        if neighbor.step_in_graph < current_point.step_in_graph:  # Берем соседа с меньшим шагом
            current_point = neighbor                # Устанавливаем новый текущий узел
            path.append(current_point.room_id)      # Добавляем узел в путь
            break
    
    # Если дошли до первого шага по графу, то останавливаем восстановление пути
    if current_point.step_in_graph == 0:
        break

print(path)
