import sys

GUARD="^>v<"

def print_map(map):
    for row in map:
        print(row)
    print("*******")

def move(map):
    guard_pos = []
    max_h = len(map)
    max_w = len(map[0])
    # where is the guard?
    #print_map(map)
    for x in range(max_h):
        for y in range(max_w):
            if map[x][y] in GUARD:
                guard_pos = [x,y]
                break
        if guard_pos:
            break
    if not guard_pos:
        print("Guard left map")
        return False, 1
    if guard_pos[0] in (0, max_h-1):
        return False, 1
    if guard_pos[1] in (0, max_w-1):
        return False, 1
    #print(f"Guard: {guard_pos}")
    # What is around the guard?
    sub_map = {"^": [map[x-1][y], x-1, y], # up
               "v": [map[x + 1][y], x+1, y], # down
               "<": [map[x][y-1], x, y-1], # left
    ">": [map[x][y +1], x, y+1]} # right

    # Take step
    guard_facing = map[guard_pos[0]][guard_pos[1]]
    #print(f"Guard facing: {guard_facing}")
    if sub_map[guard_facing][0] == "#":
        # Turn right
        indx = GUARD.index(guard_facing) + 1
        if indx >= len(GUARD):
            indx = 0
        map[guard_pos[0]][guard_pos[1]] = GUARD[indx]
        return True, 0
    # move
    new_spot = 0
    if map[sub_map[guard_facing][1]][sub_map[guard_facing][2]] == ".":
        new_spot = 1
    map[guard_pos[0]][guard_pos[1]] = "X"
    map[sub_map[guard_facing][1]][sub_map[guard_facing][2]] = guard_facing
    
        
    return True, new_spot


if __name__ == "__main__":
    data = []
    with open(sys.argv[1]) as f:
        for line in f:
            data.append([x for x in line.strip()])
        #data = [line.strip() for line in f]
    counter = 1
    max_moves = len(data) * len(data[0])
    more, new_spot = move(data)
    while more:
        if counter >= max_moves:
            print("Found a loop, quitting")
            break
        more, new_spot = move(data)
        counter += new_spot
        #print(counter)
    print(f"Saw {counter} new spots")
