import os
import enzyme
from pymediainfo import MediaInfo
os.system('cls') # Clear Terminal

dirPath = os.path.dirname(__file__)
path = os.path.join(dirPath, "testPath")
filename = "file.mkv"
tfile = os.path.join(path, filename)
print ("Path: "+tfile)

mediaInfo = MediaInfo.parse(tfile)
for track in mediaInfo.tracks:
    if track.track_type == 'Video':
        print (track.frame_rate, int(track.duration)/1000) 