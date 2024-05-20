line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

Map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?(Use A,B,C to specify along the row and 1,2,3 to specify "
                 "along the column. So example input can be like A2) = ")

coordinate1 = position[0]
if coordinate1 == "A":
    coordinate1 = 0
elif coordinate1 == "B":
    coordinate1 = 1
else:
    coordinate1 = 2
coordinate2 = int(position[1]) - 1

Map[coordinate2][coordinate1] = 'X'

print(f"{line1}\n{line2}\n{line3}")
