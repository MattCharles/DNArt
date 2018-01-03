from tkinter import Tk
from tkinter import filedialog


def generate_dna_image(dna_file):
    output = open("output.txt", "w")
    for line in dna_file:
        for character in line:
            if character == 'A':
                output.write("00")
            if character == 'T':
                output.write("01")
            if character == 'G':
                output.write("10")
            if character == 'C':
                output.write("11")
    dna_file.close()
    output.close()


def main():
    Tk().withdraw()
    generate_dna_image(filedialog.askopenfile("r"))


if __name__ == "__main__":
    main()
