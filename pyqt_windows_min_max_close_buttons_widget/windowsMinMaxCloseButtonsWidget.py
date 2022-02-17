from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import qApp, QMenuBar
from pyqt_min_max_close_buttons import MinMaxCloseButtonsWidget

from python_color_getter.pythonColorGetter import PythonColorGetter


class WindowsMinMaxCloseButtonsWidget(MinMaxCloseButtonsWidget):
    def __init__(self, menu_bar: QMenuBar, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__menu_bar = menu_bar
        self.__initUi(hint)

    def __initUi(self, hint):
        self._minimizeBtn.setText('🗕')
        self._maximizeBtn.setText('🗖')
        self._closeBtn.setText('🗙')

        btns = [self._minimizeBtn, self._maximizeBtn, self._closeBtn]

        menubar_base_color = self.__menu_bar.palette().color(QPalette.Base)
        menubar_base_color = menubar_base_color.lighter(150)

        lbl_r, lbl_g, lbl_b = PythonColorGetter.get_complementary_color(menubar_base_color.red(),
                                                                                          menubar_base_color.green(),
                                                                                          menubar_base_color.blue())
        btn_text_color = QColor(lbl_r, lbl_g, lbl_b)
        btn_text_hover_color = btn_text_color.lighter(150)

        tool_button_style = f'''
                            QToolButton
                            {{ 
                            background: transparent;
                            color: {btn_text_color.name()};
                            border: 0; 
                            }}
                            QToolButton:hover
                            {{ 
                            background-color: {menubar_base_color.name()};
                            color: {btn_text_hover_color.name()};
                            }}
                            '''

        close_button_style = f'''
                             QToolButton 
                             {{ 
                             background: transparent;
                             color: {btn_text_color.name()}; 
                             border: 0; 
                             }}
                             QToolButton:hover 
                             {{ 
                             background-color: #EE0000; 
                             color: {btn_text_hover_color.name()};
                             }}
                             '''

        font_size = qApp.font().pointSize() * 1.2

        for btn in btns:
            font = btn.font()
            font.setPointSize(font_size)
            btn.setFont(font)
            btn.setStyleSheet(tool_button_style)

        self._closeBtn.setStyleSheet(close_button_style)