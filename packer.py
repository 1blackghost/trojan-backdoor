import sys
from cx_Freeze import setup, Executable

# Define the path to the main script and the application icon
main_script = 'main.py'
icon_file = 'icon.png'

# Define the shortcut information
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Ghostbusters",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]ghostbusters.exe",   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
]

# Define the build options
build_options = {
    'include_files': [icon_file],
    'create_shortcut': shortcut_table,
}

# Define the executable information
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(script=main_script,
                 base=base,
                 targetName='ghostbusters.exe',
                 icon=icon_file)

# Define the setup information
setup(name='Ghostbusters',
      version='1.0',
      description='A sample cx_Freeze script',
      options={'build_exe': build_options},
      executables=[exe])
