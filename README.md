# pyqt-windows-min-max-close-buttons-widget
PyQt Windows min/max/close buttons widget

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-windows-min-max-close-buttons-widget.git --upgrade```

## Imported Package
* <a href="https://github.com/yjg30737/pyqt-min-max-close-buttons-widget.git">pyqt-min-max-close-buttons-widget</a> - Parent widget

## Usage
* ```WindowsMinMaxCloseButtonsWidget(base_widget: QWidget, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)``` - Constructor. The argument ```base_widget``` is used for matching the color of buttons with ```QWidget```(including ```QMenuBar```)'s base color.
* ```getMinimizedBtn()```, ```getMaximizedBtn()```, ```getCloseBtn()```.
* This module is used for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s Windows style button. You can see the example of this module's usage on the documentation at the link above.
