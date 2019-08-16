import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFontDialog, QFileDialog, QLabel, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFontMetrics
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PIL import Image, ImageDraw, ImageFont
import pygame
from Proyect_ui import*


class App(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonColor.clicked.connect(self.openColorDialog)
        self.actionNew_2.triggered.connect(self.insertImage)
        self.pushButton_AppendText.clicked.connect(self.WriteOnImage)
        self.textEdit.textChanged.connect(self.DisplayInLabel)
        self.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.spinBox.valueChanged.connect(self.size)

        self.myFont = self.fontComboBox.currentFont()
        self.Font = pygame.font.match_font(self.myFont.family())
        self.textEdit.setText("Write here")
        self.spinBox.setValue(11) #Tamaño de letra predeterminado en el textEdit.

    def openColorDialog(self):
        self.color = QColorDialog.getColor()
        self.textEdit.selectAll()
        self.textEdit.setTextColor(self.color)
#        print(self.color.name)
#        print(self.color)
#       print(self.color.standardColor())

    def changeFont(self):
        self.textEdit.selectAll()
        self.myFont = QtGui.QFont(self.fontComboBox.itemText(self.fontComboBox.currentIndex()))
        self.textEdit.setFont(self.myFont)
        self.textEdit.setFocus()
        self.l_TD.setText(self.textEdit.toHtml())
        self.l_TD.adjustSize()
        self.Font = pygame.font.match_font(self.myFont.family())
#        print(pygame.font.SysFont(self.myFont.family(), 11))
        print(self.Font)
        if self.Font==None:
            self.Font = "Ubuntu-R.ttf"

    def size(self):
        self.textEdit.selectAll()
        self.mySize=self.spinBox.value()
        self.textEdit.setFontPointSize(self.mySize)
#        print(self.textEdit.fontPointSize())

# Si es que agregamos un pushButton, abrimos una ventana secundaria.
##    def openFontDialog(self):
##        self.current=self.textEdit.currentFont()
##        self.font, self.ok = QFontDialog.getFont(self.current, self)
##        self.textEdit.selectAll()
##        self.info=QtGui.QFontInfo(self.font)
##        if self.ok:
##            self.textEdit.setCurrentFont(self.font)
##            print(self.font.toString())
##            print(self.info.family())
##            print(self.info.pointSize())


    def insertImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files, _ = QFileDialog.getOpenFileName(self, "Insertar Fondo", "", "All Files (*);Images Files (*.png *jpg)", options=options)
        if self.files:
#      print(files)
            self.im = Image.open(self.files)
            self.imW, self.imH = self.im.size
#            print(str(self.imW)+","+str(self.imH))
            self.coordx = self.imW / self.label.width()
            self.coordy = self.imH / self.label.height()
            self.im1 = self.im.resize((self.label.width(), self.label.height()), Image.ANTIALIAS)
            self.im1.save("Imagen1.png")
            self.image = QPixmap("Imagen1.png")
            self.label.setPixmap(self.image)

    def DisplayInLabel(self):
        self.l_TD.setMaximumWidth(self.label.width())
        self.l_TD.setMaximumHeight(self.label.height())
        self.l_TD.setText(self.textEdit.toHtml())
#        self.l_TD.setWordWrap(True)
        self.l_TD.adjustSize()

        xp = self.label.x() + (self.label.width()/2)
        yp = self.label.y() + (self.label.height()/2)
        self.l_TD.move(xp - (self.l_TD.width()/2), yp - (self.l_TD.height()/2))
        self.textEdit.setFocus()

        if self.l_TD.width() > (self.label.width()-10):
            self.l_TD.setGeometry(self.label.x() + 5, self.l_TD.y(), self.label.width() - 10, self.l_TD.height())
        if self.l_TD.height() > (self.label.height()-10):
            self.l_TD.setGeometry(self.l_TD.x(), self.label.y() + 5, self.l_TD.width(), self.label.height() - 10)



    def WriteOnImage(self):
        image = Image.open(self.files)
        draw = ImageDraw.Draw(image)
        size = (self.imW * self.imH * self.spinBox.value()) / (self.label.width() * self.label.height())
        font = ImageFont.truetype(self.Font, size=int(size))
        (x, y) = (self.coordx*self.l_TD.x(), self.coordy*self.l_TD.y())
        text = self.textEdit.toPlainText()
        rgb = (self.color.red(), self.color.green(), self.color.blue())
        color = "rgb(%d,%d,%d)" % rgb
        draw.text((x, y), text, fill=color, font=font)
        image.save('Imagen1.png')

        self.Preview = Preview(imag = 'Imagen1.png')

class Preview(QWidget):

    def __init__(self, imag=None):
        super().__init__()
        self.title = 'Preview'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.Image = imag
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(self.Image)
        label.setPixmap(pixmap)
        label.adjustSize()
        self.resize(pixmap.width(), pixmap.height())
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = App()
    w.show()
    app.exec_()