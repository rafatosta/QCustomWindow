from PyQt6.QtCore import QEvent


class UIFunctions():
    GLOBAL_STATE = False

    def __init__(self, mainWindow) -> None:
        self.win = mainWindow

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.Type.MouseButtonDblClick:
                self.maximize_restore()
        self.win.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

    def maximize_restore(self):
        if self.GLOBAL_STATE:
            self.GLOBAL_STATE = False
            self.win.showNormal()
        else:
            self.GLOBAL_STATE = True
            self.win.showMaximized()
