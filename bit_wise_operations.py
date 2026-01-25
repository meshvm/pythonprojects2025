
# Bitwise operations

"""
Common Bitwise Operators and Their Actions The main bitwise operators are: Bitwise AND (&): Compares two bits and
 returns 1 only if both bits are 1; otherwise, it returns 0. This is often used for "masking" to check the value of
 specific bits.Example: 5 & 7 -> 0101 & 0111 -> 0101 (which is 5 in decimal).Bitwise OR (|): Compares two bits and
 returns 1 if at least one of the bits is 1; otherwise, it returns 0. This is used to set specific bits (flags) to 1.
 Example: 5 | 7 -> 0101 | 0111 -> 0111 (which is 7 in decimal).Bitwise XOR (^): Compares two bits and returns 1 if the
  bits are different (1 and 0 or 0 and 1); otherwise, it returns 0. It's useful for toggling bits or swapping variables.
  Example: 5 ^ 7 -> 0101 ^ 0111 -> 0010 (which is 2 in decimal).Bitwise NOT (~): A unary operator that inverts all the
   bits of a single operand, changing every 0 to 1 and every 1 to 0.
   Example: ~5 (in an 8-bit system) -> ~00000101 -> 11111010 (which is -6 in two's complement representation).
   Left Shift (<<): Shifts the bits of a number to the left by a specified number of positions,
    filling the newly vacated positions on the right with zeros. A left shift by n positions is equivalent to
    multiplying the original number by \(2^{n}\).Example: 5 << 1 -> 00000101 << 1 -> 00001010 (which is 10 in decimal).
    Right Shift (>>): Shifts the bits of a number to the right by a specified number of positions.
     A right shift by n positions is roughly equivalent to integer division by \(2^{n}\).
Example: 5 >> 1 -> 00000101 >> 1 -> 00000010 (which is 2 in decimal, with the last bit discarded)
"""
num = 12345
evenofnum = num & 1
orofnum = num | 1
notofnum = num ^ 1

print("Even Of Num: %s",evenofnum)
print("OR Of Num: %s",orofnum)
print("NOT Of Num: %s",notofnum)



# how to find a number is even with Modulus operation( %, /  or // )

def check_even(n):
    check = n & 1
    if check:
        return "ODD"
    else:
        return "EVEN"


print(check_even(n=345670))
