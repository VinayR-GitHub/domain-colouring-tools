from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):

    def build(self):
        box = BoxLayout()
        #box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

import os
import sys

parent_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(parent_dir)

from graphing import domain_colouring_universal

MyApp().run()