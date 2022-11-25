#!python3
# main.py
# A Z-Fix program using Kivy as GUI.

import kivy
import func
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class Handler(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_first()

    def check_first(self):

        try:
            # Checks if 'fix.txt' exists.
            if os.path.exists(func.path + 'fix.txt') == False:
                raise Exception(
                    "File does not exist, proceeding to create file.")
        except:
            # Creates 'fix.txt' and lets the user save a fixed position.
            with open(func.path + 'fix.txt', 'w+') as f:
                eval_data = {}
        # end try

    def validate_z(self, desired_z):
        ''' Checks if the user input is formatted correctly.

        Returns:
            Float: A float containing the desired Z-position.
        '''

        print('test')

        '''cordinate_test = re.compile(r"\d+[\.|,]\d{3}")
        mo = re.fullmatch(cordinate_test, desired_z)

        if mo is None:
            return 'error'

        if ',' in desired_z:
            desired_z = desired_z.replace(',', '.')
        return desired_z'''


"""    def new_fix(eval_data, placement, desired_z):
        ''' new_fix lets the user create and save a new fixed position

        Args:
            eval_data (Dictionary): A Dictionary over all saved fixed positions.

        Returns:
            NoneType: Returns a matchobject or None.
        '''

        adder = eval_data
        adder[placement] = desired_z

        with open(path + 'fix.txt', 'w') as f:
            add_data = f.write(str(adder))

        return adder

    self.check_first(self)"""


class ZFix(App):

    def build(self):
        return Handler()


if __name__ == "__main__":
    ZFix().run()
