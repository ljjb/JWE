import argparse
import os

def is_cjk(character):
    number = ord(character)
    return number >= 0x4E00 and number <= 0x9FA5

parser = argparse.ArgumentParser(description="Convert decomposition file to that used by this program")
parser.add_argument("infile", type=str, help="input file")
parser.add_argument("name", type=str, help="name of the dataset")

args = parser.parse_args()

decomps = {}
radicals = {}
comps = set()

out_of_bounds_decomps = 0
number_characters = 0

with open(args.infile, "r") as f:
    for line in f.readlines():
        parts = line.split("\t")
        char = parts[0]
        number_characters += 1
        if not is_cjk(char):
            out_of_bounds_decomps += 1
            continue 
        radicals[char] = parts[1][-1]
        decomp = [ c for c in parts[1][1:-1] if is_cjk(c) ]
        if len(decomp) > 0:
            for comp in decomp:
                comps.add(comp)
            decomps[char] = decomp
        else:
            print("Out of bounds decomp is char={} decomp={}".format(char, parts[1][0:]))
            print("As ord is char={} decomp={}".format(ord(char), [ thing for thing in map(ord, parts[1][0:]) ] ))
            out_of_bounds_decomps += 1

print("In total {} out of bounds decomps".format(out_of_bounds_decomps))
print("In total {} characters".format(number_characters))

directory = args.name + "-subcharacter"

try: 
    os.mkdir(directory)
except OSError:
    pass

with open(directory + "/char2comp.txt", "w") as f:
    for char, decomp in decomps.items():
        f.write(char + " " + " ".join(decomp) + "\n")

with open(directory + "/comp.txt", "w") as f:
    for comp in comps:
        f.write(comp + " ")
    f.truncate()
    f.write("\n")
