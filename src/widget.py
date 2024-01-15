import sys
sys.dont_write_bytecode = True

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QSlider, QLineEdit, QDial, QToolButton
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

#Initialise global widgets dict.
gwdict = {
    'home_image': [],
    'select_button1_img': [],
    'select_button2_img': [],
    'select_button3_img': [],
    'select_button4_img': [],
    'select_button1_txt': [],
    'select_button2_txt': [],
    'select_button3_txt': [],
    'select_button4_txt': [],
    'base_info': [],
    'sel1box': [],
    'sel2box': [],
    'sel3box': [],
    'sel4box': [],
    'sel1idbox': [],
    'sel2idbox': [],
    'sel3idbox': [],
    'sel4idbox': [],
    'sel1func': [],
    'sel2func': [],
    'sel3func': [],
    'sel4func': [],
    'sel1funclab': [],
    'sel2funclab': [],
    'sel3funclab': [],
    'sel4funclab': [],
    'sel1funckey': [],
    'sel2funckey': [],
    'sel3funckey': [],
    'sel4funckey': [],
    'sel1sat': [],
    'sel2sat': [],
    'sel3sat': [],
    'sel4sat': [],
    'sel1acu': [],
    'sel2acu': [],
    'sel3acu': [],
    'sel4acu': [],
    'sel2contour': [],
    'sel4contour': []
}

