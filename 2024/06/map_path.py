import sys

GUARD="^>v<"

def move(map):
    guard_pos = []
    max_h = len(map)
    max_w = len(map[0])
    # where is the guard?
    for x in range(max_h):
        for y in range(max_w):
            if map[x][y] in GUARD:
                guard_pos = [x,y]
                break
        if guard_pos:
            break
    if not guard_pos:
        print("Guard left map")
        return False
    print(f"Guard: {guard_pos}")
    # What is around the guard?
    sub_map = {"^": map[x-1][y], # up
               "v": map[x + 1][y], # down
               "<": map[x][y-1], # left
    ">": map[x][y +1]} # right

    # Take step
    guard_facing = map[guard_pos[0]][guard_pos[1]]
    print(f"Guard facing: {guard_facing}")
    if sub_map[guard_facing] == "#":
        # Turn right
        indx = GUARD.index(guard_facing) + 1
        if indx > len(GUARD):
            indx = 0
        map[guard_pos[0]][guard_pos[1]] = GUARD[indx]
        return True
    #map[guard_pos[0]][guard_pos[1]] = sub_map[]
    
        
    return True


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    counter = 0
    max_moves = len(data) * len(data[0])
    while move(data):
        counter += 1
        if counter >= max_moves:
            print("Found a loop, quitting")
            break

