# from idlelib.configdialog import changes

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        Window.size = (500, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self):
        value = self.get_miles(self)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


    def handle_direction(self, change):
        value = self.get_miles(self) + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()


    def get_miles(self, value):
        while value == float(self.root.ids.input_miles.text):
            return value
        else:
            return 0


MilesConverterApp().run()
