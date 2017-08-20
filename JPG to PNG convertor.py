"""
SHARED UNDER MIT LICENSE

INSTALL NOTICE:
    - Written for Python 2
    - Needs PIL (Python Imaging Library)
        - Download from: http://www.pythonware.com/products/pil/#pil117
        - Install
        - Enjoy
"""

import Image
import os
# converting functions (are called on later in the script)

def imageconvertor(infile, savelocation, name):
    sourcefile = Image.open(infile)
    dimension = sourcefile.size
    width = dimension[0]
    height = dimension[1]
    print "processing: "+ filename
#Detecting and modding file dimensions (only resized if W or H are > 2048px)
    if width > 2048 or width > 2048:
        if height > width:          #Portraitorientation   (Calc OK)
            newwidth = width/(height/2048.0)
            newwidth = int(newwidth)
            newdim = (newwidth,2048)
        else:                       #Landscapeorietnation
            newheight = height/(width/2048.0)
            newheight = int(newheight)
            newdim = (2048,newheight)
    else:
        newdim = (width,height)
    newfile = sourcefile.resize(newdim, Image.ANTIALIAS)
    newfile.save(savelocation+"\\"+name+".png","PNG")



# Asking the folder you want to convert; and creates an output folder if it's not there.
folder = raw_input("Paste the path of the folder containing the JPEGS you want to convert: ")
target = folder+"\output"
isthere = os.path.exists(target)
if isthere == False:
    os.mkdir(folder+"\output")

if folder[-1] != "\\":
    folder = folder+"\\"


for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        try:
            extension = filename.split(".")[1]
            name_of_file = filename.split(".")[0]
            extension = extension.lower()
            fullpath = folder+filename

            if extension == "jpg" or extension == "jpeg":
                imageconvertor(fullpath, target, name_of_file)
            elif extension == "png":
                imageconvertor(fullpath, target, name_of_file)
            else:
                print "files with a ."+extension+" extension are not supported at this time."
                succeedded = succeedded+1
        except:
            pass #To ignore newly created files.
            #print "Couldn't handle file: "+fullpath
