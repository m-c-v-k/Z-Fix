#! python3
# main.py
# A Z-Fix program using Kivy as GUI.


import func
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class ZFix(App):

    def build(self):

        header = Label(text='Z Fix')

        fix_pos = TextInput(
            hint_text='Fix höjd',
            height=10
        )
        fix_submit = Button(
            text='Enter'
        )

        laser_pos = TextInput(
            hint_text='Stickans höjd',
            height=10
        )
        laser_submit = Button(
            text='enter'
        )

        layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.7)
        )
        layout.add_widget(header)
        layout.add_widget(fix_pos)
        layout.add_widget(fix_submit)
        layout.add_widget(laser_pos)
        layout.add_widget(laser_submit)

        root = BoxLayout(
            orientation='vertical'
        )
        root.add_widget(layout)

        return root


if __name__ == "__main__":
    ZFix().run()
