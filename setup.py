import PyInstaller.__main__
import os
import shutil

shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)

if os.path.exists('main.spec'):
    os.remove('main.spec')

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '--clean'
])