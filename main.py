import sys
from PyQt6.QtWidgets import QApplication

from authWindow import AuthWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth_win = AuthWindow()
    sys.exit(app.exec())
