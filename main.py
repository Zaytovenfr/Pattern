rows = int(input("How many rows: "))
# TODO:  Ask the user for how many rows.
#   And store it in a variable called rows

for row in range(1, rows + 1):
    for star in range(1, row + 1):
        print("* ")
    print("stuff ", end="")