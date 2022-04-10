from setuptools import setup

APP = ['timestamper.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'img/icon.icns',
    'plist': {
        'LSUIElement': True,
        'LSPrefersPPC': True
    },
    'packages': ['rumps', 'pynput'],
}

setup(
    name="Timestamper",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

