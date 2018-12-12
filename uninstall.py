import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STARTUP_FOLDER = os.path.join(os.environ.get('USERPROFILE', None),
                              'AppData', 'Roaming', 'Microsoft',
                              'Windows', 'Start Menu', 'Programs',
                              'Startup'
                              )

try:
    os.remove(os.path.join(STARTUP_FOLDER, 'autostart.bat.lnk'))
    os.remove(os.path.join(BASE_DIR, 'autostart.bat'))
except FileNotFoundError:
    pass
