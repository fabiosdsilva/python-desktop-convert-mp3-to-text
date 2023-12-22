from tkinter import messagebox
import openai
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
api_key = OPENAI_API_KEY
openai.api_key = api_key

class Transcribe:

    async def transcribe(folder_name ,file_audio):
        output_dir = folder_name + 'output'
        data_dir = folder_name + 'data'
        #print(data_dir)

        try:
            files = os.listdir(output_dir)

            if not os.path.exists(folder_name + 'data'):
                os.makedirs(data_dir)

            for file in files:
                #print(f"Transcribing {file}")
                audio_cwd = folder_name + 'output/' + file
                audio_file = open(audio_cwd, 'rb')
                transcript = openai.Audio.transcribe('whisper-1', audio_file)

                with open(data_dir + '/' + file_audio.replace('.mp3', '') + '.txt', "a") as txt_file:
                    txt_file.write(transcript['text'] + '\n')

            #print('Transcrição concluída!')
        except Exception as e:
            messagebox.showerror('Error', f"Erro ao transcrever o áudio: {e}")

