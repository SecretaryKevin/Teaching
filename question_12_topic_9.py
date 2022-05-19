import os


def main(input_filename, output_filename):
    """takes input file reverses it and writes it to output file"""
    """opens the file and reads it and splits it into a list"""
    infile = open(input_filename, 'r')
    text = infile.read()
    text = text.split()
    """creates a new list with the words reversed"""
    i = len(text) - 1
    output = []
    while i >= 0:
        output.append(text[i])
        i -= 1
    final_string = ' '.join(output)
    """Opens the output file and writes the final string to it."""
    output_file = open(output_filename, "w")
    output_file.write(final_string)
    output_file.close()


main('Text.text', 'output.txt')


