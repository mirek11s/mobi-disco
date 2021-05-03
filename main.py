import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    def _test(self):
        sound = SoundLoader.load('sample3.mp3')

        if sound:
            print(f"Sound found at {sound.source} ")

        sound.play()



# http://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
