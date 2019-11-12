import os
from PIL import Image
from PIL.ExifTags import TAGS


os.system('cls') # Clear Terminal




path = r"D:\Projects\Ruslan\dev\pycourse\testPath" # Test files folder
filename = "file1.jpg"
tfile = os.path.join(path, filename)


print (list(TAGS.values()))   
print ("hello")


##  Walk through path
# for root, dirs, files in os.walk(path):
#     print(root)
#     for _dir in dirs:
#         print(_dir)
 
#     for _file in files:
#         print(_file)
        