from PyQt6.QtCore import Qt, QEvent


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

        # Decoração da janela
        self.win.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # MINIMIZE
        self.win.minimizeAppBtn.clicked.connect(
            lambda: self.win.showMinimized())

        # MAXIMIZE/RESTORE
        self.win.maximizeRestoreAppBtn.clicked.connect(self.maximize_restore)

        # CLOSE APPLICATION
        self.win.closeAppBtn.clicked.connect(lambda: self.win.close())

    def maximize_restore(self):
        if self.win.windowState() == Qt.WindowState.WindowMaximized:
            self.win.setWindowState(Qt.WindowState.WindowNoState)
            self.win.showNormal()
            self.win.appMargins.setContentsMargins(5, 5, 5, 5)
        else:
            self.win.showMaximized()
            self.win.appMargins.setContentsMargins(0, 0, 0, 0)

        """if self.GLOBAL_STATE:
            self.GLOBAL_STATE = False
            self.win.showNormal()
            self.win.appMargins.setContentsMargins(5, 5, 5, 5)
        else:
            self.GLOBAL_STATE = True
            self.win.showMaximized()
            self.win.appMargins.setContentsMargins(0, 0, 0, 0)"""

    
