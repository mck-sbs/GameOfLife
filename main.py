import sys
from MyDialog import *

app = QtWidgets.QApplication(sys.argv)
window = MyDialog()
window.show()
sys.exit(app.exec())
