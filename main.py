from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MainApp(App):
	def build(self):
		layout = GridLayout(cols=2, row_force_default = True, row_default_height=40, spacing=10, padding=10)

		self.weight = TextInput(text="Enter the weight: ")
		self.height = TextInput(text="Enter the height: ")

		submit = Button(text="Submit", on_press=self.getweight)

		layout.add_widget(self.weight)
		layout.add_widget(self.height)
		layout.add_widget(submit)

		return layout

	def getweight(self, obj):
		print("Weight", self.weight.text)
		print("Height", self.height.text)

MainApp().run()