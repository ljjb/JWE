import argparse
import os

parser = argparse.ArgumentParser(description="Convert decomposition file to that used by this program")
parser.add_argument("infile", type=str, help="input file")
parser.add_argument("name", type=str, help="name of the dataset")

args = parser.parse_args()

decomps = {}
radicals = {}
comps = set()

with open(args.infile, "r") as f:
    for line in f.readlines():
        parts = line.split("\t")
        char = parts[0]
        radicals[char] = parts[1][-1]
        decomp = parts[1][1:-1]
        for comp in decomp:
            comps.add(comp)
        decomps[char] = decomp

directory = args.name + "-subcharacter"

try: 
    os.mkdir(directory)
except OSError:
    pass

with open(directory + "/char2comp.txt", "w") as f:
    for char, decomp in decomps.items():
        f.write(char + " " + decomp + "\n")

with open(directory + "/comps.txt", "w") as f:
    for comp in comps:
        f.write(comp + " ")
    f.truncate()
    f.write("\n")
