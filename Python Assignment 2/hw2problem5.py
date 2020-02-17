# Natalya Tulloch
# 112791014
# ntulloch
#
# IAE 101 (Fall 2019)
# HW 2, Problem 5

def is_palindrome(s):
    pal = True
    i = 0
    s = ''.join(s.split())
    r = s[::-1]
    while i < len(s):
        if s[i] != r[i]:
            pal = False
            break
        i += 1
    return pal


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = is_palindrome("racecar")
    print("is_palindrome(\"racecar\") is:", test1)
    print()
    test2 = is_palindrome("raceboat")
    print("is_palindrome(\"raceboat\") is:", test2)
    print()
    test3 = is_palindrome("a man a plan a canal panama")
    print("is_palindrome(\"a man a plan a canal panama\") is:", test3)
    print()
    test4 = is_palindrome("a place to call up")
    print("is_palindrome(\"a place to call up\") is:", test4)
    print()
    test5 = is_palindrome("deified")
    print("is_palindrome(\"deified\") is:", test5)
    print()

