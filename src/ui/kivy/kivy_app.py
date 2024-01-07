from kivy.app import App
from kivy.uix.widget import Widget


class MyApp(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyApp()


if __name__ == '__main__':
    MyApp().run()