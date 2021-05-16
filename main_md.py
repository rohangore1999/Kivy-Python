from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helper import username_helper
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

class DemoApp(MDApp):
	def build(self):
		screen = Screen()

		self.theme_cls.primary_palette = "Green"

		# username = MDTextField(text="Enter your name", pos_hint={'center_x':0.5,'center_y':0.5}, size_hint=(0.5,1))
		self.username = Builder.load_string(username_helper)
		button = MDRectangleFlatButton(text="Submit", pos_hint={'center_x':0.5,'center_y':0.4}, on_release=self.show)
		
		screen.add_widget(self.username)
		screen.add_widget(button)
		return screen

	def show(self, obj):
		if self.username.text is "":
			check_str = "Please enter Username"
		else:
			check_str = self.username

		close = MDFlatButton(text="Close", on_release = self.close_dialog)
		more = MDFlatButton(text="More")
		self.dialog = MDDialog(title="Username Check",text=check_str, size_hint=(0.7,1),
			buttons=[close,more])
		self.dialog.open()

	def close_dialog(self,obj):
		self.dialog.dismiss()
DemoApp().run()