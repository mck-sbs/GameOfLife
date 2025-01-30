import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic

class MyDialog(QDialog):
    """
    Test dialog for verifying UI design loading.
    """
    def __init__(self):
        super(MyDialog, self).__init__()
        uic.loadUi("Design.ui", self)  # Load the UI file

if __name__ == "__main__":
    """
    Entry point for testing the UI design.
    """
    app = QApplication(sys.argv)
    window = MyDialog()  # Create the dialog instance
    window.show()  # Show the dialog
    sys.exit(app.exec())  # Execute the application
