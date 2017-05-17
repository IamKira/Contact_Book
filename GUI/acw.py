"""
Add Contact Window

Окно добавления нового контакта
"""

import tkinter as Tk
import AddressBook as ab
import gui
import addcw as cw


class AddContactWindow(object):

	def close_window(self):
		self.top.destroy()


	def field_return(self):
		"""Захватывает данные контактной формы и отправляет их в add_contact() в
		AddressBook.py.
		"""

		# Список для хранения данных формы
		field_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
		
		# Получить данные формы
		first = self.first_name.get()
		last = self.last_name.get()
		st1 = self.address1.get()
		st2 = self.address2.get()
		city = self.city.get()
		state = self.state.get()
		zip = self.zip.get()
		home = self.home.get()
		mobile = self.mobile.get()
		email = self.email.get()
		bday = self.birthday.get()
		notes = self.notes.get()

		field_vars = [first, last, st1, st2, city, state, zip, home, mobile, email, bday, notes]

		# Добавить данные в поле field_list
		for i in range(12):
			field_list[i] = field_vars[i]

		# Если контактная запись имеет имя, добавить запись
		#	Иначе, вывести предупреждение об отсутствии имени
		if field_list[0] != '':
			ab.add_contact(field_list)
		
		else:
			self.c=cw.ConfirmationWindow(self.master)

		gui.mainWindow(self.master).search_query(gui.mainWindow(self.master).sort.get())
		self.close_window()


	def __init__(self,master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title('Add Contact')

		self.first_name_label = Tk.Label(top, text = 'First Name:')
		self.first_name_label.grid()

		#Ввод имени для контакта
		self.first_name = Tk.Entry(top)
		self.first_name.grid(row = 0, column = 1, padx = 10)

		self.last_name_label = Tk.Label(top, text = 'Last Name:')
		self.last_name_label.grid(row = 1) 

		#Ввод фамилии для контакта
		self.last_name = Tk.Entry(top)
		self.last_name.grid(row = 1, column = 1)

		self.address1_label = Tk.Label(top, text = 'Address 1:')
		self.address1_label.grid(row = 2)

		#Ввод адреса1
		self.address1 = Tk.Entry(top)
		self.address1.grid(row = 2, column = 1)

		self.address2_label = Tk.Label(top, text = 'Address 2:')
		self.address2_label.grid(row = 3)

		#Ввод адреса2
		self.address2 = Tk.Entry(top)
		self.address2.grid(row = 3, column = 1)

		self.city_label = Tk.Label(top, text = 'City:')
		self.city_label.grid(row = 4)

		#Ввод города
		self.city = Tk.Entry(top)
		self.city.grid(row = 4, column = 1)

		self.state_label = Tk.Label(top, text = 'State:')
		self.state_label.grid(row = 5)

		#Ввод региона
		self.state = Tk.Entry(top)
		self.state.grid(row = 5, column = 1 )

		self.zip_label = Tk.Label(top, text= 'Zip:')
		self.zip_label.grid(row = 6)

		#Ввод почтового индекса
		self.zip = Tk.Entry(top)
		self.zip.grid(row = 6, column = 1)

		# Ввод домашнего телефона
		self.home_label = Tk.Label(top, text = 'Home Phone:')
		self.home_label.grid(row = 7)

		self.home = Tk.Entry(top)
		self.home.grid(row = 7, column = 1)

		# Ввод мобильного телефона
		self.mobile_label = Tk.Label(top, text = 'Mobile Phone:')
		self.mobile_label.grid(row = 8)

		self.mobile = Tk.Entry(top)
		self.mobile.grid(row = 8, column = 1)
		
		self.email_label = Tk.Label(top, text = 'Email:')
		self.email_label.grid(row = 9)

		#Ввод email
		self.email = Tk.Entry(top)
		self.email.grid(row = 9, column = 1)

		self.birthday_label = Tk.Label(top, text = 'Birthday:')
		self.birthday_label.grid(row = 10)

		#Ввод дня рождения
		self.birthday = Tk.Entry(top)
		self.birthday.grid(row = 10, column = 1)

		self.notes_label = Tk.Label(top, text = "Notes")
		self.notes_label.grid(row = 11)

		#Ввод заметок
		self.notes = Tk.Entry(top)
		self.notes.grid(row = 11, column = 1)

		self.cancel_button = Tk.Button(top, text = 'Cancel', command = self.close_window)
		self.cancel_button.grid(row = 12, column = 1)

		self.add_button = Tk.Button(top, text= 'Add', command = self.field_return)
		self.add_button.grid(row = 12, column = 1, padx = 10, sticky = Tk.E)
		
