from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500)

#flow
# Screen -> BoxLayout -> MDToolbar + Widget

toolbar_helper = """
Screen:
	BoxLayout:
		orientation: 'vertical'
		MDToolbar:
			title: "Demo App"
			left_action_items: [['menu',lambda x:app.navigation_draw()]]
			elevation: 10

		MDLabel:
			text: "Hello"
			halign: 'center'

		MDBottomAppBar:
			MDToolbar:
				title: "Demo App"
				left_action_items: [['menu',lambda x:app.navigation_draw()]]
				mode: 'free-end'
				type: 'bottom'
				icon: 'whatsapp'
				on_action_button: app.navigation_draw()
"""

class DemoApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = 'Red'
		screen = Builder.load_string(toolbar_helper)
		return screen

	def navigation_draw(self):
		print("menu clicked")

DemoApp().run()