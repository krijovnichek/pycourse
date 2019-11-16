import os
import enzyme
from PIL import Image
from PIL.ExifTags import TAGS


os.system('cls') # Clear Terminal

dirPath = os.path.dirname(__file__)
path = os.path.join(dirPath, "testPath")
filename = "file.mkv"

tfile = os.path.join(path, filename)
print (tfile)
# print (tfile)

with open(tfile, 'rb') as f:
    info = enzyme.MKV(f)

print (info)

# print (list(TAGS.values()))   

# #  Walk through path
# for root, dirs, files in os.walk(path):
#     print(root)
#     for _dir in dirs:
#         print(_dir)
 
#     for _file in files:
#         print(_file)
        