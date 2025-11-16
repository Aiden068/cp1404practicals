from kivy.app import App
from kivy.lang import Builder


class DynamicLabels(App):
    def ___init___(self, names):
        self.names = ["test1", "test2", "test3"]
        return names


    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels(self)
        return self.root


    def create_labels(self, names):
        self.root.ids.output_label.text = "test"
        # self.root.ids.output_label.text = names(0)


DynamicLabels().run()
