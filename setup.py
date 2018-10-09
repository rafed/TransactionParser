import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "c:\\Users\\Rafed\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "c:\\Users\\Rafed\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = "Win32GUI"    

# executables = [Executable("fileChoosingScreen.py", base=base, shortcutName="Bank Parser", shortcutDir="DesktopFolder")]
executables = [Executable("fileChoosingScreen.py", base=base)]

packages = ["idna", "tkinter", "os", "fpdf", "lxml", "datetime", "sys"]


shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Transaction Parser",     # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]fileChoosingScreen.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

options = {
    'build_exe': {    
        'packages':packages,
        "include_files": ["tcl86t.dll", "tk86t.dll", "parser.png"]
    },
    "bdist_msi": bdist_msi_options,
}

# setup(
#     options = {
#         "bdist_msi": bdist_msi_options,
#     },
#     )

setup(
    name = "Transaction Parser",
    version = "1.0",
    description = 'Bank transaction XML parser',
    author='IIT BSSE 07',
    author_email='bsse0733@iit.du.ac.bd',
    url='http://iit.du.ac.bd',
    options = options,
    executables = executables
)

