import os

def retsum():
    file_path = os.path.join(os.path.dirname(__file__),"number.txt")
    tot = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if line.isnumeric():
                tot = tot + int(line)

    return tot

print(retsum())