from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

from custom_grips import CustomGrip


class UIFunctions():
    GLOBAL_STATE = False

    def __init__(self, mainWindow) -> None:
        self.win = mainWindow

    def uiDefinitions(self):
        # Duplo click na headbar
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.Type.MouseButtonDblClick:
                self.maximize_restore()
        self.win.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.MouseButton.LeftButton:
                window = self.win.window().windowHandle()
                window.startSystemMove()
        self.win.titleRightInfo.mouseMoveEvent = moveWindow

        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self.win, Qt.Edge.LeftEdge, True)
        self.right_grip = CustomGrip(self.win, Qt.Edge.RightEdge, True)
        self.top_grip = CustomGrip(self.win, Qt.Edge.TopEdge, True)
        self.bottom_grip = CustomGrip(self.win, Qt.Edge.BottomEdge, True)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self.win)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.win.appMargins.setGraphicsEffect(self.shadow)

        # Decoração da janela
        self.win.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        ## ----- Botões ------ ##
        # MINIMIZE
        self.win.minimizeAppBtn.clicked.connect(
            lambda: self.win.showMinimized())

        # MAXIMIZE/RESTORE
        self.win.maximizeRestoreAppBtn.clicked.connect(self.maximize_restore)

        # CLOSE APPLICATION
        self.win.closeAppBtn.clicked.connect(lambda: self.win.close())

    def maximize_restore(self):
        if self.win.windowState() == Qt.WindowState.WindowMaximized:
            self.win.appMargins.setContentsMargins(5, 5, 5, 5)
            self.win.showNormal()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
        else:
            self.win.appMargins.setContentsMargins(0, 0, 0, 0)
            self.win.showMaximized()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()

    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.win.height())
        self.right_grip.setGeometry(self.win.width() - 10, 10, 10, self.win.height())
        self.top_grip.setGeometry(0, 0, self.win.width(), 10)
        self.bottom_grip.setGeometry(0, self.win.height() - 10, self.win.width(), 10)
