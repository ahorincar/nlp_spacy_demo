from PyQt5 import QtWidgets, QtCore, QtGui

class DrawWords(QtWidgets.QWidget):
    def __init__(self, word_1, word_2, word_3):
        super(DrawWords, self).__init__()

        self.word_1 = word_1
        self.word_2 = word_2
        self.word_3 = word_3

        self.move(150,50)
        self.setFixedSize(900,500)
        self.startA    = 5
        self.endA      = 30
        self.linewidth = 1

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        paint.setBrush(QtCore.Qt.white)
        paint.drawRect(event.rect())

        first_circle = QtCore.QRect(70, 70, 250, 250)
        text_coord_x = 70 + (first_circle.width() - 40)/2
        text_coord_y = 70 + (first_circle.height() - 10)/2
        paint.setPen(QtCore.Qt.blue)
        paint.setBrush(QtCore.Qt.blue)
        paint.drawEllipse(first_circle)
        paint.setPen(QtCore.Qt.white)
        paint.drawText(text_coord_x, text_coord_y, self.word_1)

        second_circle = QtCore.QRect(390, 105, 200, 200)
        text_coord_x = 390 + (second_circle.width() - 40)/2
        text_coord_y = 105 + (second_circle.height() - 10)/2
        paint.setPen(QtCore.Qt.darkGreen)
        paint.setBrush(QtCore.Qt.darkGreen)
        paint.drawEllipse(second_circle)
        paint.setPen(QtCore.Qt.white)
        paint.drawText(text_coord_x, text_coord_y, self.word_2)

        third_circle = QtCore.QRect(660, 140, 150, 150)
        text_coord_x = 660 + (third_circle.width() - 40)/2
        text_coord_y = 140 + (third_circle.height() - 10)/2
        paint.setPen(QtCore.Qt.darkCyan)
        paint.setBrush(QtCore.Qt.darkCyan)
        paint.drawEllipse(third_circle)
        paint.setPen(QtCore.Qt.white)
        paint.drawText(text_coord_x, text_coord_y, self.word_3)
        paint.end()
