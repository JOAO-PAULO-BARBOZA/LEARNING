blocks = int(input("Enter the number of blocks: "))
height = 0
while True:
    height += 1
    blocks = blocks - height
    if blocks < height + 1:
        break

print("The height of the pyramid:", height)
