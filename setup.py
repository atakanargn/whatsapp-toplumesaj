from cx_Freeze import setup, Executable

import main

options = {
    'build_exe': {
        'includes': ['easygui','base64','threading','requests','os','PyQt5.QtWidgets','PyQt5.QtGui','main', 'cx_Logging','PyQt5','PyQt5.QtCore','traceback','datetime','functools'],
        'include_files':['./fav.ico']
    }
}

executables = [
    Executable('main.py',
    base='Win32Gui',
            targetName='TopluMesaj.exe',
            icon="fav.ico")
]

setup(name='TopluMesaj',
    version='0.1',
    description='Toplu Mesaj',
    executables=executables,
    options=options
)