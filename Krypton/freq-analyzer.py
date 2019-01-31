import sys
import operator

'''
This script is to solve the Krypton3 from http://overthewire.org/wargames/krypton/krypton3.html
This script will take in filenames as command line arguments and do frequency analysis on the 
characters in that file. I will use a dictionary datastructure that has capital letters as the
keys, and integers corresponding to the count of that letter occuring in the files as the 
value.
'''

uni_grams = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
             "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
num_unigrams = 0
most_common = "EATSORINHCLDUPGFWYMBKVJXQZ"
encrypted_pass = "KSVVWBGSJDSVSISVXBMNYQUUKBNWCUANMJS"


def analyze_unigrams(string):
    global num_unigrams

    for char in string:
        if char != ' ' and char != '\n':
            num_unigrams += 1
            uni_grams[char] += 1


def generate_report():
    print("[*] Generating report\n\n")
    print("Letter\t\tFrequency\t\tMost Common")
    print("=" * 50)

    result_dict = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "",
                   "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "",
                   "W": "", "X": "", "Y": "", "Z": ""}

    sorted_unigram_alphabet = sorted(uni_grams.items(), key=operator.itemgetter(1))
    if num_unigrams != 0:
        index = 0
        for i in range(len(sorted_unigram_alphabet) - 1, -1, -1):
            freq = (sorted_unigram_alphabet[i][1] / num_unigrams) * 100
            print("  " + sorted_unigram_alphabet[i][0] + "\t\t%.03f%%\t\t\t    %s" % (freq, most_common[index]))
            result_dict[sorted_unigram_alphabet[i][0]] = most_common[index]
            index += 1

    result = ""
    for char in encrypted_pass:
        result += result_dict[char]
    print("\n\n[+] Based on analysis the encrypted text is decrypted as: %s\n" % result)


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

    string = ""
    for line1, line2, line3 in zip(filey1, filey2, filey3):
        string += line1 + "\n\n" + line2 + "\n\n" + line3

    print("[*] Analyzing uni-grams in %s, %s, and %s" % (filey1.name, filey2.name, filey3.name))
    analyze_unigrams(string=string)
    generate_report()

    filey1.close()
    filey2.close()
    filey3.close()

