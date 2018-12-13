import os
import winshell


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STARTUP_FOLDER = os.path.join(os.environ.get('USERPROFILE', None),
                              'AppData', 'Roaming', 'Microsoft',
                              'Windows', 'Start Menu', 'Programs',
                              'Startup'
                              )


# 1. Generate commands
commands = [
    '@echo off\n',
    ' '.join(['explorer.exe', BASE_DIR, '\n']),
    ' '.join(['cd', BASE_DIR, '\n']),
    'autostart.exe'
]

# 2. Write commands to bat file
bat_file = open(os.path.join(BASE_DIR, 'autostart.bat'), 'w')
bat_file.writelines(commands)
bat_file.close()

# 3. create shortcut
with winshell.shortcut(os.path.join(STARTUP_FOLDER, 'autostart.bat.lnk')) as shortcut:
    shortcut.path = os.path.join(BASE_DIR, 'autostart.bat')
    shortcut.description = 'Cold Boot auto shutdown part'
    shortcut.working_directory = BASE_DIR
