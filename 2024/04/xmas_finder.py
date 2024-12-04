
import sys


PHRASE = "XMAS"

def count_phrase(lines, phrase=PHRASE):
    counter = 0
    def _line_counter(lin, counter):
        for line in lin:
            if phrase in line:
                counter += 1
            if phrase in ''.join(list(reversed(line))):
                counter += 1
        return counter
    counter += _line_counter(lines, counter)
    # Transform?
    transpose = [''.join(col) for col in zip(*lines)]
    counter += _line_counter(transpose, counter)
    return counter


def count_phrase_brute(lines, phrase):
    counter = 0
    # Recusively call to check the length of the phrase? (e.g. one letter at a time)
    for row in lines:
        for col in row:
            # Scan left for phrase
            # Scan Down (if room)
            #
            for l in phrase:
                if c != l:
                    break


    return counter


if __name__ == "__main__":
    filename = sys.argv[1]
    data = []

    with open(filename) as f:
        for line in f:
            data.append(line)

    print(f"{PHRASE} is seen {count_phrase(data)} times")

