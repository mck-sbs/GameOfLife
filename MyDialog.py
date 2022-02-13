#start designer with qt5-tools designer

from PyQt5.QtGui import QPen, QBrush

from GOL import *
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QGraphicsView, QSlider, QLabel, QPushButton

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        uic.loadUi("Design.ui", self)
        self.__gv = self.findChild(QGraphicsView, "graview")
        self.__scene = QtWidgets.QGraphicsScene()
        self.__gv.setScene(self.__scene)
        self.__side = 10
        self.__row = 70
        self.__isRunning = False
        self.__speed = 1
        self.__gen = 0
        self.__rand = 50


        self.__slr_speed = self.findChild(QSlider, "sldr_speed")
        self.__slr_random = self.findChild(QSlider, "sldr_random")
        self.__lbl_gen = self.findChild(QLabel, "lbl_gen")
        self.__btn_startStop = self.findChild(QPushButton, "btn_startStop")

        self.__btn_startStop.clicked.connect(self.startStopGol)
        self.__slr_speed.valueChanged.connect(self.setSpeed)
        self.__slr_random.valueChanged.connect(self.setRandom)

        self.resetScene()

    def setSpeed(self, sp):
        self.__speed = sp

    def setRandom(self, r):
        self.__rand = r

    def resetScene(self):
        self.__scene.clear()
        #pen = QtGui.QPen(QtCore.Qt.cyan)
        pen = QtGui.QPen(QtCore.Qt.darkRed)
        for i in range(self.__row):
            for j in range(self.__row):
                r = QtCore.QRectF(QtCore.QPointF(i*self.__side, j*self.__side), QtCore.QSizeF(self.__side, self.__side))
                self.__scene.addRect(r, pen)


    def setList(self, lst):
        self.__gen = self.__gen + 1
        self.resetScene()

        self.__lbl_gen.setText(str(self.__gen))

        self.__pen = QtGui.QPen(QtCore.Qt.green)

        for i in range(len(lst)):
            for j in range(len(lst[0])):
                if(lst[i][j]):

                    pen = QtGui.QPen()
                    #brush = QBrush(QtCore.Qt.green)
                    brush = QBrush(QtCore.Qt.red)

                    r = QtCore.QRectF(QtCore.QPointF(i * self.__side, j * self.__side),
                                      QtCore.QSizeF(self.__side, self.__side))
                    self.__scene.addRect(r, pen, brush)

    def startStopGol(self):

        if(self.__isRunning == False):
            self.__gen = 0

            self.__lbl_gen.setText(str(self.__gen))
            self.__gol = GOL(self.__row, self.__speed, self.__rand)
            self.resetScene()
            self.__gol.sendList.connect(self.setList)

            self.__gol.start()
            self.__isRunning = True
            self.__btn_startStop.setText('stop')
            self.__slr_speed.setEnabled(False)
            self.__slr_random.setEnabled(False)
        else:
            self.__gol.terminate()
            self.__isRunning = False
            self.__btn_startStop.setText('start')
            self.__slr_speed.setEnabled(True)
            self.__slr_random.setEnabled(True)






