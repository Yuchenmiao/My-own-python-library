def printMap(data: dict) -> None:
    """
    output the game map to screen
    """

    # Generate the empty map
    rownumber = data['size'][0]
    columnnumber = data['size'][1]
    mapLayout = []

    for _ in range(rownumber) :
        row = []
        for _ in range(columnnumber) :
            row.append(' ')
        mapLayout.append(row)

    # Generate the targets
    for i in range(len(data['targets'])) :
        mapLayout[data['targets'][i][0]][data['targets'][i][1]] = '.'

    # Generate the player
    mapLayout[data['player'][0]][data['player'][1]] = 'P'

    # Generate the boxes
    for i in range(len(data['boxes'])) :
        mapLayout[data['boxes'][i][0]][data['boxes'][i][1]] = 'o'

    # Generate the walls
    for i in range(len(data['walls'])) :
        mapLayout[data['walls'][i][0]][data['walls'][i][1]] = '#'

    for row in mapLayout :
        print(''.join(row))


def readMap(mapFile: str) -> dict:
    """
    read the map data file and return the data
    """
    data = {
        "size": [],
        "player": [],
        "boxes": [],
        "targets": [],
        "walls": []
    }

    mapFile = open(mapFile)
    text = mapFile.readlines()
    rownumber = len(text)
    for i in range(rownumber) :
        line = text[i]
        columnnumber = len(line)
        for j in range(len(line)) :
            if line[j] == '#' :
                data['walls'].append([i, j])
            elif line[j] == 'P' :
                data['player'] = [i, j]
            elif line[j] == 'o' :
                data['boxes'].append([i, j])
            elif line[j] == '.' :
                data['targets'].append([i, j])
            else :
                None

    data['size'] = [rownumber, columnnumber]
    
    return data

def movePlayer(direction: str, data: dict) -> None:
    """
    move the player (update data) according to the direction
    """
    for step in direction :
        if step == 'w' :
            result_wall = any(True for walls in data['walls'] if walls[0] == data['player'][0] - 1 and walls[1] == data['player'][1]) # This function is referred to CSDN
            if result_wall: # 撞墙
                None
            else : # 没有撞墙
                if [data['player'][0] - 1, data['player'][1]] in data['boxes'] : # 人前有箱子
                    box = [data['player'][0] - 1, data['player'][1]]
                    box_index = data['boxes'].index(box)
                    if [data['player'][0] - 2, data['player'][1]] in data['boxes'] or [data['player'][0] - 2, data['player'][1]] in data['walls'] : # 判断所推箱子前有没有墙或者另一个箱子
                        None
                    else :
                        data['boxes'][box_index][0] = data['boxes'][box_index][0] - 1 # 推动箱子
                        data['player'][0] = data['player'][0] - 1 # 人走
                else : # 人前没有箱子(有空地或目标点)
                    data['player'][0] = data['player'][0] - 1 # 人走
        if step == 's' :
            result_wall = any(True for walls in data['walls'] if walls[0] == data['player'][0] + 1 and walls[1] == data['player'][1]) # This function is referred to CSDN
            if result_wall: # 撞墙
                None
            else : # 没有撞墙
                if [data['player'][0] + 1, data['player'][1]] in data['boxes'] : # 人前有箱子
                    box = [data['player'][0] + 1, data['player'][1]]
                    box_index = data['boxes'].index(box)
                    if [data['player'][0] + 2, data['player'][1]] in data['boxes'] or [data['player'][0] + 2, data['player'][1]] in data['walls'] : # 判断所推箱子前有没有墙或者另一个箱子
                        None
                    else :
                        data['boxes'][box_index][0] = data['boxes'][box_index][0] + 1 # 推动箱子
                        data['player'][0] = data['player'][0] + 1 # 人走
                else : # 人前没有箱子(有空地或目标点)
                    data['player'][0] = data['player'][0] + 1 # 人走
        if step == 'a' :
            result_wall = any(True for walls in data['walls'] if walls[0] == data['player'][0] and walls[1] == data['player'][1] - 1) # This function is referred to CSDN
            if result_wall: # 撞墙
                None
            else : # 没有撞墙
                if [data['player'][0], data['player'][1] - 1] in data['boxes'] : # 人前有箱子
                    box = [data['player'][0], data['player'][1] - 1]
                    box_index = data['boxes'].index(box)
                    if [data['player'][0], data['player'][1] - 2] in data['boxes'] or [data['player'][0], data['player'][1] - 2] in data['walls'] : # 判断所推箱子前有没有墙或者另一个箱子
                        None
                    else :
                        data['boxes'][box_index][1] = data['boxes'][box_index][1] - 1 # 推动箱子
                        data['player'][1] = data['player'][1] - 1 # 人走
                else : # 人前没有箱子(有空地或目标点)
                    data['player'][1] = data['player'][1] - 1 # 人走
        if step == 'd' :
            result_wall = any(True for walls in data['walls'] if walls[0] == data['player'][0] and walls[1] == data['player'][1] + 1) # This function is referred to CSDN
            if result_wall: # 撞墙
                None
            else : # 没有撞墙
                if [data['player'][0], data['player'][1] + 1] in data['boxes'] : # 人前有箱子
                    box = [data['player'][0], data['player'][1] + 1]
                    box_index = data['boxes'].index(box)
                    if [data['player'][0], data['player'][1] + 2] in data['boxes'] or [data['player'][0], data['player'][1] + 2] in data['walls'] : # 判断所推箱子前有没有墙或者另一个箱子
                        None
                    else :
                        data['boxes'][box_index][1] = data['boxes'][box_index][1] + 1 # 推动箱子
                        data['player'][1] = data['player'][1] + 1 # 人走
                else : # 人前没有箱子(有空地或目标点)
                    data['player'][1] = data['player'][1] + 1 # 人走

def checkWin(data: dict) -> bool:
    """
    return whether the player wins the game
    """
    result = True
    for boxes in data['boxes'] :
        if boxes not in data['targets'] :
            result = False
        else :
            None
    
    return result

# ! don't modify the following line of code
if __name__ == "__main__":#

# You can modify the following lines of code to test your implementation of the functions above.
# The following lines of code will run the whole game if you have implemented all the functions above correctly.
    data = readMap("map_easy.txt")
    print("\033c", end="") # clear the screen
    printMap(data)
    while not checkWin(data):
        movePlayer(input(), data)
        print("\033c", end="") # clear the screen
        printMap(data)
    print("You win!")