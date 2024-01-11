import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

#Initialise global widgets dict.
gwdict = {
    'home_image': [],
    'select_button1': [],
    'select_button2': [],
    'select_button3': [],
    'select_button4': [],
    'base_info': [],
    'sel1': [],
    'sel2': [],
    'sel3': [],
    'sel4': [],
    'sel1': [],
    'sel2': [],
    'sel3': [],
    'sel4': [],
    'sel1': [],
    'sel2': [],
    'sel3': [],
    'sel4': [],
    'sel1': [],
    'sel2': [],
    'sel3': [],
    'sel4': [],
    'sel1': [],
    'sel2': [],
    'sel3': [],
    'sel4': [],
}

#Initialise app and window.
myapp = QApplication(sys.argv)
display = QWidget()

#Initialise window features.
display.setWindowTitle('Domain Colouring Tools')
display.setStyleSheet('background: #191213;')
display.setWindowIcon(
    QtGui.QIcon(
        'assets/imgico.jpg'
    )
)

#Initialise coordinate system.
coords = QGridLayout()
display.setLayout(coords)

def home_window():
    #Set up image.
    home_image = QLabel()
    home_image.setPixmap(
        QPixmap(
            'assets/imghome.jpg'
        ).scaled(512, 512, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

    )
    home_image.setAlignment(QtCore.Qt.AlignCenter)
    home_image.setStyleSheet('margin: 0;')
    gwdict ['home_image'].append(home_image)
    coords.addWidget(
        gwdict ['home_image'] [-1],
        0,
        0,
        1,
        4
    )

    ########################################

    #Create button options.
    select_button1 = QPushButton(
        'Standard Plot'
    )
    select_button1.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button1.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button1'].append(select_button1)
    coords.addWidget(
        gwdict ['select_button1'] [-1],
        2,
        0
    )

    select_button2 = QPushButton()
    select_button2.setText('Plot with Modulus Contours')
    select_button2.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button2.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button2'].append(select_button2)
    coords.addWidget(
        gwdict ['select_button2'] [-1],
        2,
        1
    )

    select_button3 = QPushButton()
    select_button3.setText('Plot with Phase/Modulus Contours')
    select_button3.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button3.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button3'].append(select_button3)
    coords.addWidget(
        gwdict ['select_button3'] [-1],
        2,
        2
    )

    select_button4 = QPushButton()
    select_button4.setText('Multiple Plots')
    select_button4.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button4.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button4'].append(select_button4)
    coords.addWidget(
        gwdict ['select_button4'] [-1],
        2,
        3
    )

    ########################################

    #Add infotext.
    base_info = QLabel()
    base_info.setText(
        '''<p>Domain colouring is one of the key tools used in complex analysis, and presents great opportunities to aid and accelerate mathematical research.</p>
        <p>With this tool, a variety of complex functions can be plotted on their domain, in a variety of different styles.</p>
        <p>The tool also has native support for a variety of special functions, such as modified Bessel functions of the first kind.</p>
        <p>To see my other projects, visit my 
        <a href = "https://github.com/VinayR-GitHub" name = "VinayR-GitHub" class = "hl">GitHub</a> <!--Shameless self promotion-->
         or my 
        <a href = "https://vinayr-github.github.io/" name = "VinayR's Website" class = "hl">website</a>.</p>'''
    )
    base_info.setStyleSheet(
        '* {margin-top: 0;' +
        'color: "#FFFFFF";' +
        'font-size: 20px;}' +
        'a {color: "#40E0D0";}'
    )
    base_info.setAlignment(QtCore.Qt.AlignCenter)
    base_info.setOpenExternalLinks(True)
    gwdict ['base_info'].append(base_info)
    coords.addWidget(
        gwdict ['base_info'] [-1],
        1,
        0,
        1,
        4
    )

def sel_1_entry():
    pass

def sel_2_entry():
    pass

def sel_3_entry():
    pass

def sel_4_entry():
    pass


home_window()


#Display and exit window.
display.showMaximized()
sys.exit(
    myapp.exec()
)