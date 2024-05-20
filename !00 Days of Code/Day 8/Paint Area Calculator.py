# Instructions You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square
# meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height x wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
#
# number of cans = (2 * 4) / 5
#                = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# A way to solve the above problem is to use int() function to type case the float number. To do that properly add
# 0.9 to the number because int(4.4) = 4 and int(4.6) = 4
# Here we can only round upwards so round function won't be of any help

def paint_calc(height, width, cover):
    print(f"You'll need {int((height * width / cover) + 0.9)} cans of paint.")


test_h = int(input("Enter the Height of your wall - "))  # Height of wall (m)
test_w = int(input("Enter the Width of your wall - "))  # Width of wall (m)
coverage = int(input("Enter the coverage of your paint can - "))
paint_calc(height=test_h, width=test_w, cover=coverage)
