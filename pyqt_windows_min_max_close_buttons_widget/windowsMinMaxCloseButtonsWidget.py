from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QToolButton, qApp, QMenuBar

from python_color_getter.pythonColorGetter import PythonColorGetter


class WindowsMinMaxCloseButtonsWidget(QWidget):
    def __init__(self, menu_bar: QMenuBar, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__menu_bar = menu_bar
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self.__minimizeBtn = QToolButton()
        self.__maximizeBtn = QToolButton()
        self.__closeBtn = QToolButton()

    def __initUi(self, hint):
        self.__minimizeBtn.setText('🗕')
        self.__maximizeBtn.setText('🗖')
        self.__closeBtn.setText('🗙')

        btns = [self.__minimizeBtn, self.__maximizeBtn, self.__closeBtn]

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

        self.__closeBtn.setStyleSheet(close_button_style)

        lay = QHBoxLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        if hint == Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self.__minimizeBtn)
            lay.addWidget(self.__maximizeBtn)
            lay.addWidget(self.__closeBtn)
        elif hint == Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self.__minimizeBtn)
            lay.addWidget(self.__closeBtn)
        elif hint == Qt.WindowCloseButtonHint:
            lay.addWidget(self.__closeBtn)
        else:
            # todo for another type of flags
            pass

        self.setLayout(lay)

    def getMinimizedBtn(self):
        return self.__minimizeBtn

    def getMaximizedBtn(self):
        return self.__maximizeBtn

    def getCloseBtn(self):
        return self.__closeBtn

