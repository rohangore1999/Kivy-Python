from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
	def build(self):
		screen = Screen()
		scroll = ScrollView()

		list_view = MDList()
		scroll.add_widget(list_view)

		for i in range(20):
			icon = IconLeftWidget(icon = "android")
			items = OneLineIconListItem(text = "Item: "+ str(i))

			items.add_widget(icon)
			list_view.add_widget(items)

		screen.add_widget(scroll)
		return screen

DemoApp().run()