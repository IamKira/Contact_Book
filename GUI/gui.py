"""
Address Book GUI
"""
import sys
sys.path.insert(0, '..')

import tkinter as Tk
import AddressBook as ab
import db 	# Database backend
import new 	# New address book window
import ecw 	# Edit Contact Window
import acw 	# Add Contact Window
import dcw  # Confirmation Window
import ns 	# Warning window when user tries delete/edit no selection
import about 	# About window

class mainWindow(object):
			
	def search_call(self):
		self.search_query(self.sort.get())


	def search_query(self, sort):
		"""Получить записи на основе строки поиска. Строка поиска по умолчанию - ''.

		Keyword arguments:
		sort -- Способ сортировки (фамилия или индекс)
		"""
		self.book_list.delete(0, Tk.END)

		for contact in ab.search(self.search_bar.get(), sort):
			self.book_list.insert(Tk.END, contact[0] + " " + contact[1])


	def delete_contact(self, name):
		"""Удаляет выбранный контакт

		Keyword arguments:
		name -- Имя удаляемого контакта
		"""
		ab.remove_contact(name)
		self.search_query(self.sort.get())


	def popupAdd(self):
		"""Открыть окно 'Добавить контакт'"""
		self.w=acw.AddContactWindow(self.master)
		self.master.wait_window(self.w.top)


	def popupEdit(self):
		"""Открыть окно 'Редактировать контакт'"""
		try:
			name = str(self.book_list.get(self.book_list.curselection()))
			entry = []

			try:
				entry.append(name.split()[0])
			except:
				entry.append('')

			try:
				entry.append(name.split()[1])
			except:
				entry.append('');

			entry_id = db.get_id(entry)
			self.k=ecw.EditContactWindow(self.master, name, entry_id)
			self.master.wait_window(self.k.top)
		except:
			self.c=ns.ConfirmationWindow(self.master)


	def popup_confirmation(self):
		"""Открыть окно подтверждения удаления контакта"""
		try:
			name = str(self.book_list.get(self.book_list.curselection()))
			self.c=dcw.ConfirmationWindow(self.master, name)
			self.master.wait_window(self.c.top)
		except:
			self.c=ns.ConfirmationWindow(self.master)





	def open_about(self):
		"""Открыть окно 'about'"""
		self.c = about.About_Window(self.master)


	def save(self):
		db.db_commit()


	def quit(self):
		sys.exit()


	def noEdit(self):
		"""Текствовый поля в главном окне только для чтения"""
		self.first_name.configure(state='readonly')
		self.last_name.configure(state='readonly')
		self.address1.configure(state='readonly')
		self.address2.configure(state='readonly')
		self.city.configure(state='readonly')
		self.state.configure(state='readonly')
		self.zip.configure(state='readonly')
		self.home.configure(state='readonly')
		self.mobile.configure(state='readonly')
		self.email.configure(state='readonly')
		self.birthday.configure(state='readonly')
		self.notes.configure(state='readonly')


	def onSelect(self,event):
		"""Отображение контактной информации, когда выбран контакт из списка контактов
		"""
		w = event.widget

		try:
			name = str(self.book_list.get(self.book_list.curselection()))
			self.clearTextEntries()
			
			name_entry = ab.get_contact(name)
			
			self.first_name.insert(0,str(name_entry[0]))
			self.last_name.insert(0,str(name_entry[1]))
			self.address1.insert(0,str(name_entry[2]))
			self.address2.insert(0,str(name_entry[3]))
			self.city.insert(0,str(name_entry[4]))
			self.state.insert(0,str(name_entry[5]))
			self.zip.insert(0,str(name_entry[6]))
			self.home.insert(0,str(name_entry[7]))
			self.mobile.insert(0,str(name_entry[8]))
			self.email.insert(0,str(name_entry[9]))
			self.birthday.insert(0,str(name_entry[10]))
			self.notes.insert(0,str(name_entry[11]))

			# Нельзя редактировать запись, отображаемую в главном окне, если не нажата кнопка 'изменить'
			self.first_name.configure(state='readonly')
			self.last_name.configure(state='readonly')
			self.address1.configure(state='readonly')
			self.address2.configure(state='readonly')
			self.city.configure(state='readonly')
			self.state.configure(state='readonly')
			self.zip.configure(state='readonly')
			self.home.configure(state='readonly')
			self.mobile.configure(state='readonly')
			self.email.configure(state='readonly')
			self.birthday.configure(state='readonly')
			self.notes.configure(state='readonly')

		except:
			return


	def clearTextEntries(self):
		"""Удаление значений в полях при выборе другого контакта
		"""
		self.first_name.configure(state='normal')
		self.last_name.configure(state='normal')
		self.address1.configure(state='normal')
		self.address2.configure(state='normal')
		self.city.configure(state='normal')
		self.state.configure(state='normal')
		self.zip.configure(state='normal')
		self.home.configure(state='normal')
		self.mobile.configure(state='normal')
		self.email.configure(state='normal')
		self.birthday.configure(state='normal')
		self.notes.configure(state='normal')

		self.first_name.delete(0,Tk.END)
		self.last_name.delete(0,Tk.END)
		self.address1.delete(0,Tk.END)
		self.address2.delete(0,Tk.END)
		self.city.delete(0,Tk.END)
		self.state.delete(0,Tk.END)
		self.zip.delete(0,Tk.END)
		self.home.delete(0,Tk.END)
		self.mobile.delete(0,Tk.END)
		self.email.delete(0,Tk.END)
		self.birthday.delete(0,Tk.END)
		self.notes.delete(0,Tk.END)


	def __init__(self,master):
		self.master = master
		master.title('Address Book')

		# Menu bar
		menuBar = Tk.Menu(self.master)
		options = Tk.Menu(menuBar, tearoff = 0)

		# File Menu
		options.add_command(label = "Save", command = self.save)
		options.add_command(label = "Quit", command = self.quit)
		options.add_separator()
		menuBar.add_cascade(label = "File", menu = options)

		# Help Menu
		helpOptions = Tk.Menu(menuBar, tearoff = 1)
		helpOptions.add_command(label = "About", command = self.open_about)
		helpOptions.add_separator()
		menuBar.add_cascade(label="Help", menu=helpOptions)
		
		self.master.config(menu=menuBar)

		#кнопка сохранения адресной книги
		self.save_button = Tk.Button(master, text='Save', command = self.save)
		self.save_button.grid(row = 0, column = 0, sticky = Tk.W, padx = 15,
			pady = 10)
		
		# Меню сортировка
		self.sort = Tk.StringVar(master)
		self.sort.set('Last Name')

		#self.sort.get() получение параметра
		self.sort_option_menu = Tk.OptionMenu(master, self.sort, 'Last Name',
			 'Zip', command = self.search_query)
		self.sort_option_menu.grid(row = 1, column = 0, sticky = Tk.W, 
			padx = 10)

		# Полоса прокрутки
		self.scrollbar = Tk.Scrollbar(master)

		# Список контактов
		self.book_list = Tk.Listbox(master, yscrollcommand = self.scrollbar.set, 
			height=20)
		self.book_list.grid(row = 2, column = 0, rowspan = 12 , padx = 15)
		self.scrollbar.config(command = self.book_list.yview)
		self.book_list.bind('<<ListboxSelect>>', self.onSelect)
		
		# Поле поиска
		self.search_bar = Tk.Entry(master)
		self.search_bar.grid(row = 0, column = 4, padx = 10 )
		self.search_bar.insert(0, '')

		self.search_return = Tk.Button(master, text = 'Search', 
			command = self.search_call)
		self.search_return.grid(row = 0, column = 3, padx = 5)

		# Инициализация списка контактов
		self.search_query(self.sort.get())

		# Кнопка добавить контакт
		self.add_button = Tk.Button(master, text = 'Add', 
			command = self.popupAdd)
		self.add_button.grid(row = 14, column = 0, sticky = Tk.W , padx = 12) 

		# Кнопка удалить контакт
		self.delete_button = Tk.Button(master, text = 'Delete', 
			command = self.popup_confirmation)
		self.delete_button.grid(row = 14, column = 0 )

		# Кнопка редактировать контакт
		self.edit_button = Tk.Button(master, text = 'Edit', 
			command = self.popupEdit)
		self.edit_button.grid(row = 14, column = 4, padx = 10, sticky = Tk.E )

		### Поля для отображения контактной информации###
		# Имя
		self.first_name_label = Tk.Label(master, text = 'First Name:')
		self.first_name_label.grid(row= 2, column = 3)
		self.first_name = Tk.Entry(master)
		self.first_name.grid(row = 2, column = 4)

		# Фамилия
		self.last_name_label = Tk.Label(master, text = 'Last Name:')
		self.last_name_label.grid(row = 3, column = 3) 
		self.last_name = Tk.Entry(master)
		self.last_name.grid(row = 3, column = 4)

		# Адрес 1
		self.address1_label = Tk.Label(master, text = 'Address 1:')
		self.address1_label.grid(row = 4, column = 3)
		self.address1 = Tk.Entry(master)
		self.address1.grid(row = 4, column = 4)

		# Адрес 2
		self.address2_label = Tk.Label(master, text = 'Address 2:')
		self.address2_label.grid(row = 5, column = 3)
		self.address2 = Tk.Entry(master)
		self.address2.grid(row = 5, column = 4)

		# Город
		self.city_label = Tk.Label(master, text = 'City:')
		self.city_label.grid(row = 6, column = 3)
		self.city = Tk.Entry(master)
		self.city.grid(row = 6, column = 4)

		# Регион
		self.state_label = Tk.Label(master, text = 'State:')
		self.state_label.grid(row = 7, column = 3)
		self.state = Tk.Entry(master)
		self.state.grid(row = 7, column = 4 )

		# Индекс
		self.zip_label = Tk.Label(master, text= 'Zip:')
		self.zip_label.grid(row = 8, column = 3)
		self.zip = Tk.Entry(master)
		self.zip.grid(row = 8, column = 4)

		# Домашний номер
		self.home_label = Tk.Label(master, text = 'Home:')
		self.home_label.grid(row = 9, column = 3)
		self.home = Tk.Entry(master)
		self.home.grid(row = 9, column = 4)

		# Мобильный номер
		self.mobile_label = Tk.Label(master, text = 'Mobile:')
		self.mobile_label.grid(row = 10, column = 3)
		self.mobile = Tk.Entry(master)
		self.mobile.grid(row = 10, column = 4)

		# Email
		self.email_label = Tk.Label(master, text = 'Email:')
		self.email_label.grid(row = 11, column = 3)
		self.email = Tk.Entry(master)
		self.email.grid(row = 11, column = 4)

		# День рождения
		self.birthday_label = Tk.Label(master, text = 'Birthday:')
		self.birthday_label.grid(row = 12, column = 3)
		self.birthday = Tk.Entry(master)
		self.birthday.grid(row = 12, column = 4)

		# Заметки
		self.notes_label = Tk.Label(master, text = "Notes")
		self.notes_label.grid(row = 13, column = 3 )
		self.notes = Tk.Entry(master)
		self.notes.grid(row = 13, column = 4)
		
		self.noEdit()	# Поля только для чтения