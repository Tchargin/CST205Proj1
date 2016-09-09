# Tyler Chargin Multimedia Programming Project 1 Taking the median pixels of a set of images & making a new image.
from statistics import median
from PIL import Image
# Declaring variables & Making new picture to store data
Images = []
R = []
G = []
B = []
Picture = Image.new('RGB', (495, 557))
Pixels = Picture.load()
# Getting files (Nathan helped me with loading the images b/c I did not know how to do it in python)
for pictures in range(1, 9):
        pic = Image.open("C:/Project1/" + str(pictures) + ".png")
        Images.append(pic)
# Getting pixels and taking the median
for x in range(495):
    for y in range(557):

        R.clear()
        G.clear()
        B.clear()

        for image in Images:
            Red, Green, Blue = image.getpixel((x, y))
            R.append(Red)
            G.append(Green)
            B.append(Blue)
        Median = (int(median(R)), int(median(G)), int(median(B)))
        Pixels[x, y] = Median
# Displaying picture
Picture.show()

# Github link: https://github.com/Tchargin/CST205Proj1/blob/master/Project%201.py
