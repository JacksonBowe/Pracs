
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConverterApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Scratch.kv')
        return self.root

    def handle_calculate(self):
        value = self.check_input_miles()
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.check_input_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def check_input_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConverterApp().run()

# class SquareNumberApp(App):
#     """ SquareNumberApp is a Kivy App for squaring a number """
#     def build(self):
#         """ build the Kivy app from the kv file """
#         Window.size = (500, 500)
#         self.title = "Square Number"
#         self.root = Builder.load_file('squaring.kv')
#         return self.root