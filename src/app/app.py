from time import sleep
from dotenv import load_dotenv
load_dotenv()

from tkinter import *
from customtkinter import *

from src.functions import functions
from src.app import version
from src.httpClient import client

upload_file = functions.AudioConverter().upload
current_version = version.get_version()

class ConverterApp:
    def __init__(self):

        if not self.check_version():
            pass

        self.app = CTk()
        self.app.resizable(False, False)

        #set_appearance_mode('light')
        self.upload_file = CTkButton(
            self.app, text='Buscar arquivo',
            corner_radius=32,
            fg_color='#02B885',
            hover_color='#026C85',
            command=upload_file,
            width=200,
            height=40,
        )
        self.upload_file.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.app.title("Converter MP3 para texto")

        self.version_label = CTkLabel(self.app, text=f'v{current_version}', font=("Helvetica", 10), anchor="w")
        self.version_label.place(relx=0, rely=1, anchor=SW)

        window_height = 120
        window_width = 400

        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        self.app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    def run(self):
        self.app.mainloop()

    def check_version(self):
        release = ''
        feature = ''
        fix = ''

        try:
            get_new_version = client.GetVersion()
            get_old_version = version.get_version()

            for i in range(len(get_new_version['data'])):
                release = get_new_version['data'][i]['release']
                feature = get_new_version['data'][i]['feature']
                fix = get_new_version['data'][i]['fix']

                full_version = f'{release}.{feature}.{fix}'

                if full_version > get_old_version:
                    client.GetFile(get_new_version['data'][i]['build_file'])
                    client.DownloadFile(full_version, 'main')
                    
                    sleep(4)
                    
        except Exception:
            return False
