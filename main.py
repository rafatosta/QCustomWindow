from PyQt6.QtWidgets import QApplication
import sys, os

from main_window import MainWindow


def main():
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()