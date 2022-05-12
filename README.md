# pyqt-windows-buttons-widget
PyQt Windows titlebar buttons (e.g. min/max/close button) widget

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-windows-buttons-widget.git --upgrade```

## Imported Package
* <a href="https://github.com/yjg30737/pyqt-titlebar-buttons-widget.git">pyqt-titlebar-buttons-widget</a> - Parent widget

## Usage
* `WindowsButtonsWidget(base_widget: QWidget, hint=['min', 'max', 'close'], font=QFont('Arial', 12))` - Constructor. The argument ```base_widget``` is used for matching the color of buttons with ```QWidget```(including ```QMenuBar```)'s base color. ```font``` argument is the font of each button's text.
* ```getMinimizedBtn()```, ```getMaximizedBtn()```, ```getCloseBtn()```.
* This module is used for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s Windows style button. You can see the example of this module's usage on the documentation at the link above.