#Create a rect-box-selection widget (customised).
class QRectangleSelect(QWidget):
    def __init__(self, title, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.layout = QGridLayout() 
        self.setLayout(self.layout) 
        self.slider1 = QSlider()
        self.slider2 = QSlider()
        self.slider3 = QSlider()
        self.slider4 = QSlider()
        self.title = QLabel()
        self.title.setText(title)
        self.label1 = QLabel()
        self.label1.setText('Lower Real')
        self.label2 = QLabel()
        self.label2.setText('Upper Real')
        self.label3 = QLabel()
        self.label3.setText('Lower Imaginary')
        self.label4 = QLabel()
        self.label4.setText('Upper Imaginary')
        self.layout.addWidget(
            self.title,
            0,
            0,
            1,
            4
        )
        self.layout.addWidget(
            self.label1,
            2,
            0
        )
        self.layout.addWidget(
            self.label2,
            2,
            1
        )
        self.layout.addWidget(
            self.label3,
            2,
            2
        )
        self.layout.addWidget(
            self.label4,
            2,
            3
        )
        self.layout.addWidget(
            self.slider1,
            1,
            0
        )
        self.layout.addWidget(
            self.slider2,
            1,
            1
        )
        self.layout.addWidget(
            self.slider3,
            1,
            2
        )
        self.layout.addWidget(
            self.slider4,
            1,
            3
        )

#Initialise app and window.
myapp = QApplication(sys.argv)
display = QWidget()

#Initialise window features.
display.setWindowTitle('Domain Colouring Tools')
display.setStyleSheet('background: #0F0F00;')
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

    #Create button options.
    select_button1_img = QPushButton()
    select_button1_txt = QPushButton()
    select_button1_txt.setText('Standard Plot')
    button1_img = QtGui.QIcon('assets/continuousglimpse.png')
    select_button1_img.setIcon(button1_img)
    select_button1_img.setIconSize(
        QtCore.QSize(200, 200)
    )
    select_button1_txt.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619C";}'
    )
    select_button1_txt.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button1_txt'].append(select_button1_txt)
    coords.addWidget(
        gwdict ['select_button1_txt'] [-1],
        2,
        0
    )
    select_button1_img.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619C";}'
    )
    select_button1_img.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button1_img'].append(select_button1_img)
    coords.addWidget(
        gwdict ['select_button1_img'] [-1],
        3,
        0
    )

    select_button2_img = QPushButton()
    select_button2_txt = QPushButton()
    select_button2_txt.setText('Plot with Modulus Contours')
    button2_img = QtGui.QIcon('assets/modulusglimpse.png')
    select_button2_img.setIcon(button2_img)
    select_button2_img.setIconSize(
        QtCore.QSize(200, 200)
    )
    select_button2_txt.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button2_txt.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button2_txt'].append(select_button2_txt)
    coords.addWidget(
        gwdict ['select_button2_txt'] [-1],
        2,
        1
    )
    select_button2_img.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button2_img.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button2_img'].append(select_button2_img)
    coords.addWidget(
        gwdict ['select_button2_img'] [-1],
        3,
        1
    )

    select_button3_img = QPushButton()
    select_button3_txt = QPushButton()
    select_button3_txt.setText('Plot with Phase/Modulus Contours')
    button3_img = QtGui.QIcon('assets/MPglimpse.png')
    select_button3_img.setIcon(button3_img)
    select_button3_img.setIconSize(
        QtCore.QSize(200, 200)
    )
    select_button3_txt.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button3_txt.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button3_txt'].append(select_button3_txt)
    coords.addWidget(
        gwdict ['select_button3_txt'] [-1],
        2,
        2
    )
    select_button3_img.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button3_img.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button3_img'].append(select_button3_img)
    coords.addWidget(
        gwdict ['select_button3_img'] [-1],
        3,
        2
    )

    select_button4_img = QPushButton()
    select_button4_txt = QPushButton()
    select_button4_txt.setText('Multiple Plots')
    button4_img = QtGui.QIcon('assets/universalglimpse.png')
    select_button4_img.setIcon(button4_img)
    select_button4_img.setIconSize(
        QtCore.QSize(200, 200)
    )
    select_button4_txt.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button4_txt.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button4_txt'].append(select_button4_txt)
    coords.addWidget(
        gwdict ['select_button4_txt'] [-1],
        2,
        3
    )
    select_button4_img.setStyleSheet(
        '* {border: 2.5px solid "#26619C";' +
        'border-radius: 45px;' +
        'color: "#FFFFFF";' +
        'font-size: 30px;' +
        'margin: 0 10px;' +
        'padding: 30px 15px;}' +
        '*:hover {background-color: "#26619c";}'
    )
    select_button4_img.setCursor(
        QCursor(
            QtCore.Qt.PointingHandCursor
        )
    )
    gwdict ['select_button4_img'].append(select_button4_img)
    coords.addWidget(
        gwdict ['select_button4_img'] [-1],
        3,
        3
    )


    #Add infotext.
    base_info = QLabel()
    base_info.setText(
        '''<p>Domain colouring is one of the key tools used in complex analysis, and presents great opportunities to aid and accelerate mathematical research.</p>
        <p>With this tool, a variety of complex functions can be plotted on their domain, in a variety of different styles.</p>
        <p>The tool also has native support for a variety of special functions, such as the zeta and polygamma functions.</p>
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
    # Acuity (integer text)

    # Box (ReL, ReU, ImL, ImU) (rectselect)
    sel1box = QRectangleSelect('Function Domain')
    sel1box.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel1box'].append(sel1box)
    coords.addWidget(
        gwdict ['sel1box'] [-1],
        0,
        0,
        4,
        1
    )

    # Identity Box (ReL, ReU, ImL, ImU) (rectselect))
    sel1idbox = QRectangleSelect('Identity Domain')
    sel1idbox.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel1idbox'].append(sel1idbox)
    coords.addWidget(
        gwdict ['sel1idbox'] [-1],
        0,
        1,
        4,
        1
    )

    #Label (function)
    sel1funclab = QLabel()
    sel1funclab.setText('Function:')
    gwdict ['sel1funclab'].append(sel1funclab)
    coords.addWidget(
        gwdict ['sel1funclab'] [-1],
        0,
        2
    )

    # Function (text)
    sel1func = QLineEdit()
    sel1func.setText('f(z) = ')
    gwdict ['sel1func'].append(sel1func)
    coords.addWidget(
        gwdict ['sel1func'] [-1],
        0,
        3
    )

    # Saturation (dial)
    sel1sat = QDial()
    sel1sat.setMaximum(10) # x10
    sel1sat.setMinimum(1) #x10
    sel1sat.setValue(10) #x10
    sel1sat.setNotchesVisible(True)
    gwdict ['sel1sat'].append(sel1sat)
    coords.addWidget(
        gwdict ['sel1sat'] [-1],
        1,
        3
    )
    
    #Label (accepted functions)
    with open('src/accepted_functions.txt') as func_file:
        acc = func_file.readlines()
    sel1funckey = QLabel()
    sel1funckey.setText(
        ''.join(
            (
                term.split(' --> ') [0] + '\n'
            ) for term in acc
        ) [: -1]
    )
    gwdict ['sel1funckey'].append(sel1funckey)
    coords.addWidget(
        gwdict ['sel1funckey'] [-1],
        0,
        4
    )


def sel_2_entry():
    # Acuity (integer text)
    # Contour Base (slider)

    # Box (ReL, ReU, ImL, ImU) (rectselect)
    sel2box = QRectangleSelect('Function Domain')
    sel2box.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel2box'].append(sel2box)
    coords.addWidget(
        gwdict ['sel2box'] [-1],
        0,
        0,
        4,
        1
    )

    # Identity Box (ReL, ReU, ImL, ImU) (rectselect)
    sel2idbox = QRectangleSelect('Function Domain')
    sel2idbox.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel2idbox'].append(sel2idbox)
    coords.addWidget(
        gwdict ['sel2idbox'] [-1],
        0,
        1,
        4,
        1
    )

    #Label (function)
    sel2funclab = QLabel()
    sel2funclab.setText('Function:')
    gwdict ['sel2funclab'].append(sel2funclab)
    coords.addWidget(
        gwdict ['sel2funclab'] [-1],
        0,
        2
    )

    # Function (text)
    sel2func = QLineEdit()
    sel2func.setText('f(z) = ')
    gwdict ['sel2func'].append(sel2func)
    coords.addWidget(
        gwdict ['sel2func'] [-1],
        0,
        3
    )

    # Saturation (dial)
    sel2sat = QDial()
    sel2sat.setMaximum(10) # x10
    sel2sat.setMinimum(1) #x10
    sel2sat.setValue(10) #x10
    sel2sat.setNotchesVisible(True)
    gwdict ['sel2sat'].append(sel2sat)
    coords.addWidget(
        gwdict ['sel2sat'] [-1],
        1,
        3
    )

    #Label (accepted functions)
    with open('src/accepted_functions.txt') as func_file:
        acc = func_file.readlines()
    sel2funckey = QLabel()
    sel2funckey.setText(
        ''.join(
            (
                term.split(' --> ') [0] + '\n'
            ) for term in acc
        ) [: -1]
    )
    gwdict ['sel2funckey'].append(sel2funckey)
    coords.addWidget(
        gwdict ['sel2funckey'] [-1],
        0,
        4
    )

def sel_3_entry():
    # Acuity (integer text)

    # Box (ReL, ReU, ImL, ImU) (rectselect)
    sel3box = QRectangleSelect('Function Domain')
    sel3box.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel3box'].append(sel3box)
    coords.addWidget(
        gwdict ['sel3box'] [-1],
        0,
        0,
        4,
        1
    )

    # Identity Box (ReL, ReU, ImL, ImU) (rectselect)
    sel3idbox = QRectangleSelect('Function Domain')
    sel3idbox.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel3idbox'].append(sel3idbox)
    coords.addWidget(
        gwdict ['sel3idbox'] [-1],
        0,
        1,
        4,
        1
    )

    #Label (function)
    sel3funclab = QLabel()
    sel3funclab.setText('Function:')
    gwdict ['sel3funclab'].append(sel3funclab)
    coords.addWidget(
        gwdict ['sel3funclab'] [-1],
        0,
        2
    )

    # Function (text)
    sel3func = QLineEdit()
    sel3func.setText('f(z) = ')
    gwdict ['sel3func'].append(sel3func)
    coords.addWidget(
        gwdict ['sel3func'] [-1],
        0,
        3
    )

    # Saturation (dial)
    sel3sat = QDial()
    sel3sat.setMaximum(10) # x10
    sel3sat.setMinimum(1) #x10
    sel3sat.setValue(10) #x10
    sel3sat.setNotchesVisible(True)
    gwdict ['sel3sat'].append(sel3sat)
    coords.addWidget(
        gwdict ['sel3sat'] [-1],
        1,
        3
    )

    #Label (accepted functions)
    with open('src/accepted_functions.txt') as func_file:
        acc = func_file.readlines()
    sel3funckey = QLabel()
    sel3funckey.setText(
        ''.join(
            (
                term.split(' --> ') [0] + '\n'
            ) for term in acc
        ) [: -1]
    )
    gwdict ['sel3funckey'].append(sel3funckey)
    coords.addWidget(
        gwdict ['sel3funckey'] [-1],
        0,
        4
    )

def sel_4_entry():
    # Acuity (integer text)
    # Contour Base (slider)

    # Box (ReL, ReU, ImL, ImU) (rectselect)
    sel4box = QRectangleSelect('Function Domain')
    sel4box.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel4box'].append(sel4box)
    coords.addWidget(
        gwdict ['sel4box'] [-1],
        0,
        0,
        4,
        1
    )

    # Identity Box (ReL, ReU, ImL, ImU) (rectselect)
    sel4idbox = QRectangleSelect('Function Domain')
    sel4idbox.setStyleSheet(
        '* {border: 3px solid "#FFFFFF";' +
        'border-radius: 3px;}'
    )
    gwdict ['sel4idbox'].append(sel4idbox)
    coords.addWidget(
        gwdict ['sel4idbox'] [-1],
        0,
        1,
        4,
        1
    )

    #Label (function)
    sel4funclab = QLabel()
    sel4funclab.setText('Function:')
    gwdict ['sel4funclab'].append(sel4funclab)
    coords.addWidget(
        gwdict ['sel4funclab'] [-1],
        0,
        2
    )

    # Function (text)
    sel4func = QLineEdit()
    sel4func.setText('f(z) = ')
    gwdict ['sel4func'].append(sel4func)
    coords.addWidget(
        gwdict ['sel4func'] [-1],
        0,
        3
    )

    # Saturation (dial)
    sel4sat = QDial()
    sel4sat.setMaximum(10) # x10
    sel4sat.setMinimum(1) #x10
    sel4sat.setValue(10) #x10
    sel4sat.setNotchesVisible(True)
    gwdict ['sel4sat'].append(sel4sat)
    coords.addWidget(
        gwdict ['sel4sat'] [-1],
        1,
        3
    )

    #Label (accepted functions)
    with open('src/accepted_functions.txt') as func_file:
        acc = func_file.readlines()
    sel4funckey = QLabel()
    sel4funckey.setText(
        ''.join(
            (
                term.split(' --> ') [0] + '\n'
            ) for term in acc
        ) [: -1]
    )
    gwdict ['sel4funckey'].append(sel4funckey)
    coords.addWidget(
        gwdict ['sel4funckey'] [-1],
        0,
        4
    )

def sel_1_display():
    pass

def sel_2_display():
    pass

def sel_3_display():
    pass

def sel_4_display():
    pass


home_window()


#Display and exit window.
display.showMaximized()
sys.exit(
    myapp.exec()
)

"""
    Notes to self:
    domain_colouring_{insert_type}.input_list is a dict of the form:
        {
            'sat': ~,
            'acu': ~,
            'cgp': ~,
            'rel': ~,
            'reu': ~,
            'iml': ~,
            'imu': ~,
            'relid': ~,
            'reuid': ~,
            'imlid': ~,
            'imuid': ~,
            'func (NP)': ~
        }
"""