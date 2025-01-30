from PyQt6.QtCore import QObject, pyqtSignal, QThread
import time
import random
import copy

class GOL(QThread):
    """
    Game of Life simulation engine running in a separate thread.
    Emits updated grid states to the UI.
    """

    # Signal to send the updated grid state
    sendList = pyqtSignal(list)

    def __init__(self, cnt, sp, rnd):
        """
        Initialize the Game of Life engine.

        :param cnt: Grid size (rows and columns)
        :param sp: Simulation speed
        :param rnd: Random seed for initial grid generation
        """
        super().__init__()
        self.__speed = sp
        self.__random = rnd
        self.__running = False
        self.__cnt = cnt
        self.__lst = [[0] * cnt for _ in range(cnt)]

    def run(self):
        """
        Main simulation loop. Updates the grid state periodically based on speed.
        """
        while True:
            time.sleep(1.0 / self.__speed)  # Wait based on simulation speed
            self.newGen()  # Generate the next grid state
            self.sendList.emit(self.__lst)  # Emit the updated grid

    def newGen(self):
        """
        Generate the next state of the grid based on the rules of Conway's Game of Life.
        """
        if not self.__running:
            # Initialize the grid randomly
            self.__running = True
            for i in range(len(self.__lst)):
                for j in range(len(self.__lst[0])):
                    self.__lst[i][j] = random.randint(0, 100) < self.__random
        else:
            # Compute the next generation
            lst = [[0] * self.__cnt for _ in range(self.__cnt)]

            for i in range(len(self.__lst)):
                for j in range(len(self.__lst[0])):
                    counter = 0

                    # Horizontal and vertical neighbors
                    if i > 0 and self.__lst[i-1][j]:
                        counter += 1
                    if i < self.__cnt - 1 and self.__lst[i+1][j]:
                        counter += 1
                    if j > 0 and self.__lst[i][j-1]:
                        counter += 1
                    if j < self.__cnt - 1 and self.__lst[i][j+1]:
                        counter += 1

                    # Diagonal neighbors
                    if i > 0 and j > 0 and self.__lst[i-1][j-1]:
                        counter += 1
                    if i > 0 and j < self.__cnt - 1 and self.__lst[i-1][j+1]:
                        counter += 1
                    if i < self.__cnt - 1 and j > 0 and self.__lst[i+1][j-1]:
                        counter += 1
                    if i < self.__cnt - 1 and j < self.__cnt - 1 and self.__lst[i+1][j+1]:
                        counter += 1

                    # Apply rules of Conway's Game of Life
                    if self.__lst[i][j]:
                        # Cell stays alive if it has 2 or 3 neighbors
                        lst[i][j] = counter in (2, 3)
                    else:
                        # Dead cell becomes alive if it has exactly 3 neighbors
                        lst[i][j] = counter == 3

            self.__lst = copy.deepcopy(lst)  # Update the grid
