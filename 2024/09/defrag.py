import sys
import pdb
import sys

def excepthook(type, value, traceback):
    # Print the exception
    print(f"Exception caught: {value}")
    # Start the debugger
    pdb.post_mortem(traceback)

# Override the default exception handler
sys.excepthook = excepthook

def generate_fs_map(data):
    output = []
    is_file = -1
    counter = -1
    for item in data:
        count = int(item)
        counter += 1
        is_file += 1
        if is_file == 0:
            output += [0] * count
            continue
        c = -9 if is_file % 2 else counter
        if c == -9:
            counter -= 1
        output += [c] * count

    return output

def print_debug(fs):
    output = ""
    for x in fs:
        if x == -9:
            output += "."
            continue
        output += str(x)
    print(output)

def defrag(fs):
    # Get the last non "." char from list
    rev_fs = list(fs)
    rev_fs.reverse()
    fs_len = len(fs) -1
    # breakpoint()
    for x in range(len(rev_fs)):
        y = rev_fs[x]
        if y == -9:
            continue
        try:
            pos = fs.index(-9)
        except:
            print(f"Exiting? {fs}")
            break
        fs[pos] = y
        fs[fs_len-x] = -9

    print("done defraging")

def defrag2(fs):
    output = []
    rev_fs = list(fs)
    fs_len = len(fs)
    counter = 0
    max_replaced = fs.count(-9)
    for x in range(len(fs)):
        val = fs[x]
        new_val = None
        if val == -9:
            counter += 1
            while rev_fs:
                new_val = rev_fs.pop()
                if new_val != -9:
                    break
            if not new_val:
                break
            val = new_val
        output.append(val)
        if len(output) == fs_len - max_replaced:
            print("found all?")
            break
    output += [-9,] * max_replaced
    return output

def defrag_cont(fs):
    output = []
    map_of_files ={}
    rev_fs = list(fs)
    rev_fs.reverse()
    for x in rev_fs:
        counter = map_of_files.get(x, 0)
        counter += 1
        map_of_files[x] = counter
    del map_of_files[-9]
    already_seen = []
    # Iterate through the map_of_files, see if the counter matches a run of -9's
    for key, value in map_of_files.items():
        print(key)
        for pos in range(len(output), len(fs)):
            if fs[pos] in already_seen:
                fs[pos] = -9
                continue
            if fs[pos] == -9:
                overwrite = True
                for z in range(value):
                    if pos+z < len(fs) and fs[pos+z] != -9:
                        overwrite = False
                if overwrite:
                    for z in range(value):
                        output.append(key)
                    already_seen.append(value)
                    break
                else:
                    output.append(-9)
            else:
                output.append(fs[pos])
        already_seen.append(value)
    print(map_of_files)
    return output

def checksum(fs):
    output = []
    for x in range(len(fs)):
        if fs[x] == -9:
            continue
        output.append(x*fs[x])
    return output

if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip()
    fs = generate_fs_map(data)
    print_debug(fs)
    print("00...111...2...333.44.5555.6666.777.888899")
    #defrag(fs)
    fs2 = defrag2(fs)
    #print_debug(fs2)
    print("0099811188827773336446555566..............")
    print(f"Checksum: {sum(checksum(fs2))}")
    print(f"Compacted:")
    print_debug(defrag_cont(fs))
