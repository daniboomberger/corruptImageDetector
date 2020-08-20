import os
from PIL import Image

picture_file_endings = ['*.jpg', '*.gif', '*.bmp', '*.png', '*.svg', '*.jpeg', '.*jif', '*.webp', '*.tiff', '*.raw']

'''
function to get files of from inputed folder path
'''
def get(path):
    files = os.listdir(path)
    for pic in files:
        if checkFileEnding(pic) == 1:
            print(checkImg(pic))

'''
checks with pillow libary if image is corrupt and prints corrupt file name out
'''
def checkImg(pic): 
    try: 
        img = Image.open(pic)
        img.verify()
    except:
        count += count + 1
        print(pic)

'''
checks for image file endings
'''
def checkFileEnding(pic): 
    for i in range(0, len(picture_file_ending) - 1): 
        if picture_file_endings[i] in pic: 
            return 1
    return 0

def main():
    path = input("Enter Folder Path: ")
    get(path)

main()
