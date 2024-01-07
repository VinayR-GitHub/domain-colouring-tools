from kivy.app import App
from kivy.uix.widget import Widget


class MyApp(Widget):
    pass


class MyApplication(App):
    def build(self):
        return MyApp()


if __name__ == '__main__':
    MyApplication().run()