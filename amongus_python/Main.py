import amongUs
from win32api import GetSystemMetrics

# Just runs the lobby only
# tkinter gui with online button to run game is in Gui.py
if __name__ == "__main__":
    #first two numbers are lobby size and next two are map size
    code = amongUs.Game(1366, 768, 1368, 768)
    code.run()


