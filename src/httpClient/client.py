import requests
import os
import shutil
from tkinter import messagebox

DIRECTUS_URL = os.getenv('DIRECTUS_URL')

global dump

def GetVersion():
    try:
        url = f'{DIRECTUS_URL}/items/Builds'
        response = requests.get(url).json()

        return response
    except Exception as error:
        return error
    
def GetFile(build_file):
    global dump
    try:
        url = f'{DIRECTUS_URL}/assets/{build_file}'
        file = requests.get(url, stream=True)
        dump = file.raw
    except Exception as error:
        return error

def DownloadFile(version, file_name):
    global dump

    full_file_name = 'v' + version + '-' + file_name
    location = os.path.abspath(f'./{full_file_name}.exe')

    try:

        with open(f'{full_file_name}.exe', 'wb') as location:
            shutil.copyfileobj(dump, location)
        del dump

        messagebox.showinfo('Informação', "Uma nova versão foi baixada")
    except Exception as error:
        return error
