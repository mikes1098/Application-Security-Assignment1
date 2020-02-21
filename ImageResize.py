# -*- coding: utf-8 -*-
""" Resizing an image to a square """

from PIL import Image
import sys

#Resizes PNG image to a square with specified dimensions, while maintaining aspect ratio
#If no dimensions requested, defaults to 400
def resize(path, dimension=400):
    imageToResize = open(path,'rb')
    img = Image.open(imageToResize)
    newimg = img.resize((dimension,dimension))
    newimg.save(path,newimg.format)
    print("Square Resize Completed!")

#Takes path to image and requested dimensions as first and second argument        
def main():
    if len(sys.argv)==3:
        resize(sys.argv[1],int(sys.argv[2]))
    else:
        resize(sys.argv[1])
        
main()