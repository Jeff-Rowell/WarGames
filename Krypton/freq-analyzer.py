import sys
import operator

'''
This script is to solve the Krypton3 from http://overthewire.org/wargames/krypton/krypton3.html

This script will take in filenames as command line arguments and do frequency analysis on the 
characters in that file. I will use a dictionary datastructure that has capital letters as the
keys, and integers corresponding to the count of that letter occuring in the files as the 
value.
'''


def analyze_unigrams(file1, file2, file3):
    print("[*] Analyzing uni_grams in %s, %s, and %s" %(file1.name, file2.name, file3.name))
    alphabet = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0,
                "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
                "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    most_common = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    num_letters = 0
    string = ""
    for line1, line2, line3 in zip(file1, file2, file3):
        string += line1 + "\n\n" + line2 + "\n\n" + line3

    for char in string:
        if char != ' ':
            num_letters += 1

        if char == "A":
            alphabet["A"] += 1

        elif char == "B":
            alphabet["B"] += 1

        elif char == "C":
            alphabet["C"] += 1

        elif char == "D":
            alphabet["D"] += 1

        elif char == "E":
            alphabet["E"] += 1

        elif char == "F":
            alphabet["F"] += 1

        elif char == "G":
            alphabet["G"] += 1

        elif char == "H":
            alphabet["H"] += 1

        elif char == "I":
            alphabet["I"] += 1

        elif char == "J":
            alphabet["J"] += 1

        elif char == "K":
            alphabet["K"] += 1

        elif char == "L":
            alphabet["L"] += 1

        elif char == "M":
            alphabet["M"] += 1

        elif char == "N":
            alphabet["N"] += 1

        elif char == "O":
            alphabet["O"] += 1

        elif char == "P":
            alphabet["P"] += 1

        elif char == "Q":
            alphabet["Q"] += 1

        elif char == "R":
            alphabet["R"] += 1

        elif char == "S":
            alphabet["S"] += 1

        elif char == "T":
            alphabet["T"] += 1

        elif char == "U":
            alphabet["U"] += 1

        elif char == "V":
            alphabet["V"] += 1

        elif char == "W":
            alphabet["W"] += 1

        elif char == "Y":
            alphabet["Y"] += 1

        elif char == "Y":
            alphabet["Y"] += 1

        elif char == "Z":
            alphabet["Z"] += 1

    print("[*] Generating report\n\n")
    print("Letter\t\tFrequency\t\tMost Common")
    print("="*55)
    sorted_alphabet = sorted(alphabet.items(), key=operator.itemgetter(1))
    index = 0
    for i in range(len(sorted_alphabet)-1, -1, -1):
        freq = (sorted_alphabet[i][1]/num_letters) * 100
        print("  " + sorted_alphabet[i][0] + "\t\t%.03f%%\t\t\t    %s" % (freq, most_common[index]))
        index += 1


if __name__ == "__main__":
    length = len(sys.argv)
    if (length-1) != 3:
        print("[-] Error: Need 3 filenames to parse for frequency analysis")
        exit(1)

    print("Beginning frequnecy analysis...\n")
    print("[*] Opening files: %s, %s, and %s" % (sys.argv[1], sys.argv[2], sys.argv[3]))
    filey1 = open(sys.argv[1], "r")
    filey2 = open(sys.argv[2], "r")
    filey3 = open(sys.argv[3], "r")

    analyze_unigrams(file1=filey1, file2=filey2, file3=filey3)

    filey1.close()
    filey2.close()
    filey3.close()

    filey1.close()

