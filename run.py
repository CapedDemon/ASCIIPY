from helpers import *

if __name__ == "__main__":
    path = input("Enter the path of the image : ")

    newWidth = int(input("Enter width: "))

    mainName = input(
        "Enter a name of file in which the image will be stored: ")
    filename1 = mainName + ".txt"
    filename2 = mainName + ".jpg"

    targetImage = Image.open(path)
    newImg = pixelAscii(graying(imageResize(targetImage, newWidth)))

    pixels = (len(newImg))
    asciiLetters = "\n".join(newImg[i:(i+newWidth)]
                             for i in range(0, pixels, newWidth))

    f = open(filename1, "w")
    f.write(asciiLetters)
    f.close()

    asciiimg = text_to_img(filename1)
    asciiimg.save(filename2)