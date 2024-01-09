import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

#Initialise app and window.
myapp = QApplication(sys.argv)
display = QWidget()

#Initialise window features.
display.setWindowTitle('Domain Colouring Tools')
display.setStyleSheet('background: #191213;')
display.setBaseSize(1024, 1024)

#Initialise coordinate system.
coords = QGridLayout()
display.setLayout(coords)

#Set up image.
home_image = QLabel()
home_image.setPixmap(
    QPixmap(
        'assets/imghome.jpg'
    )
)
home_image.setAlignment(QtCore.Qt.AlignCenter)
coords.addWidget(home_image, 0, 0)

#Create button options.











#Display and exit window.
display.showMaximized()
sys.exit(
    myapp.exec()
)