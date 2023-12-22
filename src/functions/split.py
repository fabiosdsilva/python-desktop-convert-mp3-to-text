import math
from pydub import AudioSegment
import sys
import os

PATH_FFMPEG = os.getenv('PATH_FFMPEG')

if not PATH_FFMPEG:
    PATH_FFMPEG = 'C:\\PATH_Programs\\ffmpeg.exe'

sys.path.append(PATH_FFMPEG)

class SplitMp3AudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + filename

        self.audio = AudioSegment.from_mp3(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename, folder_name):
        output_folder = "output"

        if not os.path.exists(folder_name + output_folder):
            os.makedirs(folder_name + output_folder)
        
        t1 = from_min * 900 * 1000
        t2 = to_min * 900 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + 'output/' +
                           split_filename, format="mp3")

    def multiple_split(self, min_per_split, folder_name):
        total_mins = math.ceil(self.get_duration() / 900)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn, folder_name)
            #print(str(i) + ' Done')
            # if i == total_mins - min_per_split:
            #     print('All splited successfully')
            #     pass
            
        return split_fn
