import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pathlib
import numpy

def create_img(path: pathlib.Path):
    img = mpimg.imread(path)
    colors = set()
    palettelegal = set()
    ispalettespace = True
    ispaletteblock = True
    for col, line in enumerate(img):
        for row, pixel in enumerate(line):
            pixel = tuple(pixel)
            if ispalettespace and (row == 0 or ispaletteblock) and pixel[3] != 0.0:
                ispaletteblock = True
                palettelegal.add(pixel)
                print(pixel)
            else:
                ispaletteblock = False
            if ispaletteblock and row == 0 and pixel[3] == 0.0:
                ispalettespace = False
            if pixel != (0.0, 0.0, 0.0, 0.0):
                colors.add(pixel)

    for col, line in enumerate(img):
        for row, pixel in enumerate(line):
            pixel = tuple(pixel)
            if pixel != (0.0, 0.0, 0.0, 0.0) and pixel[3] != 1.0:
                print("Translucent pixel at ", col, "x", row)
                print(type(col))
                newpix = numpy.ndarray((4,))
                newpix[0] = 0.0
                newpix[1] = 1.0
                newpix[2] = 0.0
                newpix[3] = 1.0
                img[col][row] = newpix
            elif len(palettelegal) != 0 and pixel != (0.0, 0.0, 0.0, 0.0) and pixel not in palettelegal:
                newpix = numpy.ndarray((4,))
                newpix[0] = 0.0
                newpix[1] = 0.0
                newpix[2] = 1.0
                newpix[3] = 1.0
                img[col][row] = newpix
    print(len(colors), "colors")
    print(len(palettelegal), "palette colors")
    #print(palettelegal)
    return img


if __name__ == "__main__":
    #while True:
        img = create_img(pathlib.Path(input()))
        plt.imshow(img)
        plt.show()