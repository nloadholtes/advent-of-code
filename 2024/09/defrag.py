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
            output += "0" * count
            continue
        c = -9 if is_file % 2 else counter
        if c == -9:
            counter -= 1
        output += [c] * count

    return output

def print_debug(fs_map):
    output = ""
    for x in fs_map:
        if x == -9:
            output += "."
            continue
        output += str(x)
    print(output)

if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip()
    fs = generate_fs_map(data)
    print_debug(fs)
    print("00...111...2...333.44.5555.6666.777.888899")
