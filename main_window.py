from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import os

from ui_functions import UIFunctions


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        self.ui_func = UIFunctions(self)
        self.ui_func.uiDefinitions()
    
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        self.ui_func.resize_grips()


def main():
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
