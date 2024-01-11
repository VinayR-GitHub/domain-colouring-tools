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
display.setGeometry(0, 0, 1024, 1024)
display.setWindowIcon(
    QtGui.QIcon(
        'assets/imgico.jpg'
    )
)

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
select_button1 = QPushButton(
    'Standard Plot'
)
select_button1.setStyleSheet('border: 2.5px solid "#26619C"')
select_button1.setCursor(
    QCursor(
        QtCore.Qt.PointingHandCursor
    )
)


select_button2 = QPushButton(
    'Plot with Modulus Contours'
)
select_button2.setStyleSheet('border: 2.5px solid "#26619C"')
select_button2.setCursor(
    QCursor(
        QtCore.Qt.PointingHandCursor
    )
)


select_button3 = QPushButton(
    'Plot with Phase/Modulus Contours'
)
select_button3.setStyleSheet('border: 2.5px solid "#26619C"')
select_button3.setCursor(
    QCursor(
        QtCore.Qt.PointingHandCursor
    )
)


select_button4 = QPushButton(
    'Multiple Plots'
)
select_button4.setStyleSheet('border: 2.5px solid "#26619C"')
select_button4.setCursor(
    QCursor(
        QtCore.Qt.PointingHandCursor
    )
)






#Display and exit window.
display.showMaximized()
sys.exit(
    myapp.exec()
)