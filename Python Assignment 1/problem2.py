# Natalya Tulloch
# 112791014
# ntulloch
#
# IAE 101 (Fall 2019)
# HW 1, Problem 2

def tip_amount(bill, good_service):
    if bill <= 30:
        tipAmount = 5
    elif bill > 30 and good_service == True:
        tipAmount = (bill * .25) + bill
    elif bill > 30 and good_service == False:
        tipAmount = (bill * .15) + bill
    return tipAmount # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("tip_amount(23.37,True) is", tip_amount(23.37, True))
    print()
    print("tip_amount(23.37,False) is", tip_amount(23.37, False))
    print()
    print("tip_amount(81.75,True) is", tip_amount(81.75, True))
    print()
    print("tip_amount(63.59,True) is", tip_amount(63.59, True))
    print()
    print("tip_amount(63.59,False) is", tip_amount(63.59, False))
    print()
