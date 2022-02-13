from PyQt5.QtCore import QObject, pyqtSignal, QThread
import time
import random
import copy

class GOL(QThread):

    sendList = pyqtSignal(list)

    def __init__(self, cnt, sp, rnd):
        super().__init__()
        self.__speed = sp
        self.__random = rnd
        self.__running = False
        self.__cnt = cnt
        self.__lst = [ [0]*cnt for i in range(cnt)]


    def run(self):
        while(True):
            time.sleep(1. / self.__speed)
            self.newGen()
            self.sendList.emit(self.__lst)


    def newGen(self):
        if(self.__running == False):
            self.__running = True
            for i in range(len(self.__lst)):
                for j in range(len(self.__lst[0])):
                    if random.randint(0, 100) < self.__random:
                        self.__lst[i][j] = True
                    else:
                        self.__lst[i][j] = False
        else:
            lst = [[0] * self.__cnt for i in range(self.__cnt)]


            for i in range(len(self.__lst)):
                for j in range(len(self.__lst[0])):
                    counter = 0

                    # to be optimized

                    # horizonzal + vertical check and count
                    if i > 0:
                        if self.__lst[i-1][j] == True:
                            counter = counter + 1
                    if i < self.__cnt - 1:
                        if self.__lst[i+1][j] == True:
                            counter = counter + 1
                    if j > 0:
                        if self.__lst[i][j-1] == True:
                            counter = counter + 1
                    if j < self.__cnt - 1:
                        if self.__lst[i][j+1] == True:
                            counter = counter + 1

                    # diagonal check and count
                    if i > 0 and j > 0:
                        if self.__lst[i-1][j-1] == True:
                            counter = counter + 1
                    if i > 0 and j < self.__cnt - 1:
                        if self.__lst[i-1][j+1] == True:
                            counter = counter + 1
                    if i < self.__cnt - 1 and j > 0:
                        if self.__lst[i+1][j-1] == True:
                            counter = counter + 1
                    if i < self.__cnt - 1 and j < self.__cnt - 1:
                        if self.__lst[i+1][j+1] == True:
                            counter = counter + 1


                    # check for life
                    if self.__lst[i][j] == True:
                        if counter == 2 or counter == 3:
                            lst[i][j] = True
                        else:
                            lst[i][j] = False
                    else:
                        if counter == 3:
                            lst[i][j] = True
                        else:
                            lst[i][j] = False

            self.__lst = copy.deepcopy(lst)


