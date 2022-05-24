from PyQt5.QtWidgets import QWidget
from pyqt_titlebar_buttons_widget import TitlebarButtonsWidget


class WindowsButtonsWidget(TitlebarButtonsWidget):
    def __init__(self, base_widget: QWidget, hint: list = ['min', 'max', 'close']):
        super().__init__(base_widget, hint)
        self.__initUi()

    def __initUi(self):
        self._minimizeBtn.setText('🗕')
        self._maximizeBtn.setText('🗖')
        self._closeBtn.setText('🗙')

        self.__window = self._base_widget.window()
        self.__window.installEventFilter(self)

    def _styleInit(self):
        super()._styleInit()
        close_button_style = self._closeBtn.styleSheet() + f'''
                             QPushButton:hover
                             {{ 
                             background-color: #EE0000; 
                             color: #ffffff;
                             }}
                             QPushButton:pressed
                             {{
                             background-color: #CC0000;
                             }}
                             '''

        self._closeBtn.setStyleSheet(close_button_style)

    def eventFilter(self, obj, e):
        if e.type() == 105:
            if self.__window.isMaximized():
                self._maximizeBtn.setText('🗗')
            else:
                self._maximizeBtn.setText('🗖')
        return super().eventFilter(obj, e)
