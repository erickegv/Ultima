from setuptools import setup

setup(
    app=['descargadorVideo.py'],
    data_files=[('images', ['meme.icns'])],
    options={'py2app': {'argv_emulation': True, 'packages': ['tkinter', 'PIL', 'yt_dlp', 'subprocess']}},
    setup_requieres=['py2app'],
)
