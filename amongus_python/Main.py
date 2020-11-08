import amongUs
from win32api import GetSystemMetrics

# Just runs the lobby only
# tkinter gui with online button to run game is in Gui.py
if __name__ == "__main__":
    code = amongUs.Game(695, 530, GetSystemMetrics(0), GetSystemMetrics(1))
    code.run()


