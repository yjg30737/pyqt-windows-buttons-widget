# pyqt-windows-min-max-close-buttons-widget
PyQt Windows min/max/close buttons widget

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-windows-min-max-close-buttons-widget.git --upgrade```

## Imported Package
* <a href="https://github.com/yjg30737/pyqt-min-max-close-buttons-widget.git">pyqt-min-max-close-buttons-widget</a> - Parent widget

## Usage
* ```WindowsMinMaxCloseButtonsWidget(menu_bar: QMenuBar, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)``` - Constructor. The argument ```menu_bar``` is used for matching the color of buttons with menu bar's base color.
* ```getMinimizedBtn()```, ```getMaximizedBtn()```, ```getCloseBtn()```.
* This module is used for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s Windows style button. You can see the example of this module's usage on the documentation at the link above.
  
## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_mac_min_max_close_buttons_widget import MacMinMaxCloseButtonsWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MacMinMaxCloseButtonsWidget()
    widget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/154260566-706ae34f-37c5-42db-ab8d-90d0d58341db.png)

