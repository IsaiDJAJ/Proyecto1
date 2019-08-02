import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFontDialog, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PIL import Image, ImageDraw, ImageFont
from Proyect_ui import*

class App(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonColor.clicked.connect(self.openColorDialog)
        self.actionNew_2.triggered.connect(self.insertImage)
        self.pushButton_AppendText.clicked.connect(self.WriteOnImage)
        self.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.textEdit.setText("Write here")
        self.spinBox.setValue(11)
        self.spinBox.valueChanged.connect(self.size)

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
#        self.Font=QtGui.QFontDataBase.systemFont(self.myFont)
#        print(self.Font)
#        print(self.textEdit.font())
#        print(self.textEdit.fontFamily())
#        print(self.myFont)
#        print(self.myFont.toString())
#        print("")

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
            self.im1 = self.im.resize((self.label.width(), self.label.height()), Image.ANTIALIAS)
            self.im1.save("Imagen1.png")
            self.image = QPixmap("Imagen1.png")
            self.label.setPixmap(self.image)

    def WriteOnImage(self):
        image = Image.open(self.files)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("Ubuntu-B.ttf", size=self.spinBox.value())
#        font = ImageFont.truetype("Tengo que obtener el archivo .ttf del FontComboBox", size=self.spinBox.value())
        (x, y) = (100, 170)
        text = self.textEdit.toPlainText()
        rgb = (self.color.red(), self.color.green(), self.color.blue())
        color = "rgb(%d,%d,%d)" % rgb
        draw.text((x, y), text, fill=color, font=font)
        image.save('Imagen1.png')
        self.im = Image.open('Imagen1.png')
        self.im1 = self.im.resize((self.label.width(), self.label.height()), Image.ANTIALIAS)
        self.im1.save("Imagen1.png")
        self.im2 = QPixmap("Imagen1.png")
        self.label.setPixmap(self.im2)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = App()
    w.show()
    app.exec_()