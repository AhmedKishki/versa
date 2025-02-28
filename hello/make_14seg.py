import sys

# Font dictionary: Maps characters to active segments
# Segment labels correspond to those in the Versa Dev Board schematic
font = {
 "A": ['e', 'f', 'a', 'b', 'c', 'p', 'k'],
 "B": ['e', 'f', 'a', 'j', 'p', 'l', 'd'],
 "C": ['d', 'e', 'f', 'a'],
 "D": ['e', 'f', 'g', 'n'],
 "E": ['d', 'e', 'f', 'a', 'p'],
 "F": ['e', 'f', 'a', 'p'],
 "G": ['d', 'e', 'f', 'a', 'k', 'c'],
 "H": ['e', 'f', 'p', 'k', 'b', 'c'],
 "I": ['a', 'h', 'm', 'd'],
 "J": ['b', 'c', 'd'],
 "K": ['e', 'f', 'p', 'j', 'l'],
 "L": ['d', 'e', 'f'],
 "M": ['e', 'f', 'g', 'j', 'b', 'c'],
 "N": ['e', 'f', 'g', 'l', 'c', 'b'],
 "O": ['e', 'f', 'a', 'b', 'c', 'd'],
 "P": ['e', 'f', 'a', 'b', 'k', 'p'],
 "Q": ['e', 'f', 'a', 'b', 'c', 'd', 'l'],
 "R": ['e', 'f', 'a', 'j', 'p', 'l'],
 "S": ['a', 'f', 'p', 'k', 'c', 'd'],
 "T": ['a', 'h', 'm'],
 "U": ['f', 'e', 'd', 'c', 'b'],
 "V": ['f', 'e', 'n', 'j'],
 "W": ['f', 'e', 'n', 'l', 'c', 'b'],
 "X": ['g', 'l', 'n', 'j'],
 "Y": ['g', 'j', 'm'],
 "Z": ['a', 'j', 'n', 'd'],
 "0": ['e', 'f', 'a', 'b', 'c', 'd'],
 "1": ['j', 'b', 'c'],
 "2": ['a', 'b', 'k', 'p', 'e', 'd'],
 "3": ['a', 'b', 'k', 'c', 'd'],
 "4": ['f', 'p', 'k', 'b', 'c'],
 "5": ['a', 'f', 'p', 'k', 'c', 'd'],
 "6": ['a', 'f', 'e', 'd', 'c', 'k', 'p'],
 "7": ['a', 'j', 'n'],
 "8": ['a', 'b', 'c', 'd', 'e', 'f', 'p', 'k'],
 "9": ['a', 'b', 'c', 'f', 'p', 'k'],
 " ": [],  # Space (all segments off)
 "\n": []  # Newline (ignored)
}

# Ordered segment names corresponding to FPGA segment layout
seg_names = "abcdefghjklmnp"

# Read input text from standard input
text = sys.stdin.read()

# Print Verilog local parameter for array size
print("    localparam pat_len = {};".format(len(text)))

# Declare Verilog array to hold display patterns
print("    wire [13:0] display_pat[0:pat_len-1];")

# Iterate through each character in the input text
for i in range(len(text)):
    segs = font[text[i]]  # Get segment list for the character
    comment = "  // {}".format(text[i]) if segs else ""  # Add comment with the character

    # Generate 14-bit binary representation (active-low: 0 = ON, 1 = OFF)
    bits = [(seg_names[k] in segs) for k in range(14)]
    bit_lit = "14'b" + "".join(reversed(["1" if b else "0" for b in bits]))

    # Print Verilog assignment statement
    print("    assign display_pat[{}] = {};{}".format(i, bit_lit, comment))
