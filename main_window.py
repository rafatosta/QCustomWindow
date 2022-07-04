from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt5.QtWidgets import QDesktopWidget
import sys
import os

from ui_functions import UIFunctions


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        self.ui_func = UIFunctions(self)
        self.ui_func.uiDefinitions()
        

    def initBasicUi(self):
        """Window decoration settings """
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowMinMaxButtonsHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    """def resizeEvent(self, e):
        if self.windowState() == Qt.WindowState.WindowMaximized:
            self.ui_func.maximize_restore()
            print(self.windowState())
        print('----')"""


def main():
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
