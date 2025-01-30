from PyQt6.QtGui import QPen, QBrush
from PyQt6.QtWidgets import QGraphicsView, QSlider, QLabel, QPushButton, QDialog, QGraphicsScene
from PyQt6.QtCore import Qt, QRectF, QPointF, QSizeF
from PyQt6 import uic
from GOL import GOL


class MyDialog(QDialog):
    """
    Main dialog for Conway's Game of Life. Provides UI controls and visualization for the game.
    """

    def __init__(self):
        """
        Initialize the dialog and connect UI elements.
        """
        super(MyDialog, self).__init__()
        uic.loadUi("Design.ui", self)  # Load the UI design

        # Find UI elements in the loaded UI file
        self.__gv = self.findChild(QGraphicsView, "graview")  # Graphics view for the grid
        self.__scene = QGraphicsScene()  # Create a new graphics scene
        self.__gv.setScene(self.__scene)  # Assign the scene to the graphics view

        # Set initial properties
        self.__side = 10  # Size of each cell in the grid
        self.__row = 70  # Number of rows and columns in the grid
        self.__isRunning = False  # Simulation running state
        self.__speed = 1  # Simulation speed
        self.__gen = 0  # Generation counter
        self.__rand = 50  # Randomness factor for initial grid state

        # Connect UI controls
        self.__slr_speed = self.findChild(QSlider, "sldr_speed")  # Slider for speed
        self.__slr_random = self.findChild(QSlider, "sldr_random")  # Slider for randomness
        self.__lbl_gen = self.findChild(QLabel, "lbl_gen")  # Label to display the generation count
        self.__btn_startStop = self.findChild(QPushButton, "btn_startStop")  # Start/Stop button

        # Connect signals to slots
        self.__btn_startStop.clicked.connect(self.startStopGol)  # Toggle simulation start/stop
        self.__slr_speed.valueChanged.connect(self.setSpeed)  # Update speed when slider changes
        self.__slr_random.valueChanged.connect(self.setRandom)  # Update randomness when slider changes

        self.resetScene()  # Initialize the grid scene

    def setSpeed(self, sp):
        """
        Update simulation speed based on slider value.
        :param sp: New speed value from the slider
        """
        self.__speed = sp

    def setRandom(self, r):
        """
        Update randomness factor for the initial grid generation.
        :param r: New randomness percentage from the slider
        """
        self.__rand = r

    def resetScene(self):
        """
        Clear and redraw the grid scene with empty cells.
        """
        self.__scene.clear()  # Clear the existing scene
        pen = QPen(Qt.GlobalColor.darkRed)  # Pen for cell borders
        for i in range(self.__row):
            for j in range(self.__row):
                # Create rectangles for each grid cell
                rect = QRectF(QPointF(i * self.__side, j * self.__side), QSizeF(self.__side, self.__side))
                self.__scene.addRect(rect, pen)  # Add rectangles to the scene

    def setList(self, lst):
        """
        Update the grid visualization with the new grid state.
        :param lst: The updated grid state
        """
        self.__gen += 1  # Increment the generation counter
        self.resetScene()  # Clear the scene
        self.__lbl_gen.setText(str(self.__gen))  # Update the generation label

        pen = QPen()  # Pen for active cells
        brush = QBrush(Qt.GlobalColor.red)  # Brush for filling active cells

        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if lst[i][j]:  # If the cell is alive
                    rect = QRectF(QPointF(i * self.__side, j * self.__side), QSizeF(self.__side, self.__side))
                    self.__scene.addRect(rect, pen, brush)  # Add a filled rectangle to the scene

    def startStopGol(self):
        """
        Start or stop the Game of Life simulation.
        """
        if not self.__isRunning:
            # Start the simulation
            self.__gen = 0  # Reset generation count
            self.__lbl_gen.setText(str(self.__gen))  # Update the generation label
            self.__gol = GOL(self.__row, self.__speed, self.__rand)  # Create a new simulation instance
            self.resetScene()  # Clear the grid
            self.__gol.sendList.connect(self.setList)  # Connect the simulation output to the UI

            self.__gol.start()  # Start the simulation thread
            self.__isRunning = True
            self.__btn_startStop.setText("stop")  # Update button text
            self.__slr_speed.setEnabled(False)  # Disable speed slider
            self.__slr_random.setEnabled(False)  # Disable randomness slider
        else:
            # Stop the simulation
            self.__gol.terminate()  # Terminate the simulation thread
            self.__isRunning = False
            self.__btn_startStop.setText("start")  # Update button text
            self.__slr_speed.setEnabled(True)  # Enable speed slider
            self.__slr_random.setEnabled(True)  # Enable randomness slider
