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
    fs_len = len(fs)
    for x in rev_fs:
        if x == -9:
            continue
        try:
            pos = fs.index(-9)
        except:
            break
        fs[pos] = x
        fs[fs_len -pos] = -9
    print("done defraging")

if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip()
    fs = generate_fs_map(data)
    print_debug(fs)
    print("00...111...2...333.44.5555.6666.777.888899")
    defrag(fs)
    print_debug(fs)
    print("0099811188827773336446555566..............")
