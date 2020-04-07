'''
Created on Mar 10, 2019
@author: Burkhard A. Meier
'''




import sys
from PyQt5 import QtWidgets, QtGui
from Designer_code.Video1_1_CSS_no_Design import Ui_MainWindow


class RunDesignerGUI():
    """Wrapper class for PyQT modularization"""
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.update_widgets()
        self.widget_actions()

        self.MainWindow.show()
        sys.exit(app.exec_())

    def widget_actions(self):
        """Define widegt actions"""
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)    # correct relative path to icon
        self.ui.actionNew.setIcon(icon)
        self.ui.actionNew.setShortcut('Ctrl+N')

        self.ui.actionExit.setStatusTip('Click to exit the application')        # use ui reference to update status bar
        self.ui.actionExit.triggered.connect(self.close_GUI)                    # connect widget to method when clicked
        self.ui.actionExit.setShortcut('Ctrl+Q')                                # keyboard shortcut, window has focus

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)   # modify icon location
        self.ui.actionExit.setIcon(icon1)                                                            # use: self.ui.

    def close_GUI(self):
        """auxiliary method to close GUI"""
        self.MainWindow.close()         # call MainWindow close method, which closes the GUI

    def update_widgets(self):
        """Update widgets"""
        self.MainWindow.setWindowTitle('PyQt5 GUI')           # use: self.MainWindow
        # self.ui.pushButton.setText('New Button text')       # use: self.ui to access widgets


if __name__ == "__main__":
    RunDesignerGUI()
    