from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from View.MainScreen.MainScreenView import MainScreenView
from View.OneScreen.OneScreenView import OneScreenView
from View.TwoScreen.TwoScreenView import TwoScreenView
class MainApp(MDApp):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.sm = MDScreenManager()
		self.load_all_kv_files(self.directory)
		self.email = list()
		self.senha = list()
	def build(self):
		#Adicione aqui as classe para screenmanager
		self.sm.add_widget(MainScreenView())
		self.sm.add_widget(OneScreenView())
		self.sm.add_widget(TwoScreenView())
		return self.sm
	def on_stop(self):
		print(self.email)
	def emailapeend(self):
		print('foi camado')
MainApp().run()