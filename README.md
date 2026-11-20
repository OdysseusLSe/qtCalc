# qtCalc

Calculator written with Python 3 and PySide 6

## Development recommendations

The app is written in Python3 (**version 3.15** and newer) and PySide6 (6.2 and
newer).

### Designer

All GUIs were desgned by Qt's Designer. To provide a consistent application
build I strongly recommend to tanslate the ui files to Python:

`pyside6-uic MainWindow.ui -o MainWindow_ui.py`

and

`pyside6-uic PlotWindow.ui -o PlotWindow_ui.py`

### Resources

To iclude all necessary resources you need the Qt resource system (`.qrc`)
provided by PySide6 from Qt: "pyside6-rcc" (included already in the "pyside6"
package):

`pyside6-rcc resources.qrc -o resources_rc.py`

This file contains all "styles" as text and the images as binary code.

### Build

To build a standalone app you need "pyinstaller". You have to install it first:

`pip install pyinstaller`

In the next step you have to change in the directory where "main.py" is and
execute the following line in a terminal:

macOS:\
`pyinstaller --windowed --icon=ui/icon.icns --name=qtCalc main.py`

Windows 11:\
`pyinstaller --noconsole --onefile --icon=ui/Calculator.ico main.py`
