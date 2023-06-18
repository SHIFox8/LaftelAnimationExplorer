from cx_Freeze import setup, Executable

setup(
    name='라프텔 애니 탐색기',
    version='1.0',
    description='배고프네여',
    executables=[Executable('gui_laftell.py')]
)