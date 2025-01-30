from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys

if __name__ == "__main__":
    """
    Test script to verify PyQt6 installation.
    Creates a simple window displaying 'Hello World!'.
    """
    app = QApplication(sys.argv)

    # Create main application window
    window = QWidget()
    window.setWindowTitle("PyQt6 App")  # Set window title
    window.setGeometry(100, 100, 280, 80)  # Set window size and position

    # Add a label with a message
    helloMsg = QLabel("Hello World!", parent=window)
    helloMsg.move(100, 15)  # Position the label within the window

    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application event loop
