from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget
from pyqt_min_max_close_buttons_widget import MinMaxCloseButtonsWidget

from python_color_getter.pythonColorGetter import PythonColorGetter


class WindowsMinMaxCloseButtonsWidget(MinMaxCloseButtonsWidget):
    def __init__(self, base_widget: QWidget, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint, font=QFont('Arial', 12)):
        super().__init__(hint)
        self.__baseWidget = base_widget
        self.__initUi(hint, font)

    def __initUi(self, hint, font):
        self.layout().setSpacing(0)

        self._minimizeBtn.setText('🗕')
        self._maximizeBtn.setText('🗖')
        self._closeBtn.setText('🗙')

        btns = [self._minimizeBtn, self._maximizeBtn, self._closeBtn]

        base_color = self.__baseWidget.palette().color(QPalette.Base)
        base_conspicuous_color = base_color.lighter(150)

        lbl_r, lbl_g, lbl_b = PythonColorGetter.get_complementary_color(base_conspicuous_color.red(),
                                                                        base_conspicuous_color.green(),
                                                                        base_conspicuous_color.blue())
        btn_text_color = QColor(lbl_r, lbl_g, lbl_b)
        btn_text_hover_color = btn_text_color.lighter(150)

        tool_button_style = f'''
                            QPushButton
                            {{ 
                            background: {base_color.name()};
                            color: {btn_text_color.name()};
                            border: 0; 
                            }}
                            QPushButton:hover
                            {{ 
                            background-color: {base_conspicuous_color.name()};
                            color: {btn_text_hover_color.name()};
                            }}
                            '''

        close_button_style = f'''
                             QPushButton 
                             {{ 
                             background: {base_color.name()};
                             color: {btn_text_color.name()}; 
                             border: 0; 
                             }}
                             QPushButton:hover 
                             {{ 
                             background-color: #EE0000; 
                             color: {btn_text_hover_color.name()};
                             }}
                             '''

        font_size = font.pointSize() // 1.2

        for btn in btns:
            font = btn.font()
            font.setPointSize(font_size)
            btn.setFont(font)
            btn.setStyleSheet(tool_button_style)

        self._closeBtn.setStyleSheet(close_button_style)