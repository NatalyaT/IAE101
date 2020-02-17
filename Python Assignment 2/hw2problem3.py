# Natalya Tulloch
# 112791014
# ntulloch
#
# IAE 101 (Fall 2019)
# HW 2, Problem 3

def reverse1(s):
    rs = ''
    for ch in s:
        rs = ch + rs
    return rs # CHANGE OR REMOVE THIS LINE

def reverse2(s):
    rs = s[::-1]
    return rs # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("reverse1(\"Mississippi\") is:", reverse1("Mississippi"))
    print()
    print("reverse2(\"Mississippi\") is:", reverse2("Mississippi"))
    print()
    print("reverse1(\"Connetquot\") is:", reverse1("Connetquot"))
    print()
    print("reverse2(\"Connetquot\") is:", reverse2("Connetquot"))
    print()
    print("reverse1(\"Wyandanch\") is:", reverse1("Wyandanch"))
    print()
    print("reverse2(\"Wyandanch\") is:", reverse2("Wyandanch"))
    print()
    print("reverse1(\"Ronkonkoma\") is:", reverse1("Ronkonkoma"))
    print()
    print("reverse2(\"Ronkonkoma\") is:", reverse2("Ronkonkoma"))
    print()
