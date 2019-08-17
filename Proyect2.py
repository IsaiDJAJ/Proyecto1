import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFontDialog, QFileDialog, QLabel, QSizePolicy, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFontMetrics
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtGui import QColor
from PIL import Image, ImageDraw, ImageFont
import pygame
from Proyect1_ui import*

class App(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setScaledContents(True)
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setVisible(True)

        self.myFont = self.fontComboBox.currentFont()
        self.Font = pygame.font.match_font(self.myFont.family())
        self.spinBox.setValue(11)  # Tamaño de letra predeterminado en el textEdit.

        self.actionNew_2.triggered.connect(self.insertImage)
        self.pushButtonColor.clicked.connect(self.openColorDialog)
        self.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.spinBox.valueChanged.connect(self.size)
        self.textEdit.textChanged.connect(self.DisplayInLabel)
        self.pushButton_AppendText.clicked.connect(self.WriteOnImage)

    def openColorDialog(self):
        self.color = QColorDialog.getColor()
        self.textEdit.selectAll()
        self.textEdit.setTextColor(self.color)

    def changeFont(self):
        self.textEdit.selectAll()
        self.myFont = QtGui.QFont(self.fontComboBox.itemText(self.fontComboBox.currentIndex()))
        self.textEdit.setFont(self.myFont)
        self.textEdit.setFocus()
        self.l_TD.setText(self.textEdit.toHtml())
        self.l_TD.adjustSize()
        self.Font = pygame.font.match_font(self.myFont.family())
##        print(pygame.font.SysFont(self.myFont.family(), 11))
        print(self.Font)
        if self.Font == None:
            self.Font = "Ubuntu-R.ttf" #Este se debe cambiar por el predeterminado (depende de la maquina)

    def size(self):
        self.textEdit.selectAll()
        self.mySize=self.spinBox.value()
        self.textEdit.setFontPointSize(self.mySize)

    def insertImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.files, _ = QFileDialog.getOpenFileName(self, "Insertar Fondo", "", "All Files (*);Images Files (*.png *jpg)", options=options)
        if self.files:
#      print(files)
            self.im = QImage(self.files)
            self.label.setPixmap(QPixmap.fromImage(self.im))
            self.scrollArea.setWidgetResizable(False)
            self.label.adjustSize()
            self.label.move(-1, -1)
            self.scrollAreaWidgetContents.resize(self.im.width(), self.im.height())
#            self.scrollArea.setVisible(True)
            self.xp = self.im.width() / 2
            self.yp = self.im.height() / 2
            print(str(self.xp), str(self.yp))
            self.l_TD.move(self.xp - (self.l_TD.width() * 0.5), self.yp - (self.l_TD.height() * 0.5))
            print(str(self.l_TD.width()/2), str(self.l_TD.height()/2))
            print(str(self.l_TD.x()), str(self.l_TD.y()))
            print(str(self.l_TD.pos()))

    def DisplayInLabel(self):
        self.l_TD.setMaximumWidth(self.scrollAreaWidgetContents.width()-10)
        self.l_TD.setMaximumHeight(self.scrollAreaWidgetContents.height()-10)
        self.l_TD.setText(self.textEdit.toHtml())
#        print(self.textEdit.toHtml())
##        self.l_TD.setWordWrap(True)
        self.l_TD.adjustSize()

        if self.label.x() < 0 and self.label.y() < 0:
            self.l_TD.move(self.xp - (self.l_TD.width() * 0.5), self.yp - (self.l_TD.height() * 0.5))

        self.textEdit.setFocus()

#        if self.l_TD.width() > (self.label.width()-10):
#            self.l_TD.setGeometry(self.label.x() + 5, self.l_TD.y(), self.label.width() - 10, self.l_TD.height())
#        if self.l_TD.height() > (self.label.height()-10):
#            self.l_TD.setGeometry(self.l_TD.x(), self.label.y() + 5, self.l_TD.width(), self.label.height() - 10)

    def WriteOnImage(self):
        image = Image.open(self.files)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.Font, size=int(self.spinBox.value()+5))
        (x, y) = (self.l_TD.x()+3, self.l_TD.y())
        text = self.textEdit.toPlainText()
#        text = self.label.text()
        print(self.label.text())
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
        self.resize(pixmap.width(), pixmap.height())
        print(str(pixmap.width()), str(pixmap.height()))
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = App()
    w.show()
    app.exec_()