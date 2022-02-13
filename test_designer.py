#start designer with qt5-tools designer
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        uic.loadUi("Design.ui", self)


app = QtWidgets.QApplication(sys.argv)
window = MyDialog()
window.show()
sys.exit(app.exec())
