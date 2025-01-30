import sys
from MyDialog import MyDialog
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    """
    Entry point for the Conway's Game of Life application.
    Initializes the application and shows the main dialog.
    """
    app = QApplication(sys.argv)
    window = MyDialog()  # Create the main dialog instance
    window.show()  # Display the dialog
    sys.exit(app.exec())  # Start the application event loop
