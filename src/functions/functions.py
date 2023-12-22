from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import *
from time import sleep
import asyncio
import shutil

from src.functions import split, transcribe

class AudioConverter:

    def upload(self):
        try:
            select_file = filedialog.askopenfilename()

            if select_file == '':
                return None

            file_name = select_file.split('/')[-1]
            file_name_mp3 = file_name.replace('.mp4', '.mp3')
            folder_name = select_file.replace(file_name, '')

            self.MP4ToMP3(select_file)

            audio_split = split.SplitMp3AudioMubin
            audio_split_formated = audio_split(folder_name, file_name_mp3).multiple_split(min_per_split=1, folder_name=folder_name)
            #print('Audfio folo', audio_split_formated)

            asyncio.run(transcribe.Transcribe.transcribe(folder_name, audio_split_formated))
            self.save_file(audio_split_formated.replace('.mp3', '.txt'), folder_name)

            sleep(4)
            shutil.rmtree(folder_name + 'output')
            os.remove(folder_name + file_name_mp3)
            return file_name
        except Exception as e:
            messagebox.showerror('Error', f"Error: {e}")

    def save_file(self, file_name, folder_name):
        save_file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text Files', '*.txt')], mode='w', initialfile=file_name)

        try:
            with open(folder_name + 'data/' + file_name, 'r+') as file:
                content = file.read()
                file.write('content')
            
            with open(save_file.name, 'w', encoding='utf-8') as output_file:
                output_file.write(content)

            shutil.rmtree(folder_name + 'data')

        except FileNotFoundError:
            messagebox.showerror('Error', f'Não encontrado: {file_name}')
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}')

    def MP4ToMP3(self, audio_path):
        VIDEO_FILE_PATH = audio_path
        AUDIO_FILE_PATH = audio_path.replace('.mp4', '.mp3')

        FILETOCONVERT = AudioFileClip(VIDEO_FILE_PATH)
        FILETOCONVERT.write_audiofile(AUDIO_FILE_PATH, logger=None)
        FILETOCONVERT.close()