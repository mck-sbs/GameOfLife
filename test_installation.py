from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel('Hello World!', parent=window)
helloMsg.move(100, 15)

window.show()

sys.exit(app.exec_())